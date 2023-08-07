import git


def get_commit_diff(repo_path, commit1, commit2, file_extension=".c"):
    repo = git.Repo(repo_path)
    diff = repo.git.diff(commit1, commit2, name_only=True)
    diff_files = [file for file in diff.split("\n") if file.endswith(file_extension)]
    diff_content = ""
    for file in diff_files:
        file_diff = repo.git.diff(commit1, commit2, file, numstat=True)
        lines = file_diff.split("\n")
        for line in lines:
            added, deleted, file_path = line.split("\t")
            if file_path.endswith(file_extension):
                diff_content += f"file name : {file_path}\n"
                diff_content += f"Added {added} lines, Deleted -{deleted} lines, Total change {int(added) + int(deleted)}\n"
    return diff_content


def main():
    repo_path = "lorawan-parser"  # Replace with the path to your Git repository
    commit1 = "d005ef5fd97b851f2850ca86ea62b3fb9c50bde8"  # Replace with the commit hash of the older version
    commit2 = "ae8f547585a67fba1c052d8e9e0b5f8d50e12f8c"  # Replace with the commit hash of the newer version

    try:
        commit_diff = get_commit_diff(repo_path, commit1, commit2)
        print(commit_diff)
    except git.GitCommandError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
