import os
import shutil
import re

# Define the problem difficulty levels
difficulty_levels = {
    "easy": ["A", "B"],
    "medium": ["C", "D", "E"],
    "hard": ["F", "G", "H", "I", "J", "K", "L"]
}

print("[+] Moving files to the appropriate folders...")

# Move files to the appropriate folders and update the README files
for filename in os.listdir("."):
    if filename.endswith(".py"):
        file_path = os.path.join(".", filename)

        if filename.endswith(".py"):
            problem_index = filename[:-3]
        elif filename.endswith(".cpp"):
            problem_index = filename[:-4]
        elif filename.endswith(".c"):
            problem_index = filename[:-2]
        elif filename.endswith(".js"):
            problem_index = filename[:-3]
        elif filename.endswith(".java"):
            problem_index = filename[:-5]

        for difficulty, levels in difficulty_levels.items():
            if problem_index[-1] in levels:
                folder_path = os.path.join(".", difficulty)
                new_file_path = os.path.join(folder_path, filename)

                if os.path.exists(new_file_path):
                    print(f"[+] Replacing existing file: {new_file_path}")
                    os.remove(new_file_path)
                shutil.move(file_path, new_file_path)

print("[+] Updating subfolder README files...")

# Update the subfolder README files with the indexed file information
for difficulty in difficulty_levels.keys():
    folder_path = os.path.join(".", difficulty)
    readme_path = os.path.join(folder_path, "README.md")
    file_list = sorted(file for file in os.listdir(
        folder_path) if file != "README.md")

    with open(readme_path, "w") as readme_file:
        readme_file.write("Problem | Codeforces Link |\n")
        readme_file.write("-------------|------|\n")

        for filename in file_list:
            problem_index = filename[:-3]

            problem_link = ""
            try:
                with open(os.path.join(folder_path, filename), "r") as problem_file:
                    first_line = problem_file.readline().strip()
                    match = re.search(r"(#|\/\/)\s*(.*)", first_line)
                    if match:
                        problem_link = match.group(2)
                    else:
                        problem_link = "Not found!"
            except:
                problem_link = "Not found!"

            readme_file.write(f"[{problem_index}]({filename}) | {problem_link} |\n")

    readme_file.close()

print("[=] Readme update successful.")
