_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    './xray_dataset_instance_bbox_nih_chestx_det.py',
    './schedule_2x.py', './default_runtime_nih_chestx_det.py'
]
