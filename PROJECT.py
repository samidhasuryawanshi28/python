import re

def clean_content(content):
    # Remove multi-line comments
    content = re.sub(r"'''[\s\S]*?'''", "", content)
    content = re.sub(r'"""[\s\S]*?"""', "", content)
    
    # Remove single-line comments
    content = re.sub(r"#.*", "", content)
    
    # Normalize whitespace
    lines = content.splitlines()
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces
        if line:  # Ignore empty lines
            cleaned_lines.append(line)
    
    return cleaned_lines

def compare_files(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1:
        content1 = f1.read()
        
    with open(file2, "r", encoding="utf-8") as f2:
        content2 = f2.read()
    
    cleaned1 = clean_content(content1)
    cleaned2 = clean_content(content2)
    
    set1 = set(cleaned1)
    set2 = set(cleaned2)
    
    common_lines = set1.intersection(set2)
    total_unique_lines = len(set1.union(set2))
    
    if total_unique_lines == 0:
        similarity_score = 0
    else:
        similarity_score = (len(common_lines) / total_unique_lines) * 100
    
    return similarity_score, common_lines

# ---- Main Program ----
file1 = input("Enter first file path: ")
file2 = input("Enter second file path: ")

score, common = compare_files(file1, file2)

print(f"\nSimilarity Score: {score:.2f}%")
print("\nCommon Lines:")
for line in common:
    print(">>", line)