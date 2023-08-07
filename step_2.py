import difflib


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def main():
    file1 = "BFSv1.c"

    try:
        lines1 = read_file(file1)
    except FileNotFoundError:
        print(f"Error: The file '{file1}' does not exist.")
        return

    file2 = "BFSv2.c"

    try:
        lines2 = read_file(file2)
    except FileNotFoundError:
        print(f"Error: The file '{file2}' does not exist.")
        return

    # Calculate the line numbers and display the differences
    differ = difflib.ndiff(lines1, lines2)
    current_line = 0
    additions = 0
    deletions = 0

    for line in differ:
        code = line[0]
        text = line[2:]

        if code in (" ", "+"):
            current_line += 1

        if code == " ":
            continue
        elif code == "-":
            deletions += 1
        elif code == "+":
            additions += 1

    total_changes = additions + deletions
    print("\n--- Summary ---")
    print(f"Additions: {additions}")
    print(f"Deletions: {deletions}")
    print(f"Total Changes: {total_changes}")


if __name__ == "__main__":
    main()
