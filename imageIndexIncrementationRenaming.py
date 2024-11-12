import os
from natsort import natsorted

def rename_images(folder_path):
    # Get a list of image files in the folder and sort them naturally
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
    files = natsorted(files)

    for i, filename in enumerate(files):
        # Extract the file extension
        file_ext = os.path.splitext(filename)[1]
        # Format new filename as 4-digit numbers starting from 0000
        new_name = f"{i:04}{file_ext}"
        # Construct the full file paths
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(src, dst)
        print(f"Renamed '{filename}' to '{new_name}'")

# Usage example
folder_path = "/path/to/your/folder"  # Replace with your folder path
rename_images(folder_path)
