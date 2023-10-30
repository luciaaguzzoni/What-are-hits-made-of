import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

sns.set_context("poster")
sns.set(rc={"figure.figsize": (12.,6.)})
sns.set_style("whitegrid")


def visualize_decade_jointplot(df, decade):
    #jointplot for each feature

    # danceability and popularity 
    jointplot = sns.jointplot(data=df, x= "track_popularity", y= "danceability", color='red')  
    plt.xlabel("Popularity")
    plt.ylabel("Danceability")
    plt.title(f"Danceability and Popularity of {decade} tracks")
    jointplot.figure.savefig(f"images/{decade}/danceability_jointplot.jpg", dpi=1000)
    plt.clf()

    # energy and popularity
    jointplot = sns.jointplot(data=df, x= "track_popularity", y= "energy", color='blue')
    plt.xlabel("Popularity")
    plt.ylabel("Energy")
    plt.title(f"Energy and Popularity of {decade} tracks")
    jointplot.figure.savefig(f"images/{decade}/energy_jointplot.jpg", dpi=1000)
    plt.clf()

    # valence and popularity
    jointplot = sns.jointplot(data=df, x= "track_popularity", y= "valence", color='green')
    plt.xlabel("Popularity")
    plt.ylabel("Valence")
    plt.title(f"Valence and Popularity of {decade} tracks")
    jointplot.figure.savefig(f"images/{decade}/valence_jointplot.jpg", dpi=1000)
    plt.clf()


def visualize_decade_lineplot(df, decade):
    #lineplot for each decade

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

    # danceability throughout decades
    barplot = sns.barplot(x="track_album_release_decade", y="danceability", data=df, order = ['60s','70s','80s','90s','2000s','2010s'], color = 'red')
    plt.xlabel("Popularity")
    plt.ylabel("Danceability")
    plt.title("Danceability in most popualr tracks throughout the decades")
    barplot.figure.savefig(f"images/all_decades/danceability.jpg", dpi=1000)
    plt.clf()


    # energy throughout decades
    barplot = sns.barplot(x="track_album_release_decade", y="energy", data=df, order = ['60s','70s','80s','90s','2000s','2010s'], color='blue')
    plt.xlabel("Popularity")
    plt.ylabel("Energy")
    plt.title("Energy in most popualr tracks throughout the decades")
    barplot.figure.savefig(f"images/all_decades/energy.jpg", dpi=1000)
    plt.clf()

    # valence throughout decades
    barplot = sns.barplot(x="track_album_release_decade", y="valence", data=df, order = ['60s','70s','80s','90s','2000s','2010s'], color='green')
    plt.xlabel("Popularity")
    plt.ylabel("Valence")
    plt.title("Valence in most popualr tracks throughout the decades")
    barplot.figure.savefig(f"images/all_decades/valence.jpg", dpi=1000)
    plt.clf()


