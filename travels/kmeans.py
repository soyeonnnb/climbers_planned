import pandas as pd

# 모두 import 해야 하는데 우선 막아놓음
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans  # K-Means
# from sklearn.metrics import silhouette_score, silhouette_samples  # 실루엣 계수 계산
# from sklearn.preprocessing import StandardScaler
from matplotlib import cm

from . import models as travels_models


def kmeans_run(travel):
    all_places = travels_models.Place.objects.filter(travel=travel).values(
        "name", "latitude", "longitude"
    )
    df_allplace = pd.DataFrame(list(all_places))
