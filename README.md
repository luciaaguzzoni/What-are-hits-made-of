# How to make a Hit


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

******** tracks aggiunte tramite API***********

New dataframes were created containing tracks of different decades (60s, 70s, 80s, 90s, 2000s and 2010s) and a dataframe with most popular songs from every decade (********* criterio ********)
Correlation between popularity and track features was investigated for each decade and popularity of features was compared between decades.


## Analysis&Results

![img](https://github.com/luciaaguzzoni/project-II/blob/main/images/all_decades/danceability.jpg)

![img](https://github.com/luciaaguzzoni/project-II/blob/main/images/all_decades/energy.jpg)

![img](https://github.com/luciaaguzzoni/project-II/blob/main/images/all_decades/valence.jpg)



## Conclusion


## Links
project presentation: https://www.canva.com/design/DAFyp7097VM/IheuZ0CFngyBh7lsxXYGlg/edit?utm_content=DAFyp7097VM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton