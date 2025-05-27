# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt

# def cluster_foods(df, n_clusters=5):
#     features = ['Protein (g)', 'Carbohydrate (g)', 'Total Fat (g)', 'Energy (kcal)']
#     data = df[features].dropna()

#     # Standardize
#     scaler = StandardScaler()
#     scaled_data = scaler.fit_transform(data)

#     # KMeans
#     kmeans = KMeans(n_clusters=n_clusters, random_state=42)
#     labels = kmeans.fit_predict(scaled_data)

#     # Add cluster labels back to original DataFrame
#     df_clustered = df.copy()
#     df_clustered = df_clustered.loc[data.index]  # align index
#     df_clustered['cluster'] = labels

#     # Display representative foods from each cluster
#     print("\nSample foods from each cluster:\n")
#     for cluster_id in range(n_clusters):
#         cluster_items = df_clustered[df_clustered['cluster'] == cluster_id]
#         print(f"\nCluster {cluster_id}:")
#         print(cluster_items[['description', 'Protein (g)', 'Carbohydrate (g)', 'Total Fat (g)', 'Energy (kcal)']].head(5))

#     return df_clustered
def cluster_foods(df, n_clusters=5):
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    features = ['Protein (g)', 'Carbohydrate (g)', 'Total Fat (g)', 'Energy (kcal)']
    data = df[features].dropna()

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(scaled_data)

    df_clustered = df.loc[data.index].copy()
    df_clustered['cluster'] = labels  # lowercase 'cluster' to match app.py

    return df_clustered
