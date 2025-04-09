# Filtered Datasets
---

Their are many dataset present in this directory and each dataset is filtered differently. Below is the descripion of how each dataset is filtered.


## Datasets
---
These are the datasets that has been filtered from (the raw dataset)[./../raw\ dataset]. Any null  and garbage records (rows) are already removed from every filtered dataset. Some records showed unrealistic 'time taken in milliseconds to answer that question(E)' (These are the records such as Q1E, Q32E etc.) times such as zero ... These types of records are also removed from every filtered dataset.

> [!IMPORTANT]
Although dataset are filtered for garbage values, its not neccessary every filtered dataset contains only `UTF-8` encoding. This means some non UTF characters are still present in the filtered dataset. So if you are using these filtered dataset consider a more forgiving encoding as `ISO-8859-1` or `latin1`.

### dass_filtered_col_rem.csv
---
This dataset removes several columns from the original dataset the removed columns inlude :

- VCL1-16 columns
- voted
- race
- hand
- engnat
- orientation
- uniquenetworklocation
- source
- screensize


### dass_filtered_major_spec_rem.csv
---
All of the filteration done in `dass_filtered_col_rem.csv` is also done in this dataset. In addition to that the `major` column is also filtered for any **special characters**. This ensures that the dataset maintains a high level of data quality and consistency.


### categorized_datav1.csv
---
All of the filteration done in `dass_filtered_major_spec_rem.csv` is also done in this dataset. In addition the `major` column grouped into similar majors. A new column `major_catagory` is added to the dataset. The `major_category` column contains generalizes the different majors into broader categories. This helps in reducing the number of unique majors and makes the dataset more manageable for analysis. The mapping of majors to categories is done using a mapping dictionary `major_mapv1.csv` , which is defined in the `map.py` file. The mapping is based on the most common majors and their corresponding categories.