import pandas as pd
import re
from map import major_mapv2, major_mapv3


def clean_input(text):
    """Clean and standardize the input text"""
    if pd.isnull(text):
        return ""
    # Convert to lowercase, remove extra spaces and special characters
    text = str(text).lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)  # Replace special chars with space
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with single space
    return text


def categorize_major(major):
    """Categorize a given major input into one of the predefined categories"""
    if pd.isnull(major):
        return "Others"

    cleaned_major = clean_input(major)
    if not cleaned_major:
        return "Others"

    # Check for exact matches first
    # for category, keywords in major_mapv2.items():
    for category, keywords in major_mapv3.items():
        if cleaned_major in keywords:
            return category

    # Then check for partial matches
    # for category, keywords in major_mapv2.items():
    for category, keywords in major_mapv3.items():
        if any(keyword in cleaned_major for keyword in keywords):
            return category

    return "Others"


def process_majors_from_dataset(file_path, save_path="../filtered data/processed_dataset.csv"):
    """
    Process the 'major' column from the dataset and categorize each entry.
    Args:
        file_path (str): Path to the dataset file.
        save_path (str): Path to save the processed dataset.
    """
    try:
        # Read the dataset
        df = pd.read_csv(file_path)

        # Check if 'major' column exists
        if "major" not in df.columns:
            raise ValueError("The dataset does not contain a 'major' column.")

        # Apply categorization function to the 'major' column
        df["major_category"] = df["major"].apply(categorize_major)

        # Generate some basic statistics
        category_counts = df["major_category"].value_counts()
        print("Major Categories Distribution:")
        print(category_counts)

        # Save the categorized dataset
        df.to_csv(save_path, index=False)
        print(f"Categorized dataset saved to '{save_path}'")

        return df
    except Exception as e:
        print(f"Error processing file: {e}")
        return None


process_majors_from_dataset(
    "filtered data/dass_filtered_major_spec_rem.csv",
    # "filtered data/categorized_datav2.csv",
    "filtered data/categorized_datav3.csv",
)

print("Processing completed.")
