import sys
import os
import glob
import datetime
import json
from PIL import Image
import xml.etree.ElementTree as ET

def create_COCO_struct():
    info = {
        "year" : 2020,
        "version" : '1.0',
        "description" : 'ChestX-Det10 annotations converted to COCO format',
        "contributor" : 'UML',
         "url" : '',
        "date_created" : datetime.datetime.now().strftime("%Y/%m/%d")
    }

    no_license = {
        'id' : 1,
        'url' : '',
        'name' : 'no license'

    }
    return {
        'info' : info,
        'images' : [],
        'annotations' : [],
        'licenses' : [no_license],
        'categories' : []
    }

def create_id_struct():
    return {
        'filename_ids' : dict(),
        'category_ids' : dict()
    }

def add_image(coco_struct, ids, fname, width, height):
    filenames = ids.get('filename_ids')
    if not fname in filenames:
        id = len(filenames) + 1
        filenames[fname] = id
        image = {
            "id" : id,
            "width" : width,
            "height": height,
            "file_name" : fname,
            "license" : 1,
            "flickr_url" : "",
            "coco_url" : "",
            "date_captured" : "2010/10/12",
        }
        coco_struct['images'].append(image)
    else:
        id = filenames[fname]
    return id

def add_category(coco_struct, ids, name):
    categories = ids.get('category_ids')
    if not name in categories:
        id = len(categories) + 1
        categories[name] = id
        category = {
           "id" : id,
           "name" : name,
           "supercategory" : "all"
        }
        coco_struct['categories'].append(category)
    else:
        id = categories[name]
    return id

def add_annotation(coco_struct, ids, id, image_id, cat_id, polygon, area, bbox, confidence):
    annotation = {
        "id" : id,
        "image_id" : image_id,
        "category_id" : cat_id,
        "segmentation" : [polygon],
        "area" : area,
        "bbox" : bbox,
        "iscrowd" : 0,
        "confidence" : confidence
    }
    coco_struct['annotations'].append(annotation)


def get_image_size(image_path):
    im=Image.open(image_path)
    return im.width, im.height


def chestx_det10_to_COCO(input_fname, image_directory, output_fname):
    coco_data = create_COCO_struct()
    ids = create_id_struct()
    annotation_id = 1
    file_count = 0

    with open(input_fname,"r") as f:
        data = json.load(f)

    for entry in data:
        try:
            file_count = file_count + 1
            filename = entry['file_name']
            full_path = os.path.join(image_directory, filename)
            width, height = get_image_size(full_path)
            image_id = add_image(coco_data, ids, filename, width, height)
            for cat_name, bbox in zip(entry["syms"], entry["boxes"]):
                cat_id = add_category(coco_data, ids, cat_name)
                x, y, w, h = bbox
                area = w * h
                points = []
                points.extend([x ,y])
                points.extend([x+w, y])
                points.extend([x+w, y + h])
                points.extend([x, y + h])
                confidence = "High"
                add_annotation(coco_data, ids, annotation_id, image_id, cat_id, points, area, bbox, confidence)
                annotation_id = annotation_id+1
        except Exception as e:
            print("Error processing ",full_path," ",sys.exc_info()[0], e)

    with open(output_fname, 'w') as outfile:
        json.dump(coco_data, outfile)


def add_count(dict, item):
    dict[item] = dict.get(item,0) + 1




if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print("Usage: chestx_det10_to_COCO <input file> <image dir> <output file>")
    else:
        chestx_det10_to_COCO(sys.argv[1], sys.argv[2], sys.argv[3])

