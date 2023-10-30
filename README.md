# What are Hits made of?


## Introduction 
The aim of this project is to analyze a dataset containing Spotify songs, looking for possible correlation between the popularity of a track and its feature.

Each track is carachterized by a **Popularity** value between 0 and 100. This value is calculated, in the most part, from the total number of plays the track has had and how recent those plays are; generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past.

In addition, to each Spotify track are associated values from 0 to 1 for the following features:
- **Danceability**: describes how suitable a track is for dancing based on a combination of musical elements including tempo, hythm stability, beat strength, and overall regularity. (0.0 is least danceable and 1.0 is most danceable);
- **Energy**: represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy;
- **Valence**: describes the musical positiveness conveyed by the track. 



## Dataset
Datasources: 

- https://www.kaggle.com/datasets/sujaykapadnis/spotify-songs (available dataset)
- https://developer.spotify.com/documentation/web-api (Spotify API)


## Workflow/Methodology 
This code was written in Python/Jupyter Notebook, using the following libraries:
- Numpy
- Pandas
- matplotlib.pyplot
- Seaborn
- requests 
- dotenv
- time

Since the majority of the tracks in the Kaggle database were released after 1990, I used Spotify API to get more songs from the previous years and joined them to the initial dataframe.

Duplicated tracks and tracks from playlists of specific artists were deleted.


## Analysis&Results

The analysis of correlation between track popularity and track features was carried out depending on the release date of the tracks.

In order to do so, new dataframes were created containing tracks of different decades (60s, 70s, 80s, 90s, 2000s and 2010s), thanks to the previous introduction of two new columns in the Dataframe *'track_album_release_year'* and *'track_album_release_decade'*.

The results are shown below, respectively for values of Danceability, Energy and Valence compared to values of track Popularity.

<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/60s/danceability_lineplot.jpg" width="370" />  <img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/70s/danceability_lineplot.jpg" width="370" />

<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/80s/danceability_lineplot.jpg" width="370" /> <img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/90s/danceability_lineplot.jpg" width="370" />

<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/2000s/danceability_lineplot.jpg" width="370" /> <img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/2010s/danceability_lineplot.jpg" width="370" />




<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/60s/energy_lineplot.jpg" width="370" /> <img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/70s/energy_lineplot.jpg" width="370" />

<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/80s/energy_lineplot.jpg" width="370" /> <img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/90s/energy_lineplot.jpg" width="370" />

<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/2000s/energy_lineplot.jpg" width="370" /> <img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/2010s/energy_lineplot.jpg" width="370" />





<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/60s/valence_lineplot.jpg" width="370" /> <img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/70s/valence_lineplot.jpg" width="370" />

<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/80s/valence_lineplot.jpg" width="370" /> <img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/90s/valence_lineplot.jpg" width="370" />

<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/2000s/valence_lineplot.jpg" width="370" /> <img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/2010s/valence_lineplot.jpg" width="370" />





Subsequently, only the most popular songs from each decade were taken into consideration, to check how track features has changed throughout decades for the most popular songs.


<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/all_decades/danceability.jpg" width="450" />

<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/all_decades/energy.jpg" width="450" />

<img src="https://github.com/luciaaguzzoni/project-II/blob/main/images/all_decades/valence.jpg" width="450" />



## Conclusion



## Links
Project Presentation: https://www.canva.com/design/DAFyp7097VM/IheuZ0CFngyBh7lsxXYGlg/edit?utm_content=DAFyp7097VM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton