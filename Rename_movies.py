import os
import re


def modify_movie_name(text):
    """Modify movie filenames based on a specific pattern."""
    pattern = r"(\[.*\])?\.?([A-Za-z0-9.]*)\.(\d{2,4})\.(.+)"
    result = re.search(pattern, text)
    if result:
        # Extract and clean the name
        name = result.group(2).replace(".", " ")
        # Check for resolution in the extracted data
        resolution_match = re.search(r"(1080|720|4k|4K)", result.group(4))
        resolution = resolution_match.group() if resolution_match else ""
        # Extract the date
        release_date = result.group(3)
        return f"{name} {release_date} {resolution}p.mp4"
    return text


def find_and_rename_videos(directory):
    """Search for video files in the directory and its subdirectories, and rename them."""
    for root, _, files in os.walk(directory):
        for e, filename in enumerate(files):
            if filename.endswith(".mp4"):
                old_file_path = os.path.join(root, filename)
                
                # Check if it's a file (to avoid directories)
                if os.path.isfile(old_file_path):
                    new_filename = modify_movie_name(filename)
                    if filename != new_filename:
                        print(f"({e+1}) {new_filename}")
                        yield old_file_path, os.path.join(root, new_filename)


def main():
    """Main function to handle user interaction and file renaming."""
    while True:
        directory = input("Provide a path: ").strip()
        if not os.path.isdir(directory):
            print("Invalid directory. Please try again.")
            continue

        changes = list(find_and_rename_videos(directory))
        
        if not changes:
            print("No .mp4 files found to rename.")
        else:
            # Ask for confirmation
            confirm = input("Do you want to save changes? (y/n): ").strip().lower()
            if confirm == "y":
                for old_path, new_path in changes:
                    os.rename(old_path, new_path)
                print("Files renamed successfully.")
            else:
                print("No changes were made.")

        # Ask to run again
        run_again = input("Do you want to run the function again? (y/n): ").strip().lower()
        if run_again != "y":
            break

    print("Function execution has stopped.")
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
