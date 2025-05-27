# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from src.preprocess import load_and_clean_data
# from src.recommend import recommend_foods

# # Set page config
# st.set_page_config(page_title="Nutrition Recommender", layout="wide")

# def main():
#     st.title("🥗 Smart Nutrition Recommender")

#     st.markdown("""
#     Welcome to the **Smart Nutrition Recommender App**! 🎯  
#     Select a dietary goal to get a list of foods that match your health needs.
#     """)

#     # Load data
#     data_dir = "data"  # change if your data is stored elsewhere
#     df = load_and_clean_data(data_dir)

#     # User goal selection
#     goal = st.selectbox(
#         "Select Your Dietary Goal",
#         ["High Protein", "Low Fat", "Low Carb", "High Fiber", "Low Calorie", "High Iron"]
#     )

#     ascending = goal in ["Low Fat", "Low Carb", "Low Calorie"]

#     # Recommend foods
#     recommendations = recommend_foods(df, goal, top_n=10, ascending=ascending)

#     st.subheader(f"🔍 Top 10 Recommendations for: {goal}")
#     st.dataframe(recommendations, use_container_width=True)

#     # Optional: Plot top 10 as a chart
#     plot_col = "Protein (g)" if goal == "High Protein" else \
#                "Total Fat (g)" if goal == "Low Fat" else \
#                "Carbohydrate (g)" if goal == "Low Carb" else \
#                "Fiber, total dietary" if goal == "High Fiber" else \
#                "Energy (kcal)" if goal == "Low Calorie" else \
#                "Iron, Fe"

#     st.subheader(f"📊 {plot_col} Levels in Recommended Foods")
#     fig, ax = plt.subplots(figsize=(10, 5))
#     ax.barh(recommendations["description"], recommendations[plot_col], color="#48C9B0")
#     ax.invert_yaxis()
#     ax.set_xlabel(plot_col)
#     ax.set_ylabel("Food")
#     st.pyplot(fig)

#     st.markdown("---")
#     st.markdown("Built with ❤️ using Streamlit")

# if __name__ == "__main__":
#     main()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.preprocess import load_and_clean_data
from src.recommend import recommend_foods

# Mapping for user-friendly goal names
GOAL_MAPPING = {
    "High Protein": "high protein",
    "Low Fat": "low fat",
    "Low Carb": "low carb",
    "Low Calorie": "low calorie",
    "High Fiber": "high fiber",
    "High Iron": "high iron"
}

def main():
    st.set_page_config(page_title="Nutrition Recommender", layout="centered")

    st.title("🥗 Nutrition-Based Food Recommendation App")
    st.markdown("This app recommends food based on your selected nutritional goal.")

    # Load data
    data_dir = "data"  # Change if your data is elsewhere
    df = load_and_clean_data(data_dir)

    # Goal selection
    st.sidebar.header("Choose your nutrition goal:")
    goal_label = st.sidebar.selectbox("Select Goal", list(GOAL_MAPPING.keys()))
    goal_key = GOAL_MAPPING[goal_label]

    # Ascending logic for sorting
    ascending_goals = ["low fat", "low carb", "low calorie"]
    ascending = goal_key in ascending_goals

    # Get recommendations and the sorting column
    recommendations, sort_column = recommend_foods(df, goal=goal_key, top_n=10, ascending=ascending)

    # Display results
    st.subheader(f"Top 10 Foods for: {goal_label}")
    st.dataframe(recommendations)

    # Plot bar chart
    if not recommendations.empty and sort_column in recommendations.columns:
        st.subheader(f"{sort_column} Levels in Top Foods")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.barh(recommendations['description'], recommendations[sort_column], color='mediumseagreen')
        ax.set_xlabel(sort_column)
        ax.set_ylabel("Food Item")
        ax.set_title(f"Top Foods Sorted by {sort_column}")
        ax.invert_yaxis()
        st.pyplot(fig)
    else:
        st.warning("Not enough data available to generate the chart.")

if __name__ == "__main__":
    main()
