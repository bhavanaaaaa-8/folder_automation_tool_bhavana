
# Python File Organizer Automation

## 1. Project Description
The Python File Organizer is an automation tool that scans a selected folder and organizes files into appropriate folders based on their extensions.

It also detects duplicate files, generates file summaries, and maintains activity logs.

## 2. Features
- Scans a user-selected folder.
- Identifies files based on extensions.
- Automatically organizes files into categories.
- Detects duplicate files using SHA-256 hashing.
- Generates file summaries.
- Calculates total storage usage.
- Maintains activity logs.
- Provides a preview mode before moving files.
- Handles invalid folder paths and file errors.

## 3. Technologies Used
- Python
- os
- pathlib
- shutil
- hashlib
- logging
- datetime
- collections

## 4. File Categories

| Category | Extensions |
|---|---|
| Documents | PDF, DOCX, DOC, TXT, PPTX, XLSX |
| Images | JPG, JPEG, PNG, GIF, BMP |
| Videos | MP4, MKV, AVI, MOV |
| Audio | MP3, WAV, AAC |
| Programs | PY, C, CPP, JAVA, EXE |
| Archives | ZIP, RAR, 7Z, TAR |
| Others | Unrecognized extensions |
| Duplicates | Identical files |

## 5. Installation

No external Python libraries are required.

1. Install Python 3.
2. Save the source code as `file_organizer.py`.
3. Open a terminal in the project directory.

## 6. How to Run

Execute:

```bash
python file_organizer.py
```

Enter the folder path when prompted.

## 7. Menu Options

1. Scan Folder
2. Preview Organization
3. Organize Files
4. Detect Duplicates
5. File Summary
6. Exit

## 8. Duplicate Detection

The application uses the SHA-256 hashing algorithm to compare file contents.

Files with identical hashes are identified as duplicates and moved into the Duplicates folder during organization.

No files are automatically deleted.

## 9. Logging

The application creates an `organizer.log` file.

It records:
- File movements
- Duplicate-related activity
- Errors
- Skipped files
- Operation timestamps

## 10. File Summary

The summary displays:
- Total number of files
- Total storage occupied in MB
- Number of files grouped by extension

## 11. Safety Measures

- Validates the selected folder.
- Uses preview mode before moving files.
- Prevents overwriting existing files.
- Handles file access errors.
- Preserves duplicate files instead of deleting them.

## 12. Future Improvements

- Recursive folder scanning.
- Graphical user interface.
- Scheduled automatic organization.
- More file categories.
- Export summaries to CSV.
- Improved duplicate detection across organized folders.

## 13. Conclusion

This project demonstrates Python file handling, automation, directory management, hashing, logging, and data analysis. It helps users maintain an organized file system while reducing manual effort.

