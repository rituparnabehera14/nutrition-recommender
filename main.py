from src.preprocess import load_and_clean_data
from src.cluster import cluster_foods
from src.recommend import recommend_foods
df = load_and_clean_data("data")
print(df.head())
df_clustered = cluster_foods(df, n_clusters=5)
df = cluster_foods(df)
recommend_foods(df, goal='high protein')
print(df.columns.tolist())

