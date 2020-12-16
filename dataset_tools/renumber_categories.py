import json
import sys
import os


def main(filename):
    with open(filename, "r") as in_file:
        data = json.load(in_file)

    id_set = {category["id"] for category in data["categories"]}
    if len(id_set) == 0:
        return
    if len(id_set) == max(id_set)+1:
        return

    cat_map = {}
    for i, id in enumerate(list(id_set)):
        cat_map[id] = i

    for cat in data["categories"]:
        cat["id"] = cat_map[cat["id"]]

    for anno in data["annotations"]:
        anno["category_id"] = cat_map[anno["category_id"]]

    with open(filename, 'w') as out_file:
        json.dump(data, out_file)


if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(f"processing {f}")
        main(f)
