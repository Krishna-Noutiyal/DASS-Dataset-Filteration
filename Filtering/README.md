# Filtering Folder README

This folder contains scripts and resources used for processing and mapping the `major` field in the dataset. The `major` field represents the academic major of survey participants, and due to the diversity of responses, it requires cleaning and standardization for meaningful analysis. Below is an explanation of the purpose of each file in this folder, how the scripts work together, and how the mapping dictionary evolved over iterations.

---

## Files in This Folder

### 1. `major.txt`
- **Purpose**: Contains the list of all the majors present in the [raw dataset](./../raw%20dataset/data.csv). It serves as the reference for the mapping process.
- **Usage**:
    - Used to create the initial `major_mapv1` mapping dictionary present in the `map.py`.

### 2. `unmapedv1.txt`, `unmapedv2.txt`, `unmapedv3.txt`, `unmapedv4.txt`
- **Purpose**: These files contain the output of the `verify_map.py` script, listing majors that remain unmapped after applying the respective versions of the mapping dictionary (`major_mapv1`, `major_mapv2`, etc.).
- **Details**:
    - During the first iteration of the mapping process, approximately **3500 unique majors** were identified in the dataset.
    - Out of these, around **800 majors** were left unmapped after applying `major_mapv1`, which were recorded in `unmapedv1.txt`.
    - Subsequent iterations refined the mapping dictionary (`major_mapv2`, `major_mapv3`, `major_mapv4`), reducing the number of unmapped majors in each step.

### 3. `map.py`
- **Purpose**: Contains the mapping dictionaries (`major_mapv1`, `major_mapv2`, `major_mapv3`, `major_mapv4`) used to categorize the `major` field into standardized groups.
- **Details**:
    - `major_mapv1`: The initial mapping dictionary created from `major.txt`.
    - `major_mapv2`: Expanded to include unmapped majors from `unmapedv1.txt`.
    - `major_mapv3`: Further refined to include additional unmapped majors from `unmapedv2.txt`.
    - `major_mapv4`: The most comprehensive version, incorporating all unmapped majors from `unmapedv3.txt` and `unmapedv4.txt`.

### 4. `major_grouping.py`
- **Purpose**: Processes the `major` column from the dataset and maps each entry to a standardized category using the latest mapping dictionary (`major_mapv4`).
- **Details**:
    - Reads the dataset (`dass_filtered_major_spec_rem.csv`).
    - Cleans and standardizes the `major` field.
    - Applies the mapping dictionary to categorize each major.
    - Outputs the processed dataset with a new column `major_category`.

### 5. `verify_map.py`
- **Purpose**: Verifies the mapping of user-provided majors against the current version of the mapping dictionary.
- **Details**:
    - Identifies unmapped majors in the dataset.
    - Outputs the unmapped majors to a file (e.g., `unmapedv1.txt`, `unmapedv2.txt`, etc.).
    - Helps refine the mapping dictionary iteratively.

---

## Evolution of the Mapping Dictionary

### **`major_mapv1`**
- **Source**: Created from `major.txt`.
- **Size**: Contained basic groupings of majors into categories such as "Engineering," "Computer Science & IT," "Medical & Health Sciences," etc.
- **Limitations**: Left approximately **800 majors** unmapped, which were recorded in `unmapedv1.txt`.

### **`major_mapv2`**
- **Source**: Expanded to include unmapped majors from `unmapedv1.txt`.
- **Size**: Grew significantly as new keywords and patterns were added to cover edge cases and typos (e.g., "psychology" vs. "psycology").
- **Impact**: Reduced the number of unmapped majors but still left some entries unmapped, recorded in `unmapedv2.txt`.

### **`major_mapv3`**
- **Source**: Further refined using `unmapedv2.txt`.
- **Size**: Included additional categories and keywords to handle more specific fields (e.g., "game development" under "Computer Science & IT").
- **Impact**: Improved coverage but still left a small number of majors unmapped, recorded in `unmapedv3.txt`.

### **`major_mapv4`**
- **Source**: The most comprehensive version, incorporating all unmapped majors from `unmapedv3.txt`.
- **Size**: Fully detailed, with extensive keywords and categories to handle almost all unique majors in the dataset.
- **Impact**: Achieved near-complete mapping of the `major` field, with very few or no unmapped entries remaining.

---

## Workflow Overview

1. **Initial Mapping**:
   - Use `map.py` to create an initial mapping dictionary (`major_mapv1`) based on raw `major` responses.

2. **Apply Mapping**:
   - Run `major_grouping.py` to apply the mapping dictionary to the dataset and standardize the `major` field.

3. **Verify Mapping**:
   - Use `verify_map.py` to identify any unmapped majors in the dataset. The output is saved in files like `unmapedv1.txt`, `unmapedv2.txt`, etc.

4. **Refine Mapping**:
   - Review the unmapped majors in the output files and update the mapping dictionary using `map.py`.

5. **Repeat**:
   - Repeat steps 2–4 iteratively until all or most majors are mapped.

---

## Summary

This folder is designed to streamline the process of cleaning and standardizing the `major` field in the dataset. The iterative workflow ensures that the mapping dictionary is continuously refined, reducing the number of unmapped majors over time. The inclusion of `major.txt` and the `unmaped` files provides transparency and traceability in the mapping process, making it easier to track progress and address gaps.

The evolution of the mapping dictionary from `major_mapv1` to `major_mapv4` demonstrates the effectiveness of this iterative approach, resulting in a comprehensive and detailed grouping of academic majors.