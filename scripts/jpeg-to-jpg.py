import os
import sys

# Check if a directory argument has been provided
if len(sys.argv) != 2:
    print("Usage: python rename_jpeg_to_jpg.py <directory>")
    sys.exit(1)

# The directory containing the .jpeg files
directory = sys.argv[1]

# Loop over each file in the directory
for filename in os.listdir(directory):
    # Check if the file has a .jpeg extension
    if filename.endswith(".jpeg"):
        # Construct the full file path
        old_file = os.path.join(directory, filename)
        # Replace the file extension
        new_file = os.path.join(directory, filename[:-5] + ".jpg")
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed {old_file} to {new_file}")

