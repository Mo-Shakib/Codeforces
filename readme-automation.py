import os
import shutil
import re
import subprocess
from datetime import datetime

# Define the problem difficulty levels
difficulty_levels = {
    "easy": ["A", "B"],
    "medium": ["C", "D"],
    "hard": ["E", "F", "G"]
}

print("[+] Moving files to the appropriate folders...")
# Move files to the appropriate folders and update the README files
for filename in os.listdir("."):
    if filename.endswith(".py"):
        file_path = os.path.join(".", filename)
        problem_index = filename[:-3]

        for difficulty, levels in difficulty_levels.items():
            if problem_index[-1] in levels:
                folder_path = os.path.join(".", difficulty)
                new_file_path = os.path.join(folder_path, filename)

                if os.path.exists(new_file_path):
                    print(f"[+] Replacing existing file: {new_file_path}")
                    os.remove(new_file_path)

                shutil.move(file_path, new_file_path)

                # Retrieve the problem link from the first line of the file
                problem_link = ""
                with open(new_file_path, "r") as problem_file:
                    first_line = problem_file.readline().strip()
                    match = re.search(r"#\s*(.*)", first_line)
                    if match:
                        problem_link = match.group(1)

                # Update the README file in the corresponding folder
                readme_path = os.path.join(folder_path, "README.md")

                with open(readme_path, "a") as readme_file:
                    readme_file.write(f"{problem_index} | {problem_link} | {datetime.today().strftime('%d-%m-%Y')}\n")
                break

print("[+] Updating subfolder README files...")
# Update the subfolder README files with the indexed file information
for difficulty in difficulty_levels.keys():
    folder_path = os.path.join(".", difficulty)
    readme_path = os.path.join(folder_path, "README.md")
    file_list = sorted(file for file in os.listdir(folder_path) if file != "README.md")

    with open(readme_path, "w") as readme_file:
        readme_file.write("Problem Name | Link | Added Date\n")
        readme_file.write("-------------|------|-----------\n")

        for filename in file_list:
            problem_index = filename[:-3]
            problem_link = ""

            with open(os.path.join(folder_path, filename), "r") as problem_file:
                first_line = problem_file.readline().strip()
                match = re.search(r"#\s*(.*)", first_line)
                if match:
                    problem_link = match.group(1)

            readme_file.write(f"[{problem_index}]({problem_link}) | {problem_link} | {datetime.today().strftime('%d-%m-%Y')}\n")

print("[=] Readme automation successful.")
