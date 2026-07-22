import os
import shutil


folder_path = input("Enter the folder path: ")

files = os.listdir(folder_path)

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Spreadsheets": [".csv", ".xlsx"]
}


for file in files:

    source_file = os.path.join(folder_path, file)

    if os.path.isdir(source_file):
        continue

    file_extension = os.path.splitext(file)[1].lower()

    file_moved = False

    for folder_name, extensions in file_types.items():

        if file_extension in extensions:

            destination_folder = os.path.join(folder_path, folder_name)

            os.makedirs(destination_folder, exist_ok=True)

            destination_file = os.path.join(destination_folder, file)

            shutil.move(source_file, destination_file)

            print(file, "moved to", folder_name)

            file_moved = True

            break

    if not file_moved:

        destination_folder = os.path.join(folder_path, "Others")

        os.makedirs(destination_folder, exist_ok=True)

        destination_file = os.path.join(destination_folder, file)

        shutil.move(source_file, destination_file)

        print(file, "moved to Others")


print("\nFile organization completed successfully!")