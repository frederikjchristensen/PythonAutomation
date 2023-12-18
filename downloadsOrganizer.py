# Import neccessary libs
import os
import shutil

# Get the user's Downloads folder path
downloads_folder = os.path.expanduser("~\\Downloads")

# Define the directories to create
media = os.path.join(downloads_folder, "Media")
pdf = os.path.join(downloads_folder, "PDF")
installers = os.path.join(downloads_folder, "Installers")
zipfiles = os.path.join(downloads_folder, "ZipFiles")

# Create the directories if they don't exist
for folder in [media, pdf, installers, zipfiles]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Organize files into directories
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    if os.path.isfile(file_path):
        # Determine the file type based on its extension
        file_extension = filename.split(".")[-1].lower()

        if file_extension in ["mp4", "mp3", "avi", "mkv", "jpg", "jpeg", "png", "gif"]:
            destination_dir = media
        elif file_extension == "pdf":
            destination_dir = pdf
        elif file_extension in ["exe", "msi"]:
            destination_dir = installers
        elif file_extension == ["zip", "7z"]:
            destination_dir = zipfiles
        else:
            continue

        # Move the file to the appropriate directory
        shutil.move(file_path, os.path.join(destination_dir, filename))

# Calculate and print the size of the Downloads folder in gigabytes (GB)
def get_folder_size_gb(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size / (1024 ** 3)  # Convert to GB

downloads_size_gb = get_folder_size_gb(downloads_folder)
print(f"Downloads folder organized successfully. Total size: {downloads_size_gb:.2f} GB")
