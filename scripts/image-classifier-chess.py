import requests
import base64
from PIL import Image
import json
import sys
import os
import glob

def get_images(directory):
    """
    Returns a list of full paths of all .jpg files in the given directory.
    """
    # Change the current directory to the specified directory
    os.chdir(directory)

    # List to store the paths of .jpg files
    jpg_files = []

    # Use glob to find all .jpg files
    for file in glob.glob("*.jpg"):
        # Get the full path and add it to the list
        full_path = os.path.join(directory, file)
        jpg_files.append(full_path)

    return jpg_files


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def classify(image_path, base64_image, prompt):
    payload = {
        "model": "chess-classifier",
        "prompt": prompt,
        "images": [base64_image]
    }

    url = 'http://localhost:11434/api/generate'
    # Make the HTTP POST request with stream=True
    response = requests.post(url, json=payload, stream=False)

    # Check the response
    if response.status_code == 200:
        complete_response = ""
        try:
            for line in response.iter_lines():
                if line:  # Check if line is not empty
                    # Decode and parse each line as JSON
                    line_data = json.loads(line.decode('utf-8'))
                    # Extract the 'response' field and append it to the complete response
                    res = line_data.get("response", "")
                    complete_response += res
                    # Check if the 'done' field is True
                    if line_data.get("done", False):
                        break
            return(complete_response.strip().upper())
        except Exception as e:
            print("Error while processing streamed response:", e)
    else:
        print("Request failed, status code:", response.status_code)

if __name__ == "__main__":
    prompt = "What chess piece is this?"
    image_dir = os.getcwd() + '/' + sys.argv[1]
    print("#image_name, actual, predicted, score")
    for image_path in get_images(image_dir):
        base64_image = image_to_base64(image_path)
        image_base = image_path.split('/')[-1]
        actual = image_base.split('_')[0].strip().lower()
        predicted = classify(image_path, base64_image, prompt).strip().lower() or "Null"
        score = "pass" if actual == predicted else "fail"
        print(f"{image_base}, {actual}, {predicted}, {score}")


