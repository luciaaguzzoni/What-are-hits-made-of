from src import extraction_cleaning as cl
from src import transforming as tr
from src import visualizing as viz
from src import spotify_api as sp

import pandas as pd


spotify_songs_kaggle="data/spotify_songs.csv" #path of kaggle dataset
spotify_songs_api_path = "data/more_spotify_songs.csv" #path of dataset obtained through API

api_df_already_created = True #dataset obtained through API has already been created
new_dataframe = False #any modifications in kaggle dataframe or API dataframe?


#IMPORTING

# importing - kaggle
spotify_songs = cl.import_dataframe(spotify_songs_kaggle)

#importing - API
if api_df_already_created:
     more_spotify_songs = cl.import_dataframe(spotify_songs_api_path)
else:
     dict_playlists = {
          # playlist from which extract more tracks
          # key=playlist_name : value=playlist_id
          "All Out 60s" : "37i9dQZF1DXaKIA8E7WcJj",
          "Soft 60s" : "37i9dQZF1DWYzKmy0vGGcY",
          "60s Party": "37i9dQZF1DX3AdAEX3vkB1",
          "Alternative 60s" : "37i9dQZF1DX5qNE4zrflL7",
          "I Love My 60s Funk" : "37i9dQZF1DX6vmXrF8Shld",
          "60s Country" : "37i9dQZF1DX7CGYgLhqwu5",
          "Tropicália" : "37i9dQZF1DXbEVW4FA74zM",
          "60s Rock Drive " : "37i9dQZF1DWSSWiBVaJn3j",
          "60s Music Hits | Best 60's Songs Rock, Soul, R&B, Blues, Pop Oldies Playlist" : "32f7ctSV6ZLppG27q4WIya",
          "Summer Hits of the 60s" : "37i9dQZF1DX9BDEbdcUkP2",
          "Hindi 60s-70s" : "7xhJAbAgeZnLy1XeoAhrxh",
          "60's, 70's, 80's love song" : "0UX4xBUNaotLQYLC3fvfKC",
          "Classic Rock Songs 60s 70s 80s 90s" : "6b2dBnxolvwV2L1L4thWRm",
          "60s, 70s and 80s Radio" : "5ZWmriIP1TbQQLcieku1g4",
          "60s 70s 80s Mellow & Chill" : "7saihTo4D0CbY3oRuEvbr1",
          "60s & 70s Rock" : "4xfz6zwuiOKePIkCd77vmd",
          "60 70 80 Hits" : "39B23QVYhuUK7xJuJUVVbN",
          #"English Oldies 60s 70s 80s" : "266GhFlFvS5VxZ2V3rjEKW",
          #"Greatest hits 60s 70s 80s" : "0dTWJPmCobQUb3rji1VpKi",
          #"Witchy 60s & 70s" : "1VVWowwhS6HXwT8ItmL730",
          #"Gold Classic 60s 70s 80s 90s" : "4RmVjbovY05t3IEMYyHtDC",
          #"All Out 90s" : "37i9dQZF1DXbTxeAdrVG2l",
          #"90s Party" : "37i9dQZF1DXdo6A3mWpdWx",
          #"I Love My '90s Hip-Hop'" : "37i9dQZF1DX186v583rmzp",
          #"90s Road Trip" : "37i9dQZF1DX76cnmxfAAhD",
          #"All Out 70s" : "37i9dQZF1DWTJ7xPn4vNaz",
          #"70s Party" : "37i9dQZF1DX1Hya1sRqqxI",
          #"70s Soul Classics" : "37i9dQZF1DWULEW2RfoSCi",
          #"Soft 70s" : "37i9dQZF1DWTTn6daQVbOa"
     }
     more_spotify_songs = sp.dataframe_from_api(dict_playlists, spotify_songs_api_path)


#concatenate kaggle dataframe and API dataframe
spotify_songs =  pd.concat([spotify_songs,more_spotify_songs], ignore_index=True) 




#CLEANING
spotify_songs = cl.clean_dataframe(spotify_songs) #removing duplicated tracks


