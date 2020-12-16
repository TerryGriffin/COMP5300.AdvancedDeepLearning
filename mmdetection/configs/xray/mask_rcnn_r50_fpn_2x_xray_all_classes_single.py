_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    './xray_dataset_instance_all_classes_single.py',
    './schedule_2x.py', './default_runtime_xray_all_classes_single.py'
]
