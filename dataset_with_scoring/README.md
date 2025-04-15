# Dataset with Scoring

This folder contains datasets that have been updated with additional scoring columns and modifications to the `major_categorie` column. Below are the details of the changes made:

## New Columns Added

1. **depression_score**: Represents the calculated depression score for each entry.
2. **anxiety_score**: Represents the calculated anxiety score for each entry.
3. **stress_score**: Represents the calculated stress score for each entry.
4. **das_score**: Represents the combined DASS (Depression, Anxiety, Stress Scale) score for each entry.  
   **Formula**: `((depression_score + anxiety_score + stress_score) / 168) * 100`

## Modification to `major_category` Column

The `major_category` column, which previously contained categorical labels, has been converted into numerical values for easier processing. The mapping is as follows:

- "Computer Science": 1,
- "Engineering": 2,
- "Business": 3,
- "Medical": 4,
- "Arts": 5,
- "Sciences": 6,
- "Humanities": 7,
- "Social Sciences": 8,
- "Law": 9,
- "Agriculture": 10,
- "Military": 11,
- "Others": 0

## Script Description

1. **major_category_covertion.py**:
   - Converts the text values in the `major_category` column to numerical values based on a predefined mapping.
   - Removes the `major` column from the dataset.
