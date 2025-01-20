import numpy as np
from sklearn.cluster import KMeans
import joblib

def get_model():
    return joblib.load('clustering_model.pkl')

def get_clusters(date):
    model = get_model()
    return model.predict(date)

def get_clustered_dataframe():
    df = ...
    return df

def get_playlist(cluster):

    df = get_clustered_dataframe()
    return df[df['cluster'] == cluster]['playlist'].values[0]