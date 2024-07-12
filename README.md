# File Search by Creation Date Script

## Overview

**This Python script searches for files created on a specific date within a given directory and its subdirectories. It is particularly useful for identifying files created on a particular day, helping with tasks such as file organization, data analysis, and monitoring changes in a directory.**

## How It Works

***The script performs the following steps:***
1. Converts the specified date into a datetime object.
2. Calculates the timestamp range for the entire day.
3. Walks through the specified directory and its subdirectories.
4. Checks the creation time of each file and compares it with the timestamp range for the specified date.
5. Collects and prints the paths of the files created on the specified date.
6. Skips directories that are specified in the exclusion list (e.g., `node_modules`, `.git`).

## Usage

### Requirements

- Python 3.x

### How to Run the Script

1. Save the script to a file named `file_search_by_created_at_date.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Modify the directory_path variable for your system
```
directory_path = "C:\\Users\\John\\Desktop\\Projects" 
```
5. Run the script using the command:
   ```bash
   python file_search_by_created_at_date.py
   ```

### Script Parameters

- date_to_find: The date for which you want to find the files, formatted as YYYY-MM-DD.
- directory_path: The root directory where the search will begin.
- exclude_directories: A list of directories to be excluded from the search.

### Modifying the Script

1. Change the Search Date:

Update the date_to_find variable to the desired date.
```bash
date_to_find = "2024-06-05"  # Change this to your desired date
```

2. Change the Search Directory:

Update the directory_path variable to the desired root directory
```bash
directory_path = "C:\\Users\\username\\Desktop"  # Change this to your desired directory
```

3. Exclude Additional Directories:

Add or remove directory names in the exclude_directories list.
```bash
exclude_directories = ['node_modules', '.git']  # Add more directories to exclude if needed
```

4. Example Output
When the script is run, it will output the list of files created on the specified date:
``` bash
C:\Users\username\Desktop\Features_Wireframe.png
C:\Users\username\Desktop\Homepage_Sitemap.png
```

### Why It's Useful

- File Organization: Helps in organizing files by identifying those created on specific dates.
- Data Analysis: Useful for analyzing data changes and trends over time.
- Monitoring: Can be used to monitor new files added to a directory on a particular day.
- Backup Management: Helps in managing backups by identifying new files created since the last backup.

### Troubleshooting

- FileNotFoundError: The script skips files that are not found and continues with the search.
- PermissionError: The script skips files for which it does not have access permissions.
- Performance Issues: Excluding large directories like node_modules and .git can improve the script's performance.