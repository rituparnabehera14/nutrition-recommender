def recommend_foods(df, goal='high protein', top_n=10, ascending=False):
    goal = goal.lower()

    goal_column_mapping = {
        'high protein': 'Protein (g)',
        'low fat': 'Total Fat (g)',
        'low carb': 'Carbohydrate (g)',
        'low calorie': 'Energy (kcal)',
        'high fiber': 'Fiber (g)',
        'high iron': 'Iron (mg)',
    }

    if goal not in goal_column_mapping:
        raise ValueError("Unknown goal.")

    sort_column = goal_column_mapping[goal]
    
   
    filtered_df = df.dropna(subset=[sort_column])
    recommendations = filtered_df.sort_values(by=sort_column, ascending=ascending)

   
    columns_to_show = ['description', 'Protein (g)', 'Carbohydrate (g)', 'Total Fat (g)', 
                       'Fiber (g)', 'Iron (mg)', 'Energy (kcal)']
    existing_columns = [col for col in columns_to_show if col in recommendations.columns]

    return recommendations[existing_columns].head(top_n), sort_column
