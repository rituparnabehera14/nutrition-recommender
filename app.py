import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.preprocess import load_and_clean_data
from src.recommend import recommend_foods

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


    data_dir = "data"  
    df = load_and_clean_data(data_dir)


    st.sidebar.header("Choose your nutrition goal:")
    goal_label = st.sidebar.selectbox("Select Goal", list(GOAL_MAPPING.keys()))
    goal_key = GOAL_MAPPING[goal_label]

   
    ascending_goals = ["low fat", "low carb", "low calorie"]
    ascending = goal_key in ascending_goals

   
    recommendations, sort_column = recommend_foods(df, goal=goal_key, top_n=10, ascending=ascending)


    st.subheader(f"Top 10 Foods for: {goal_label}")
    st.dataframe(recommendations)

  
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
