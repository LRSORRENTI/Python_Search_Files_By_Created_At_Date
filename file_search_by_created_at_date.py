import os
import datetime
import platform

def find_files_created_on(date, path='.', exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = []
    
    # Convert the input date to a datetime object
    target_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    
    # Get the timestamp for the target date
    start_timestamp = datetime.datetime(target_date.year, target_date.month, target_date.day).timestamp()
    end_timestamp = datetime.datetime(target_date.year, target_date.month, target_date.day, 23, 59, 59).timestamp()

    # List to hold the files created on the target date
    created_files = []

    # Print searching message
    print("Searching...")

    # Walk through the directory
    for root, dirs, files in os.walk(path):
        # Skip excluded directories
        if any(excluded_dir in root for excluded_dir in exclude_dirs):
            continue

        for file in files:
            # Get the file's full path
            file_path = os.path.join(root, file)
            try:
                # Get the file's creation time
                creation_time = os.path.getctime(file_path)
                
                # Check if the file was created on the target date
                if start_timestamp <= creation_time <= end_timestamp:
                    created_files.append(file_path)
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            except PermissionError:
                print(f"Permission denied: {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    # Clear the searching message
    print("\r", end="")

    return created_files

# Detect the operating system
current_os = platform.system()

# Specify the date and path based on the operating system
date_to_find = "2024-06-05"
if current_os == "Windows":
    directory_path = "C:\\Users\\username\\Desktop"
elif current_os == "Linux":
    directory_path = "/home/username/Desktop"
elif current_os == "Darwin":  # macOS is identified as "Darwin" by platform.system()
    directory_path = "/Users/username/Desktop"
else:
    directory_path = "."

# Specify directories to exclude
exclude_directories = ['node_modules', '.git']

# Get the list of files created on the specified date
files_created_on_date = find_files_created_on(date_to_find, directory_path, exclude_directories)

# Print the list of files
if files_created_on_date:
    for file in files_created_on_date:
        print(file)
else:
    print("No files found.")
