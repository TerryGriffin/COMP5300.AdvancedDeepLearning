import random
import json
import sys
import os

def coco_extract_image_files(filename, output_filename):

    with open(filename,"r") as in_file:
        data = json.load(in_file)
        
    with open(output_filename, 'w') as outfile:
        for image in data['images']:
            outfile.write(image['file_name']+"\n")


if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print("Usage: coco_extract_image_files <input file> <output file>")
    else:
        coco_extract_image_files(sys.argv[1], sys.argv[2])

