import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import joblib

def get_model():
    return joblib.load('clustering_model.pkl')

def get_clusters(data):
    model = get_model()
    return model.predict(data)

def read_csv(input_file):
    df = pd.read_csv(input_file)
    return df

def get_playlist(cluster):
    clustered_data = read_csv("cluster_data.csv")
    playlist = clustered_data[clustered_data["Cluster"] == cluster]
    return playlist["NaturalKey"]

def recommendation(activity, weather_code):
    predicted_cluster = get_clusters([[activity, weather_code]])
    