# def recommend_foods(df, goal='high protein', top_n=10, ascending=False):
#     goal = goal.lower()

#     if goal == 'high protein':
#         sort_col = 'Protein (g)'
#     elif goal == 'low fat':
#         sort_col = 'Total Fat (g)'
#     elif goal == 'low carb':
#         sort_col = 'Carbohydrate (g)'
#     elif goal == 'high fiber':
#         sort_col = 'Fiber, total dietary'
#     elif goal == 'low calorie':
#         sort_col = 'Energy (kcal)'
#     elif goal == 'high iron':
#         sort_col = 'Iron, Fe'
#     else:
#         raise ValueError("Unknown goal.")

#     sorted_df = df.sort_values(by=sort_col, ascending=ascending)

#     return sorted_df[['description', 'Protein (g)', 'Carbohydrate (g)', 'Total Fat (g)', 
#                       'Fiber, total dietary', 'Iron, Fe', 'Energy (kcal)']].head(top_n)
# def recommend_foods(df, goal_key='Protein (g)', top_n=10, ascending=False):
#     if goal_key not in df.columns:
#         raise ValueError(f"Column '{goal_key}' not found in DataFrame.")

#     sorted_df = df.sort_values(by=goal_key, ascending=ascending)

#     return sorted_df[['description', 'Protein (g)', 'Carbohydrate (g)', 'Total Fat (g)',
#                       'Fiber, total dietary', 'Iron, Fe', 'Energy (kcal)']].head(top_n)

# def recommend_foods(df, goal_key='Protein (g)', top_n=10, ascending=False):
#     if goal_key not in df.columns:
#         raise ValueError(f"Column '{goal_key}' not found in DataFrame.")

#     sorted_df = df.sort_values(by=goal_key, ascending=ascending)

#     return sorted_df[['description', 'Protein (g)', 'Carbohydrate (g)', 'Total Fat (g)',
#                       'Fiber, total dietary', 'Iron, Fe', 'Energy (kcal)', goal_key]].head(top_n)

# def recommend_foods(df, goal, top_n=10, ascending=False):
#     goal = goal.lower()

#     if goal == 'high protein':
#         recommendations = df.sort_values(by='Protein (g)', ascending=ascending)
#     elif goal == 'low fat':
#         recommendations = df.sort_values(by='Total Fat (g)', ascending=ascending)
#     elif goal == 'low carb':
#         recommendations = df.sort_values(by='Carbohydrate (g)', ascending=ascending)
#     elif goal == 'high fiber':
#         recommendations = df.sort_values(by='Fiber (g)', ascending=ascending)
#     elif goal == 'low calorie':
#         recommendations = df.sort_values(by='Energy (kcal)', ascending=ascending)
#     elif goal == 'high iron':
#         recommendations = df.sort_values(by='Iron (mg)', ascending=ascending)
#     else:
#         raise ValueError("Unknown goal.")

#     return recommendations[['description', 'Protein (g)', 'Carbohydrate (g)', 'Total Fat (g)', 'Fiber (g)', 'Iron (mg)', 'Energy (kcal)']].head(top_n)



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
    
    # Filter and sort
    filtered_df = df.dropna(subset=[sort_column])
    recommendations = filtered_df.sort_values(by=sort_column, ascending=ascending)

    # Display selected columns only if they exist
    columns_to_show = ['description', 'Protein (g)', 'Carbohydrate (g)', 'Total Fat (g)', 
                       'Fiber (g)', 'Iron (mg)', 'Energy (kcal)']
    existing_columns = [col for col in columns_to_show if col in recommendations.columns]

    return recommendations[existing_columns].head(top_n), sort_column
