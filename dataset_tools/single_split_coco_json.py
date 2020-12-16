import random
import json
import sys
import os


def split_coco_json(pos_filename, percent_for_validation):
    file_prefix = os.path.splitext(pos_filename)[0]
    
    # category names by id
    cat_by_id = dict()
    
    # count of instances by category id
    cat_count = dict()
    
    # lists of instances by category id
    cat_instances = dict()
    
    # set of image ids that have not yet been added to either
    # the training or validation set
    image_ids = set()
    
    # set of images for the training set
    train_images = set()
    
    # set of images for the validation set
    val_images = set()

    # set of images for the test set
    test_images = set()
    
    with open(pos_filename, "r") as in_file:
        pos_data = json.load(in_file)

    # for each category, create the id:name map, initialize the instance list
    for cat in pos_data['categories']:
        cat_by_id[cat['id']] = cat['name']
        cat_instances[cat['name']] = []
        
    print("num categories: ",len(pos_data['categories']))
    
    # count number of instances by category id. populate list of instances
    # of annotations by category id
    for a in pos_data['annotations']:
        add_count(cat_count,cat_by_id[a['category_id']])
        cat_instances[cat_by_id[a['category_id']]].append(a)
        image_ids.add(a['image_id'])
        
    print("cat_count: ",cat_count)
    sorted_cats = sorted(cat_count,key=cat_count.__getitem__)
    print("sorted_cats: ",sorted_cats)
    
    # go through each category in increasing order of instances.
    for cat in sorted_cats:
        # split is the number of instances in the validation set
        split = cat_count[cat] * percent_for_validation
        # val_image_count is the number of annotations already selected for the 
        # validation set
        val_image_count = 0
        test_image_count = 0
        for a in cat_instances[cat]:
            # get the image_id for this annotation
            image_id = a['image_id']
            
            if image_id in image_ids:
                # image has not been added yet
    
                # add the image to either the validation or training set
                if val_image_count < split:
                    val_images.add(image_id)
                    val_image_count += 1
                elif test_image_count < split:
                    test_images.add(image_id)
                    test_image_count += 1
                else:
                    train_images.add(image_id)
                    
                # remove the image from the available set
                image_ids.remove(image_id)
            elif image_id in val_images:
                # image is already in the validation set
                val_image_count += 1
            elif image_id in test_images:
                test_image_count += 1

    print("len(val_images): ",len(val_images))
    print("len(test_images): ",len(test_images))
    print("len(train_images): ",len(train_images))

    train_out = dict()
    val_out = dict()
    test_out = dict()

    # copy all the items except the images from
    # the original data into both the training and validation
    # sets
    for k,v in pos_data.items():
        if k != 'images':
            train_out[k] = v
            val_out[k] = v
            test_out[k] = v
        else:
            train_out[k] = []
            val_out[k] = []
            test_out[k] = []

    # for each image in the original dataset, copy it to either
    # the validation, test, or training set.
    for image in pos_data['images']:
        if image['id'] in val_images:
            val_out['images'].append(image)
        elif image['id'] in test_images:
            test_out['images'].append(image)
        elif image['id'] in train_images:
            train_out['images'].append(image)

    train_filename = file_prefix + '_train' + '.json'
    val_filename  = file_prefix + '_val' + '.json'
    test_filename = file_prefix + '_test' + '.json'
    with open(train_filename, 'w') as outfile:
        print("writing ",train_filename, " images ",len(train_out['images']))
        json.dump(train_out, outfile)
    with open(val_filename, 'w') as outfile:
        print("writing ",val_filename, " images ",len(val_out['images']))
        json.dump(val_out, outfile)
    with open(test_filename, 'w') as outfile:
        print("writing ",test_filename, " images ",len(test_out['images']))
        json.dump(test_out, outfile)

def add_count(dict, item):
    dict[item] = dict.get(item,0) + 1

if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print("Usage: single_split_coco_json <positive input file> <percent for validation>")
    else:
        split_coco_json(sys.argv[1], int(sys.argv[2])/100.0)

