
import os
import shutil
import hashlib
import logging
from pathlib import Path
from datetime import datetime
from collections import Counter

# File categories
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Programs": [".py", ".c", ".cpp", ".java", ".exe"],
    "Archives": [".zip", ".rar", ".7z", ".tar"]
}

# Logging configuration
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# 1. Scan folder
def scan_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Invalid folder path!")
        return []

    files = []

    for item in folder.iterdir():
        if item.is_file():
            files.append(item)

    return files


# 2. Identify extension
def identify_extension(file):
    extension = file.suffix.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


# 3. Create folders
def create_folders(folder_path):
    for category in list(FILE_TYPES.keys()) + ["Others", "Duplicates"]:
        (Path(folder_path) / category).mkdir(
            exist_ok=True
        )


# 4. Calculate file hash
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        return sha256.hexdigest()

    except OSError as error:
        logging.error(f"Hash error: {file_path} - {error}")
        return None


# 5. Detect duplicates
def detect_duplicates(files):
    hashes = {}
    duplicates = []

    for file in files:
        file_hash = calculate_hash(file)

        if file_hash is None:
            continue

        if file_hash in hashes:
            duplicates.append(file)
        else:
            hashes[file_hash] = file

    return duplicates


# 6. Organize files
def organize_files(folder_path, dry_run=True):
    folder = Path(folder_path)

    files = scan_folder(folder_path)

    if not files:
        print("No files found.")
        return

    duplicates = detect_duplicates(files)
    duplicate_names = {file.name for file in duplicates}

    create_folders(folder_path)

    moved_count = 0

    for file in files:

        if file.name in duplicate_names:
            category = "Duplicates"
        else:
            category = identify_extension(file)

        destination_folder = folder / category
        destination = destination_folder / file.name

        # Avoid overwriting files
        if destination.exists():
            print(f"Skipped existing file: {file.name}")
            logging.warning(f"Skipped: {file}")
            continue

        if dry_run:
            print(f"[PREVIEW] {file.name} -> {category}")
        else:
            try:
                shutil.move(str(file), str(destination))
                print(f"Moved: {file.name} -> {category}")
                logging.info(f"Moved {file.name} to {category}")
                moved_count += 1

            except OSError as error:
                print(f"Error moving {file.name}: {error}")
                logging.error(f"Move error: {error}")

    if not dry_run:
        print(f"\nFiles moved: {moved_count}")


# 7. Generate summary
def generate_summary(folder_path):
    files = scan_folder(folder_path)

    if not files:
        print("No files available for summary.")
        return

    extensions = Counter(
        file.suffix.lower() or "No extension"
        for file in files
    )

    total_size = sum(file.stat().st_size for file in files)

    print("\n------ FILE SUMMARY ------")
    print("Total files:", len(files))
    print("Total storage:", round(total_size / (1024 * 1024), 2), "MB")

    print("\nFiles by extension:")

    for extension, count in extensions.items():
        print(extension, ":", count)


# 8. Main menu
def main():
    print("===== PYTHON FILE ORGANIZER =====")

    folder_path = input("Enter folder path: ").strip()
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Invalid folder!")
        return

    while True:
        print("\n1. Scan folder")
        print("2. Preview organization")
        print("3. Organize files")
        print("4. Detect duplicates")
        print("5. File summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            files = scan_folder(folder_path)
            print("\nTotal files found:", len(files))

            for file in files:
                print(file.name)

        elif choice == "2":
            organize_files(folder_path, dry_run=True)

        elif choice == "3":
            confirm = input(
                "Are you sure you want to organize files? (yes/no): "
            )

            if confirm.lower() == "yes":
                organize_files(folder_path, dry_run=False)

        elif choice == "4":
            files = scan_folder(folder_path)
            duplicates = detect_duplicates(files)

            print("\nDuplicate files:")

            if duplicates:
                for file in duplicates:
                    print(file.name)
            else:
                print("No duplicates found.")

        elif choice == "5":
            generate_summary(folder_path)

        elif choice == "6":
            print("Exiting File Organizer.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
