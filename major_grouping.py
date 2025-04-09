import pandas as pd
from map import major_map

df = pd.read_csv("./filtered data/dass_filtered_major_spec_rem.csv")  # Load the dataset


def categorize_major(major):
    if pd.isnull(major):
        return "Others"
    major_lower = major.lower()
    for category, keywords in major_map.items():
        if any(keyword in major_lower for keyword in keywords):
            return category
    return "Others"

df['major_category'] = df['major'].apply(categorize_major)



df.to_csv("./filtered data/categorized_data.csv", index=False)
