import json
import sys
import os


def main(input_filename, output_filename):
    with open(input_filename, "r") as in_file:
        data = json.load(in_file)

    data["categories"] =[
        {
            "id": 0,
            "name": "Abnormal",
            "supercategory": "all"
        }
    ]

    for anno in data["annotations"]:
        anno["category_id"] = 0

    with open(output_filename, 'w') as out_file:
        json.dump(data, out_file)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
