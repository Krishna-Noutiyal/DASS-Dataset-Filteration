import re
from major_grouping import major_map  # Import the major_map from map.py
# Load the major_map from map.py

# Load the majors from major.txt
with open("major.txt", "r", encoding="utf-8") as file:
    majors = file.readlines()

# Normalize the majors (lowercase, strip spaces, remove special characters)
def normalize_major(major):
    major = major.lower().strip()
    major = re.sub(r"[^a-z0-9\s]", "", major)  # Remove special characters
    return major

normalized_majors = set(normalize_major(major) for major in majors)

# Flatten the major_map keywords for comparison
mapped_keywords = {}
for category, keywords_list in major_map.items():
    for keyword in keywords_list:
        mapped_keywords[keyword] = category

# Check if each major maps to a category
unmapped_majors = []
for major in normalized_majors:
    mapped = False
    for keyword in mapped_keywords:
        if keyword in major:  # Check if keyword is in the major
            mapped = True
            break
    if not mapped:
        unmapped_majors.append(major)

# Output results
print(f"Total unique majors in major.txt: {len(normalized_majors)}")
print(f"Total unmapped majors: {len(unmapped_majors)}")
print("Unmapped majors:")
print("\n".join(unmapped_majors))