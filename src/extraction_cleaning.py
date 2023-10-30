import pandas as pd

#extraction
def import_dataframe(path):
    #import dataframe
    return pd.read_csv(path)


#cleaning
def clean_dataframe(df):

    df=df.drop_duplicates(subset=["track_name","track_artist"], keep='first') #delete duplicates

    remove_playlist = ['Coldplay – Ghost Stories (Deluxe Edition)',
        'Muse Radio - (Uprising, Starlight, Supermassive Black Hole, Madness)',
        'Someone You Loved Lewis Capaldi (Pop Music Mix)',
        'This Is Gloria Estefan',
        "This Is Guns N' Roses",
        'This Is Janelle Monáe',
        'This Is Logic',
        'This Is Scorpions',
        'This Is: Don Omar',
        'This Is: Javiera Mena'
        'Tusa - Karol G | China - Anuel AA | Estrenos Reggaeton y Música Urbana 2019',
        'Vault: Def Leppard Greatest Hits']
    df = df[~df['playlist_name'].isin(remove_playlist)] #remove playlist specific to artists

    df = df[df['track_popularity']!=0] #remove tracks with popularity=0

    return df







    
