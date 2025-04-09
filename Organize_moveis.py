import os
import shutil

def organize_movies(main_folder):
    # Validate the entered path
    if not os.path.exists(main_folder):
        print("The specified path does not exist. Please check the path and try again.")
        return

    # File extensions for videos and subtitles
    video_extension = '.mp4'
    subtitle_extensions = ['.srt', '.ass', '.sub']

    # Iterate through files in the main folder
    for file in os.listdir(main_folder):
        file_path = os.path.join(main_folder, file)
        
        # Check if the file is an MP4 video file
        if os.path.isfile(file_path) and file.lower().endswith(video_extension):
            # Get the movie name without the extension
            video_name = os.path.splitext(file)[0]
            
            # Create a new folder for the movie
            movie_folder = os.path.join(main_folder, video_name)
            os.makedirs(movie_folder, exist_ok=True)
            
            # Move the video file to the new folder
            shutil.move(file_path, os.path.join(movie_folder, file))
            
            # Look for matching subtitle files
            for subtitle in os.listdir(main_folder):
                subtitle_path = os.path.join(main_folder, subtitle)
                if (os.path.isfile(subtitle_path) and 
                    any(subtitle.lower().endswith(ext) for ext in subtitle_extensions) and
                    os.path.splitext(subtitle)[0] == video_name):
                    # Move the subtitle file to the same folder as the movie
                    shutil.move(subtitle_path, os.path.join(movie_folder, subtitle))

    print("✅ Movies and subtitle files have been organized successfully!")

# Run the function
if __name__ == "__main__":
    organize_movies()