_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn_single.py',
    './xray_dataset_instance_bbox_nih_single.py',
    './schedule_2x.py', './default_runtime_nih.py'
]
