
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
    df_clustered['cluster'] = labels  

    return df_clustered
