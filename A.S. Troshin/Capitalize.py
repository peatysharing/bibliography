import os

def title_case(filename):
    """Convert the filename to title case."""
    return ' '.join(word.capitalize() for word in filename.split())

def rename_files_in_directory(directory):
    """Rename files in the specified directory to title case."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Skip directories
            if os.path.isdir(os.path.join(root, filename)):
                continue
            
            # Split the filename and extension
            name, ext = os.path.splitext(filename)
            
            # Convert the name to title case
            new_name = title_case(name) + ext
            
            # Construct full file paths
            old_file = os.path.join(root, filename)
            new_file = os.path.join(root, new_name)
            
            # Rename the file
            if old_file != new_file:  # Only rename if the name has changed
                os.rename(old_file, new_file)
                print(f'Renamed: "{filename}" to "{new_name}"')

def main():
    directory = input("Enter the main directory path where the folders are located: ")
    rename_files_in_directory(directory)

if __name__ == "__main__":
    main()

