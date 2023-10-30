import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

sns.set_context("poster")
sns.set(rc={"figure.figsize": (12.,8.)})
sns.set_style("whitegrid")


def visualize_decade_jointplot(df, decade):
    '''
    input: df (dataframe containing tracks from same decade), decade(str) 
    creates a jointplot of popularity with each feature(danceability, energy, valence)
    '''

    # danceability and popularity 
    jointplot = sns.jointplot(data=df, x= "track_popularity", y= "danceability", color='red')  
    plt.xlabel("Popularity")
    plt.ylabel("Danceability")
    plt.suptitle(f"Danceability and Popularity of {decade} tracks", y = 1)
    jointplot.figure.savefig(f"images/{decade}/danceability_jointplot.jpg", dpi=1000)
    plt.clf()

    # energy and popularity
    jointplot = sns.jointplot(data=df, x= "track_popularity", y= "energy", color='blue')
    plt.xlabel("Popularity")
    plt.ylabel("Energy")
    plt.suptitle(f"Energy and Popularity of {decade} tracks", y = 1)
    jointplot.figure.savefig(f"images/{decade}/energy_jointplot.jpg", dpi=1000)
    plt.clf()

    # valence and popularity
    jointplot = sns.jointplot(data=df, x= "track_popularity", y= "valence", color='green')
    plt.xlabel("Popularity")
    plt.ylabel("Valence")
    plt.suptitle(f"Valence and Popularity of {decade} tracks", y = 1)
    jointplot.figure.savefig(f"images/{decade}/valence_jointplot.jpg", dpi=1000)
    plt.clf()


def visualize_decade_lineplot(df, decade):
    '''
    input: df (dataframe containing tracks from same decade), decade(str) 
    creates a lineplot of popularity with each feature(danceability, energy, valence)
    '''

    plt.tight_layout()
    plt.subplots_adjust(top=0.88)

    # danceability and popularity 
    lineplot = sns.lineplot(data=df, x= "track_popularity", y= "danceability", color ='red', estimator= 'mean')
    plt.xlabel("Popularity")
    plt.ylabel("Danceability")
    plt.title(f"Danceability and Popularity of {decade} tracks")
    lineplot.figure.savefig(f"images/{decade}/danceability_lineplot.jpg", dpi=1000)
    plt.clf()

    # energy and popularity
    lineplot = sns.lineplot(data=df, x= "track_popularity", y= "energy", color='blue', estimator= 'mean')
    plt.xlabel("Popularity")
    plt.ylabel("Energy")
    plt.title(f"Energy and Popularity of {decade} tracks")
    lineplot.figure.savefig(f"images/{decade}/energy_lineplot.jpg", dpi=1000)
    plt.clf()

    # valence and popularity
    lineplot = sns.lineplot(data=df, x= "track_popularity", y= "valence", color = 'green', estimator= 'mean')
    plt.xlabel("Popularity")
    plt.ylabel("Valence")
    plt.title(f"Valence and Popularity of {decade} tracks")
    lineplot.figure.savefig(f"images/{decade}/valence_lineplot.jpg", dpi=1000)
    plt.clf()  




def visualize_all_decades(df):
    '''
    input: song dataframes
    creates a barplot for each feature (danceability, energy, valence) of tracks popularity throughout the decades
    '''

    plt.tight_layout()
    plt.subplots_adjust(top=0.88)

    # danceability popularity throughout decades
    barplot = sns.barplot(x="track_album_release_decade", y="danceability", data=df, order = ['60s','70s','80s','90s','2000s','2010s'], color = 'red')
    plt.xlabel("Popularity")
    plt.ylabel("Danceability")
    plt.title("Danceability in most popualr tracks throughout the decades")
    barplot.figure.savefig(f"images/all_decades/danceability.jpg", dpi=1000)
    plt.clf()


    # energy popularity throughout decades
    barplot = sns.barplot(x="track_album_release_decade", y="energy", data=df, order = ['60s','70s','80s','90s','2000s','2010s'], color='blue')
    plt.xlabel("Popularity")
    plt.ylabel("Energy")
    plt.title("Energy in most popualr tracks throughout the decades")
    barplot.figure.savefig(f"images/all_decades/energy.jpg", dpi=1000)
    plt.clf()

    # valence popularity throughout decades
    barplot = sns.barplot(x="track_album_release_decade", y="valence", data=df, order = ['60s','70s','80s','90s','2000s','2010s'], color='green')
    plt.xlabel("Popularity")
    plt.ylabel("Valence")
    plt.title("Valence in most popualr tracks throughout the decades")
    barplot.figure.savefig(f"images/all_decades/valence.jpg", dpi=1000)
    plt.clf()


