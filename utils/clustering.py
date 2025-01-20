import numpy as np
from sklearn.cluster import KMeans
import joblib

def get_model():
    return joblib.load('clustering_model.pkl')

def get_clusters(date):
    model = get_model()
    return model.predict(date)


