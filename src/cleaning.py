import pandas as pd

#importing dataframe
spotify = pd.read_csv("../data/spotify_songs.csv")

#delete duplicates
spotify = spotify.drop_duplicates(subset=["track_name","track_artist"], keep='first')

#creating column with release year of the track albums
pattern_year="(^\d{4})"
spotify["track_album_release_year"]= spotify["track_album_release_date"].str.extract(pattern_year)