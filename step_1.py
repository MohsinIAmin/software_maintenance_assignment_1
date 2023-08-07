def count_lines_of_code(file_path):
    with open(file_path, "r") as f:
        code_lines = [
            line.strip()
            for line in f.readlines()
            if line.strip() and not line.strip().startswith("//")
        ]
    return len(code_lines)


# Usage example:
file_path = "BFSv1.c"
lines_of_code = count_lines_of_code(file_path)
print(f"Number of lines of code in {file_path}: {lines_of_code}")
