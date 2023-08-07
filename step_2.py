import difflib


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def main():
    # Prompt for the first file name
    file1 = "BFSv1.c"

    try:
        lines1 = read_file(file1)
    except FileNotFoundError:
        print(f"Error: The file '{file1}' does not exist.")
        return

    # Prompt for the second file name
    file2 = "BFSv2.c"

    try:
        lines2 = read_file(file2)
    except FileNotFoundError:
        print(f"Error: The file '{file2}' does not exist.")
        return

    # Calculate the line numbers and display the differences
    differ = difflib.ndiff(lines1, lines2)
    current_line = 0

    for line in differ:
        code = line[0]
        text = line[2:]

        if code in (" ", "+"):
            current_line += 1

        if code == " ":
            continue
        elif code == "-":
            print(f"Line {current_line} in {file1}: {text}", end="")
        elif code == "+":
            print(f"Line {current_line} in {file2}: {text}", end="")


if __name__ == "__main__":
    main()
