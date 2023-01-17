import json

# You should have saved all the annotations you get in a json file in the same directory as this file

annotatedData = open('annotations.json')
annotations = json.load(annotatedData)

# The first thing to do is to save the resized image URL as an image -> annotations[0]['resizedImageUri'] {save this}

# Go to the Ultralytics GitHub repository and clone the repository and install all the requirements
# You can do it using this
# git clone https://github.com/ultralytics/yolov5
# cd yolov5
# pip install -r requirements.txt
# This is only to understand the structure of the directories to be created.

# Manipulation and converting to yolo format

import requests
from PIL import Image
from io import BytesIO
from tqdm.auto import tqdm

for j in tqdm(range(0, len(annotations))):
    r = requests.get(annotations[j]['resizedImageUri'])
    i = Image.open(BytesIO(r.content))
    i.save(f"images/{annotations[j]['id']}.jpg")
    
# We are interested in {annotations[i]['regions']} for the regions

# Yolo conversion formula
# We have left, top, width and height
# Left, Top, Width, Height => Xc, Yc, W, H

# Xc = Left + W/2
# Yc = Top + H/2
# W = Width
# H = Height

def azure2yolo(x, y, w, h):
    return x + w / 2, y + h / 2, w, h
  
map = {
    'Fire': 0,
    'Smoke': 1
}

# Expected Output
# [tagnum,xcent, ycent, w, h]
# [tagnum,xcent, ycent, w, h]

for i in tqdm(range(len(annotations))):
    id = annotations[i]['id'] # Save file with this name
    f = open(f'labels/{id}.txt', 'w')
    for detection in annotations[i]['regions']:
        tagNum = map[detection['tagName']]
        x = detection['left']
        y = detection['top']
        w = detection['width']
        h = detection['height']
        xc, yc, w, h = azure2yolo(x, y, w, h)
        f.write(f"{tagNum} {xc} {yc} {w} {h}\n")
    f.close()
    
 # After this we will get the folders and files as per requirements.
