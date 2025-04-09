# Filtering Folder README

This folder contains scripts and resources used for processing and mapping the `major` field in the dataset. The `major` field represents the academic major of survey participants, and due to the diversity of responses, it requires cleaning and standardization for meaningful analysis. Below is an explanation of the purpose of each file in this folder and how the scripts work together.

---

## Files in This Folder

### 1. `major.txt`
- **Purpose**: Contains the list of all the majors present in the [raw dataset](./../raw%20dataset/data.csv). It serves as the reference for the mapping process.
- **Usage**:
    - Used to create the initial major_mapv1 mapping dictionary present in the `map.py`.


### 2. `unmapedv1.txt`
- **Purpose**: Contains the output of the `verify_map.py` script, listing majors that remain unmapped after applying the `major_mapv1` mapping dictionary.
- **Details**:
    - During the first iteration of the mapping process, approximately **3500 unique majors** were identified in the dataset.
    - Out of these, around **800 majors** were left unmapped, which are recorded in this file.
    - Helps in identifying edge cases, typos, or new majors that need to be added to the mapping dictionary (`major_mapv1`) for better coverage.

---

## Scripts in This Folder

### 1. `verify_map.py`
- **Purpose**: Verifies the mapping of user-provided majors against the `major_mapv1` dictionary.
- **Working**:
    1. Takes the dataset containing user-provided majors as input.
    2. Attempts to map each major to a standardized major using the `major_mapv1` dictionary.
    3. Flags unmapped majors and writes them to the `unmapedv1.txt` file.
    4. The output (`unmapedv1.txt`) is then used to refine the mapping dictionary by adding new mappings or correcting existing ones.

---

## Workflow

### 1. Initial Mapping
- The dataset is processed using the `major_mapv1` dictionary to map user-provided majors to standardized ones.
- The `verify_map.py` script identifies unmapped majors and outputs them to `unmapedv1.txt`.

### 2. Review and Refinement
- The `unmapedv1.txt` file is reviewed to identify patterns, typos, or new majors that need to be added to the mapping dictionary.
- Updates are made to the `major_mapv1` dictionary to improve the mapping process.

### 3. Iteration
- The mapping process is repeated with the updated dictionary until the number of unmapped majors is minimized.

---

## Key Insights from the First Iteration
- **Unique Majors Identified**: Approximately **3500 unique majors** were found in the dataset.
- **Unmapped Majors**: Around **800 majors** were left unmapped after the first iteration.

---

### 4. **`README.md`**
This file (the one you are currently reading) provides documentation for the folder, explaining the purpose of each file and script, as well as how they work together.

---

## Workflow Overview

1. **Initial Mapping:**
   - Use `map.py` to create an initial mapping dictionary (`major_mapv1`) based on raw `major` responses.

2. **Apply Mapping:**
   - Run `major_grouping.py` to apply the mapping dictionary to the dataset and standardize the `major` field.

3. **Verify Mapping:**
   - Use `verify_map.py` to identify any unmapped majors in the dataset. The output is saved in `unmapedv1.txt`.

4. **Refine Mapping:**
   - Review the unmapped majors in `unmapedv1.txt` and update the mapping dictionary using `map.py`.

5. **Repeat:**
   - Repeat steps 2–4 iteratively until all or most majors are mapped.

---

## Summary

This folder is designed to streamline the process of cleaning and standardizing the `major` field in the dataset. The iterative workflow ensures that the mapping dictionary is continuously refined, reducing the number of unmapped majors over time. The inclusion of `major.txt` and `unmapedv1.txt` provides transparency and traceability in the mapping process, making it easier to track progress and address gaps.