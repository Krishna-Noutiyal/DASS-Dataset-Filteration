# Dataset with Scoring

This folder contains datasets that have been updated with additional scoring columns and modifications to the `major_categorie` column. Below are the details of the changes made:

## New Columns Added

1. **depression_score**: Represents the calculated depression score for each entry.
2. **anxiety_score**: Represents the calculated anxiety score for each entry.
3. **stress_score**: Represents the calculated stress score for each entry.
4. **das_score**: Represents the combined DASS (Depression, Anxiety, Stress Scale) score for each entry. ( Its percentage of summation of depression_score, anxiety_score and stress_score ). Formula : upper(((depression_score + anxiety_score + stress_score) / 168) * 100)

## Modification to `major_categorie` Column

The `major_categorie` column, which previously contained categorical labels, has been converted into numerical values for easier processing. The mapping is as follows:

- `Depression` → `0`
- `Anxiety` → `1`
- `Stress` → `2`
- `Normal` → `3`

These changes aim to enhance the usability of the dataset for analysis and machine learning tasks.

## Usage

You can use this updated dataset for research and analysis involving mental health scoring and classification.
