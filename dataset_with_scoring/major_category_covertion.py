import pandas as pd

# Load the dataset
file_path = "dataset_with_scoring/categorized_v4/categorized_datav4_scored.csv"  # Replace with the actual dataset file name
df = pd.read_csv(file_path)

# Define a mapping for the `major_category` column
major_category_mapping = {
    "Computer Science": 1,
    "Engineering": 2,
    "Business": 3,
    "Medical": 4,
    "Arts": 5,
    "Sciences": 6,
    "Humanities": 7,
    "Social Sciences": 8,
    "Law": 9,
    "Agriculture": 10,
    "Military": 11,
    "Others": 0
}

# Convert `major_category` text values to integers
df['major_category'] = df['major_category'].map(major_category_mapping)

# Drop the `major` column
df = df.drop(columns=['major'])

# Save the updated dataset
output_file_path = "dataset_with_scoring/categorized_v4/categorized_v4_numeric.csv"  # Replace with the desired output file name
df.to_csv(output_file_path, index=False)

print("Dataset updated and saved successfully.")