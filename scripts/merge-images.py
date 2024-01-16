import os
import shutil

def merge_images_with_prefix(source_dir, target_dir):
    """
    Merges images from subdirectories into a single directory, prefixing file names with parent directory name.

    :param source_dir: Path to the source directory containing subdirectories.
    :param target_dir: Path to the target directory where merged images will be stored.
    """
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate over each subdirectory in the source directory
    for subdir in os.listdir(source_dir):
        subdir_path = os.path.join(source_dir, subdir)

        # Check if the path is a directory
        if os.path.isdir(subdir_path):
            # Iterate over each file in the subdirectory
            count = 0
            for file in os.listdir(subdir_path):
                count += 1
                if count > num:
                    break
                file_path = os.path.join(subdir_path, file)
                # Check if the path is a file and has a .jpg extension
                if os.path.isfile(file_path) and file.lower().endswith('.jpg'):
                    # Create a new file name with the prefix and copy the file
                    new_file_name = f"{subdir}_{file}"
                    new_file_path = os.path.join(target_dir, new_file_name)
                    shutil.copy(file_path, new_file_path)

# Example usage
source_directory = 'source'  # Path to the source directory
target_directory = 'target'  # Path to the target directory where merged images will be stored

num = 50
# Call the function to merge the images
merge_images_with_prefix(source_directory, target_directory)

