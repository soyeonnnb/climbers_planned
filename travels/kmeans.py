import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # K-Means
from sklearn.metrics import silhouette_score, silhouette_samples # 실루엣 계수 계산
from sklearn.preprocessing import StandardScaler
from matplotlib import cm
import json

from . import models as travels_models


def kmeans_run(travel):
    all_places = travels_models.Place.objects.filter(travel=travel).values("name", "latitude", "longitude")
    df_allplace = pd.DataFrame(all_places)

    X_features = df_allplace[["latitude", "longitude"]].values
    X_features_scaled = StandardScaler().fit_transform(X_features)

    best_cluster = 3
    kmeans = KMeans(n_clusters = best_cluster, random_state = 0)
    Y_labels = kmeans.fit_predict(X_features_scaled)
    Y_labels += 1
    df_allplace['Travel_Schedule'] = Y_labels

    travel_schedule_json = df_allplace.to_json(orient = 'records')

    #context = {
     #   'region_json': region_json,
    #}  #아마 html에서 이 값을 받을 때 쓰는 코드 같음    

    print(df_allplace)
    print(travel_schedule_json)