#TRANSFORMATION

#transforming dataframe (create two new columns: track_album_release_year, track_album_release_decade)
spotify_songs = tr.create_year_decade_columns(spotify_songs)





#creating dataframes for each decade
spotify60 = spotify_songs[pd.to_numeric(spotify_songs["track_album_release_year"])<1970]
spotify70 = spotify_songs[(pd.to_numeric(spotify_songs["track_album_release_year"])>=1970) & (pd.to_numeric(spotify_songs["track_album_release_year"])<1980)]
spotify80 = spotify_songs[(pd.to_numeric(spotify_songs["track_album_release_year"])>=1980) & (pd.to_numeric(spotify_songs["track_album_release_year"])<1990)]
spotify90 = spotify_songs[(pd.to_numeric(spotify_songs["track_album_release_year"])>=1990) & (pd.to_numeric(spotify_songs["track_album_release_year"])<2000)]
spotify00 = spotify_songs[(pd.to_numeric(spotify_songs["track_album_release_year"])>=2000) & (pd.to_numeric(spotify_songs["track_album_release_year"])<2010)]
spotify10 = spotify_songs[(pd.to_numeric(spotify_songs["track_album_release_year"])>=2010) & (pd.to_numeric(spotify_songs["track_album_release_year"])<=2020)]
#saving new dataframes
spotify60.to_csv("data/spotify60.csv", index=False)
spotify70.to_csv("data/spotify70.csv", index=False)
spotify80.to_csv("data/spotify80.csv", index=False)
spotify90.to_csv("data/spotify90.csv", index=False)
spotify00.to_csv("data/spotify00.csv", index=False)
spotify10.to_csv("data/spotify10.csv", index=False)


#creating a dataframe with only most popular songs from each decade
decades =  {
     '60s':spotify60,
     '70s':spotify70,
     '80s':spotify80,
     '90s':spotify90,
     '2000s':spotify00,
     '2010s':spotify10}

for dec,df in decades.items():
     tr.popularity(df,dec) #create for each decade an histogram of popularity

#decide how many popular tracks to get from each decade (lokking at popularity histogram + number of tracks)
if new_dataframe:
     min_60s = int(input(f"Number of tracks for 60s: {len(spotify60)}. \n Insert minimum tracks for 60s: "))
     min_70s = int(input(f"Number of tracks for 70s: {len(spotify70)}. \n Insert minimum tracks for 70s: "))
     min_80s = int(input(f"Number of tracks for 80s: {len(spotify80)}. \n Insert minimum tracks for 80s: "))
     min_90s = int(input(f"Number of tracks for 90s: {len(spotify90)}. \n Insert minimum tracks for 90s: "))
     min_00s = int(input(f"Number of tracks for 2000s: {len(spotify00)}. \n Insert minimum tracks for 2000s: "))
     min_10s = int(input(f"Number of tracks for 2010s: {len(spotify10)}. \n Insert minimum tracks for 2010s: "))
else:
     min_60s = 100 #of 458
     min_70s = 150 #of 760
     min_80s = 200 #of 992
     min_90s = 400 #of 1897
     min_00s = 700 #of 3465
     min_10s = 3000 #of 19487

spotify60_popular = tr.most_popular(spotify60,min_60s)
spotify70_popular = tr.most_popular(spotify70,min_70s)
spotify80_popular = tr.most_popular(spotify80,min_80s)
spotify90_popular = tr.most_popular(spotify90,min_90s)
spotify00_popular = tr.most_popular(spotify00,min_00s)
spotify10_popular = tr.most_popular(spotify10,min_10s)

spotify_popular = pd.concat([spotify60_popular,spotify70_popular,spotify80_popular,spotify90_popular,spotify00_popular,spotify10_popular], ignore_index=True)
spotify_popular.to_csv("data/spotify_popular.csv", index=False)






#VISUALIZING

# each decades
for dec,df in decades.items():
     viz.visualize_decade_jointplot(df, dec)
     viz.visualize_decade_lineplot(df, dec)

# all decades
viz.visualize_all_decades(spotify_popular)






