import pandas as pd
import os
def load_and_clean_data(data_dir):
    
    food = pd.read_csv(os.path.join(data_dir, "food.csv"))
    food_nutrient = pd.read_csv(os.path.join(data_dir, "food_nutrient.csv"))
    nutrient = pd.read_csv(os.path.join(data_dir, "nutrient.csv"))
    merged = pd.merge(food_nutrient, nutrient, left_on="nutrient_id", right_on="id", how="inner")
    merged = pd.merge(merged, food, on="fdc_id", how="inner")
    pivot = merged.pivot_table(
        index=["fdc_id", "description"],
        columns="name",
        values="amount",
        aggfunc="mean" 
    ).reset_index()
    pivot.columns.name = None

 
    pivot.rename(columns={
        "Protein": "Protein (g)",
        "Carbohydrate, by difference": "Carbohydrate (g)",
        "Total lipid (fat)": "Total Fat (g)",
        "Energy": "Energy (kcal)",
        "Fiber, total dietary": "Fiber (g)",
        "Iron, Fe": "Iron (mg)"
    }, inplace=True)

    
    required_columns = ["Protein (g)", "Carbohydrate (g)", "Total Fat (g)", "Energy (kcal)"]
    final_df = pivot.dropna(subset=required_columns)

    return final_df
