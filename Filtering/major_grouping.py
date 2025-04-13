import pandas as pd
from subprocess import run
from Filtering.map import major_mapv1, major_mapv2

df = pd.read_csv("./filtered data/dass_filtered_major_spec_rem.csv")  # Load the dataset


def categorize_major(major):
    if pd.isnull(major):
        return "Others"
    major_lower = major.lower()
    # for category, keywords in major_mapv1.items():
    for category, keywords in major_mapv2.items():
        if any(keyword in major_lower for keyword in keywords):
            return category
    return "Others"

df['major_category'] = df['major'].apply(categorize_major)



# df.to_csv("./filtered data/categorized_datav1.csv", index=False)
df.to_csv("./filtered data/categorized_datav2.csv", index=False)

# Run the verification script
run(["python", "./verify_map.py"])