import json
import sys
import os


def main(filename):
    with open(filename, "r") as in_file:
        data = json.load(in_file)

    image_ids = {image['id'] for image in data['images']}
    data['annotations'] = [a for a in data['annotations'] if a['image_id'] in image_ids]

    with open(filename, 'w') as out_file:
        json.dump(data, out_file)


if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(f"processing {f}")
        main(f)
