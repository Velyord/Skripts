import os
from natsort import natsorted

def rename_images(folder_path, start_number=816):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))] # Get a list of image files in the folder
    files = natsorted(files) # sort them naturally

    for i, filename in enumerate(files, start=start_number):
        file_ext = os.path.splitext(filename)[1] # Extract the file extension
        new_name = f"{i:04}{file_ext}" # Format new filename as 4-digit numbers starting from 'start_number'
        
        # Construct the full file paths
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        
        os.rename(src, dst) # Rename the file
        print(f"Renamed '{filename}' to '{new_name}'")

folder_path = "C:/Users/user/rename" # Replace with your folder path
rename_images(folder_path, start_number=323)
