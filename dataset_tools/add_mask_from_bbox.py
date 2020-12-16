import json
import sys
import os


def main(filename):
    with open(filename, "r") as in_file:
        data = json.load(in_file)

    for anno in data['annotations']:
        x, y, w, h = anno['bbox']
        mask = [ [ x, y, x+w, y, x+w, y+h]]
        anno['segmentation'] = mask

    with open(filename, 'w') as out_file:
        json.dump(data, out_file)

if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(f"processing {f}")
        main(f)
