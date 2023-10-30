import pandas as pd

#extraction
def import_dataframe(path):
    #import dataframe
    return pd.read_csv(path)


#cleaning
def clean_dataframe(df):
    #delete duplicates
    return df.drop_duplicates(subset=["track_name","track_artist"], keep='first')







    
