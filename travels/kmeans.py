import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans  # K-Means
from sklearn.metrics import silhouette_score, silhouette_samples  # 실루엣 계수 계산
from sklearn.preprocessing import StandardScaler
from matplotlib import cm
import json


from . import models as travels_models


def kmeans_run(travel, count_date):
    all_places = travels_models.Place.objects.filter(travel=travel)

    all_places_df = all_places.values("name", "latitude", "longitude")
    df_allplace = pd.DataFrame(all_places_df)

    X_features = df_allplace[["latitude", "longitude"]].values
    X_features_scaled = StandardScaler().fit_transform(X_features)

    kmeans = KMeans(init = "k-means++", n_clusters=count_date, random_state=0)
    Y_labels = kmeans.fit_predict(X_features_scaled)
    Y_labels += 1
    df_allplace["Travel_Schedule"] = Y_labels
    for place, day in zip(all_places, Y_labels):
        place.day = day
        place.save()

    travel_schedule_json = df_allplace.to_json(orient="records")

    # context = {
    #   'region_json': region_json,
    # }  #아마 html에서 이 값을 받을 때 쓰는 코드 같음

    print(df_allplace)
    # print(travel_schedule_json)

def silhouetteViz(travel, count_date): 

    all_places = travels_models.Place.objects.filter(travel=travel)
    all_places_df = all_places.values("name", "latitude", "longitude")
    df_allplace = pd.DataFrame(all_places_df)

    X_features = df_allplace[["latitude", "longitude"]].values
    X_features_scaled = StandardScaler().fit_transform(X_features)

    kmeans = KMeans(init = "k-means++", n_clusters=count_date, random_state=0)
    Y_labels = kmeans.fit_predict(X_features_scaled)
    silhouette_values = silhouette_samples(X_features, Y_labels, metric='euclidean')

    y_ax_lower, y_ax_upper = 0, 0
    y_ticks = []

    for c in range(count_date):
        c_silhouettes = silhouette_values[Y_labels == c]
        c_silhouettes.sort()
        y_ax_upper += len(c_silhouettes)
        color = cm.jet(float(c) / count_date)
        plt.barh(range(y_ax_lower, y_ax_upper), c_silhouettes,
                 height=1.0, edgecolor='none', color=color)
        y_ticks.append((y_ax_lower + y_ax_upper) / 2.)
        y_ax_lower += len(c_silhouettes)
    
    silhouette_avg = np.mean(silhouette_values)
    plt.axvline(silhouette_avg, color='red', linestyle='--')
    plt.title('Number of Cluster : '+ str(count_date)+'\n' \
              + 'Silhouette Score : '+ str(round(silhouette_avg,3)))
    plt.yticks(y_ticks, range(count_date))   
    plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.ylabel('Cluster')
    plt.xlabel('Silhouette coefficient')
    plt.tight_layout()
    plt.show()


def clusterScatter(travel, count_date): 
    c_colors = []

    all_places = travels_models.Place.objects.filter(travel=travel)
    all_places_df = all_places.values("name", "latitude", "longitude")
    df_allplace = pd.DataFrame(all_places_df)

    X_features = df_allplace[["latitude", "longitude"]].values
    X_features_scaled = StandardScaler().fit_transform(X_features)

    kmeans = KMeans(init = "k-means++", n_clusters=count_date, random_state=0)
    Y_labels = kmeans.fit_predict(X_features_scaled)

    for i in range(count_date):
        c_color = cm.jet(float(i) / count_date) #클러스터의 색상 설정
        c_colors.append(c_color)
        #클러스터의 데이터 분포를 동그라미로 시각화
        plt.scatter(X_features[Y_labels == i,0], X_features[Y_labels == i,1],
                     marker='o', color=c_color, edgecolor='black', s=50, 
                     label='cluster '+ str(i))       
    
    #각 클러스터의 중심점을 삼각형으로 표시
    for i in range(count_date):
        plt.scatter(kmeans.cluster_centers_[i,0], kmeans.cluster_centers_[i,1], 
                    marker='^', color=c_colors[i], edgecolor='w', s=200)
        
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

