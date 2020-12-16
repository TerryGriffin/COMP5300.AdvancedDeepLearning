#!/usr/bin/env python
import random
import json
import sys
import os

def count_classes(filename):
    file_prefix = os.path.splitext(filename)[0]
    cat_by_index = dict()
    cat_count = dict()
    cat_instances = dict()
    cat_images = dict()
    all_image_ids = set()
    cat_image_ids = set()
    with open(filename,"r") as in_file:
        data = json.load(in_file)
    for i in data['images']:
        all_image_ids.add(i['id'])
    for cat in data['categories']:
        cat_by_index[cat['id']] = cat['name']
        cat_instances[cat['id']] = []
    print("num categories: ",len(data['categories']))
    for a in data['annotations']:
        if a['image_id'] not in all_image_ids:
            # skip annotations for images not in this set
            continue
        add_count(cat_count,cat_by_index[a['category_id']])
        cat_instances[a['category_id']].append(a)
        cat_image_ids.add(a['image_id'])
    print("cat_count: ",cat_count)
    sorted_cats = sorted(cat_count,key=cat_count.__getitem__)
    print("sorted_cats: ",sorted_cats)
    for cat in reversed(sorted_cats):
        print(cat," ",cat_count[cat])
    print("Num images: ",len(data['images']))
    print("Num annotations: ",len(data['annotations']))
    print("Num normal images: ", len(all_image_ids - cat_image_ids))


def add_count(dict, item):
    dict[item] = dict.get(item,0) + 1



if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Usage: count_classes <input file>")
    else:
        count_classes(sys.argv[1])

