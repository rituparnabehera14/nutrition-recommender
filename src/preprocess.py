import pandas as pd
import os

# def load_and_merge_data(data_dir):
#     # Load all three files
#     food = pd.read_csv(os.path.join(data_dir, "food.csv"))
#     food_nutrient = pd.read_csv(os.path.join(data_dir, "food_nutrient.csv"))
#     nutrient = pd.read_csv(os.path.join(data_dir, "nutrient.csv"))

#     # Merge food and nutrient info
#     merged = pd.merge(food_nutrient, nutrient, left_on="nutrient_id", right_on="id", how="inner")
#     merged = pd.merge(merged, food, on="fdc_id", how="inner")

#     # Pivot nutrients to columns
#     pivot = merged.pivot_table(
#         index=["fdc_id", "description"],
#         columns="name",
#         values="amount",
#         aggfunc="first"
#     ).reset_index()

#     # Rename and filter important columns
#     pivot.rename(columns={
#         "Protein": "Protein (g)",
#         "Carbohydrate, by difference": "Carbohydrate (g)",
#         "Total lipid (fat)": "Total Fat (g)",
#         "Energy": "Energy (kcal)"
#     }, inplace=True)

#     # Drop rows missing nutritional data
#     final_df = pivot.dropna(subset=["Protein (g)", "Carbohydrate (g)", "Total Fat (g)", "Energy (kcal)"])

#     return final_df
def load_and_clean_data(data_dir):
    

    # Load all data
    food = pd.read_csv(os.path.join(data_dir, "food.csv"))
    food_nutrient = pd.read_csv(os.path.join(data_dir, "food_nutrient.csv"))
    nutrient = pd.read_csv(os.path.join(data_dir, "nutrient.csv"))

    # Merge data
    merged = pd.merge(food_nutrient, nutrient, left_on="nutrient_id", right_on="id", how="inner")
    merged = pd.merge(merged, food, on="fdc_id", how="inner")

    # Pivot to wide format using mean to handle duplicates
    pivot = merged.pivot_table(
        index=["fdc_id", "description"],
        columns="name",
        values="amount",
        aggfunc="mean"  # Use mean to resolve multiple entries for the same nutrient
    ).reset_index()

    # Remove column hierarchy caused by pivot
    pivot.columns.name = None

    # Rename key nutrients
    pivot.rename(columns={
        "Protein": "Protein (g)",
        "Carbohydrate, by difference": "Carbohydrate (g)",
        "Total lipid (fat)": "Total Fat (g)",
        "Energy": "Energy (kcal)",
        "Fiber, total dietary": "Fiber (g)",
        "Iron, Fe": "Iron (mg)"
    }, inplace=True)

    # Drop rows that are missing essential nutrients
    required_columns = ["Protein (g)", "Carbohydrate (g)", "Total Fat (g)", "Energy (kcal)"]
    final_df = pivot.dropna(subset=required_columns)

    return final_df
