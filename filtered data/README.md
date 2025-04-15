# Filtered Datasets

---

This directory contains multiple datasets, each filtered and processed differently to improve data quality and usability. Below is a detailed explanation of how each dataset is filtered and how the categorization and verification processes improve the grouping of the `major` field.

---

## Overview of Datasets

---

These datasets are filtered versions of the [raw dataset](./../raw%20dataset). Null and garbage records (rows) have been removed from every filtered dataset. Additionally, records with unrealistic "time taken in milliseconds to answer" values (e.g., `Q1E`, `Q32E`, etc.) have been excluded.

> **Important**: While the datasets are filtered for garbage values, some non-UTF characters may still be present. If you encounter encoding issues, consider using a more forgiving encoding such as `ISO-8859-1` or `latin1`.

---

## Datasets

### 1. **`dass_filtered_col_rem.csv`**

- **Description**: This dataset removes several unnecessary columns from the original dataset to focus on relevant fields.
- **Removed Columns**:
  - `VCL1-16`
  - `voted`
  - `race`
  - `hand`
  - `engnat`
  - `orientation`
  - `uniquenetworklocation`
  - `source`
  - `screensize`

---

### 2. **`dass_filtered_major_spec_rem.csv`**

- **Description**: Builds upon `dass_filtered_col_rem.csv` by further filtering the `major` column to remove any **special characters**. This ensures that the dataset maintains a high level of data quality and consistency.

---

### 3. **`categorized_datav1.csv`**

- **Description**: This dataset includes all the filtering done in `dass_filtered_major_spec_rem.csv`. Additionally, the `major` column is grouped into broader categories using the initial mapping dictionary (`major_mapv1`).
- **Key Features**:
  - A new column, `major_category`, is added to the dataset.
  - The `major_category` column generalizes different majors into broader categories, reducing the number of unique majors and making the dataset more manageable for analysis.
  - The mapping is based on the most common majors and their corresponding categories.

---

### 4. **`categorized_datav2.csv`**

- **Description**: Builds upon `categorized_datav1.csv` by incorporating the refined mapping dictionary (`major_mapv2`).
- **Key Features**:
  - Includes additional mappings for previously unmapped majors identified in `unmapedv1.txt`.
  - Reduces the number of unmapped majors significantly, improving the categorization process.

---

### 5. **`categorized_datav3.csv`**

- **Description**: Builds upon `categorized_datav2.csv` by using the further refined mapping dictionary (`major_mapv3`).
- **Key Features**:
  - Incorporates mappings for unmapped majors identified in `unmapedv2.txt`.
  - Adds more specific categories and keywords to handle edge cases and typos (e.g., "psychology" vs. "psycology").
  - Improves the accuracy and coverage of the `major_category` column.

---

### 6. **`categorized_datav4.csv`**

- **Description**: The most comprehensive version of the dataset, using the final mapping dictionary (`major_mapv4`).
- **Key Features**:
  - Incorporates all unmapped majors identified in `unmapedv3.txt` and `unmapedv4.txt`.
  - Achieves near-complete mapping of the `major` field, with very few or no unmapped entries remaining.
  - Provides a highly detailed and accurate grouping of academic majors.

---

## Verification Process

### Purpose

---

The verification process ensures that the mapping dictionary is continuously refined to handle the large variety of majors in the dataset. This iterative approach improves the accuracy and completeness of the `major_category` column.

### Workflow

---

1. **Initial Mapping**:
   - The dataset is processed using the initial mapping dictionary (`major_mapv1`).
   - Unmapped majors are identified and saved in `unmapedv1.txt`.

2. **Review and Refinement**:
   - The unmapped majors in `unmapedv1.txt` are reviewed to identify patterns, typos, or new fields of study.
   - Updates are made to the mapping dictionary (`major_mapv2`) to improve coverage.

3. **Iteration**:
   - The updated mapping dictionary is applied to the dataset, and the process is repeated.
   - Unmapped majors are saved in subsequent files (`unmapedv2.txt`, `unmapedv3.txt`, etc.).
   - The mapping dictionary evolves through versions (`major_mapv3`, `major_mapv4`) until the number of unmapped majors is minimized.

### Impact

---

- The iterative refinement process ensures that the mapping dictionary grows in size and detail, resulting in more accurate and comprehensive categorization.
- By `categorized_datav4.csv`, the mapping achieves near-complete coverage, with very few or no unmapped majors remaining.

---

## Summary

This directory provides a structured approach to filtering and categorizing the `major` field in the dataset. The iterative refinement of the mapping dictionary, combined with the verification process, ensures that the dataset is accurate, consistent, and ready for analysis. The evolution from `categorized_datav1.csv` to `categorized_datav4.csv` demonstrates the effectiveness of this approach, resulting in a highly detailed grouping of academic majors.
