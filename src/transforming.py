import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

sns.set_context("poster")
sns.set(rc={"figure.figsize": (12.,6.)})
sns.set_style("whitegrid")



def decade(year):
    if year<1969:
        return '60s'
    elif year<1979:
        return '70s'
    elif year<1989:
        return '80s'
    elif year<1999:
        return '90s'
    elif year<2009:
        return '2000s'
    elif year<=2020:
        return '2010s'
    

def create_year_decade_columns(df):
    #create column with release year of the track album
    pattern_year="(^\d{4})"
    df["track_album_release_year"]= df["track_album_release_date"].str.extract(pattern_year)
    #create column with release decade of the track album
    df["track_album_release_decade"] = pd.to_numeric(df["track_album_release_year"]).apply(decade)
    return df









def popularity(df,year):
    '''
    input: dataframe df with songs from decade 'year'
    creates an histogram displayng track_popularity of the songs in dataframe df
    '''
    popularity=sns.histplot(df, x="track_popularity", bins=30)
    plt.xlabel("Popularity")
    if year=='00':
        year==2000
    elif year=='10':
        year==2010
    plt.title(f"Popularity of songs from {year}'")
    popularity.figure.savefig(f"images/{year}/popularity_{year}.jpg", dpi=1000)
    plt.clf()




def most_popular(df,n_min):
    '''
    input: dataframe of songs from same decade, int n
    output: dataframe with at least n_min songs from that decade with highest 'track_popularity'
    '''
    best_df= df.sort_values("track_popularity", ascending=False) #sorting by popularity
    best_df = best_df.reset_index(drop=True) #rearranging the index
    p = best_df.iloc[n_min-1]["track_popularity"]
    best_df = df[df["track_popularity"]>=p] #keeping only the songs with track_popularity >= p
    return best_df


