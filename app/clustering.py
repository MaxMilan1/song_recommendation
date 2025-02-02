import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder


def get_model():
    return joblib.load('clustering_model.pkl')

def get_clusters(data):
    model = get_model()
    return model.predict(data)[0]

def read_csv(input_file):
    df = pd.read_csv(input_file)
    return df

def get_all_songs(cluster):
    # Read the CSV into a DataFrame
    clustered_data = pd.read_csv("app/cluster_data.csv")
    
    # Filter the DataFrame where "Cluster" equals the provided cluster
    natural_keys = clustered_data[clustered_data["Cluster"] == cluster]["NaturalKey"]
    
    # Read dim_song into a DataFrame
    dim_song = pd.read_csv("app/dim_song.csv")

    # Filter the DataFrame where "NaturalKey" is in the natural_keys
    songs = dim_song[dim_song["NaturalKey"].isin(natural_keys)][["Artist","Song_Title","Genre"]]

    #change index to start from 1
    songs.index = np.arange(1, len(songs) + 1)

    return songs

def recommendation(activity, weather_code):
    encoded_activity = encode_activity(activity)
    print("activity encoded", encoded_activity)
    data = [[encoded_activity, weather_code]]
    predicted_cluster = get_clusters(data)
    print("predicted cluster", predicted_cluster)
    songs = get_all_songs(predicted_cluster)
    return songs

def get_playlist(activity, weather_code, playlist_length):
    # Get the recommended songs
    songs = recommendation(activity, weather_code)
    
    # Calculate the amount of songs needed based on the desired playlist length
    amount_of_songs = playlist_length * 60 // 3

    # If there aren't enough songs, sample with replacement
    if len(songs) < amount_of_songs:
        playlist = songs.sample(n=amount_of_songs, replace=True)
    else:
        playlist = songs.sample(n=amount_of_songs)

    #change index to start from 1
    playlist.index = np.arange(1, len(playlist) + 1)

    return playlist.drop(columns=["Genre"])

def encode_activity(activity):
    activities = [
        "Run",
        "Rowing",
        "Hike",
        "Workout",
        "Walk",
        "Snowboard",
        "Ride",
        "WaterSport",
        "AlpineSki",
        "StandUpPaddling",
        "Kitesurf",
        "InlineSkate",
        "Yoga",
        "Kayaking",
        "Velomobile",
    ]
    label_encoder_type = LabelEncoder()

    label_encoder_type.fit(activities)

    return label_encoder_type.transform([activity])[0]

def recommendation_split(activity,weather_code):
    encoded_activity = encode_activity(activity)
    print("activity encoded", encoded_activity)
    data = [[encoded_activity, weather_code]]
    predicted_cluster = get_clusters(data)
    print("predicted cluster", predicted_cluster)
    songs = get_all_songs(predicted_cluster)
    return encode_activity,data, predicted_cluster, songs