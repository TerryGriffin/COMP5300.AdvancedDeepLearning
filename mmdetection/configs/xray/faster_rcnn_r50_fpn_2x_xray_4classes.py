_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    './xray_dataset_instance_bbox_4classes.py',
    './schedule_2x.py', './default_runtime_xray_4classes.py'
]
