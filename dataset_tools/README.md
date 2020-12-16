The scripts in this directory are used for working with
the dataset json files.

add_mask_from_bbox.py - adds mask annotation that are duplicates of the bounding 
    box annotations. This is required for some configurations, otherwise an error 
    is raised.
    
chestx_det10_to_COCO.py - Converts the ChestX-Det10 annotations to COCO format.

coco_extract_image_files.py - Creates a list of image files from COCO annotation format file.

count_classes.py - Gives the class list and number of instances of each class from a
    COCO annotation file.
    
filter_anno_to_images.py - Removes annotations that do not match an image included in the 
    COCO annotation file. Some models fail if such annotations exist.
    
renumber_categories.py - Renumbers the categories starting at 0. This fills any holes
    in the numbering of categories, which causes problems for some models.
    
single_split_coco_json.py - Splits a COCO annotation file into train, val, and test splits.

use_single_category.py - Converts a COCO annotation file to on using a single 'Abnormal' class. This
    is used for class-agnostic testing.
    
