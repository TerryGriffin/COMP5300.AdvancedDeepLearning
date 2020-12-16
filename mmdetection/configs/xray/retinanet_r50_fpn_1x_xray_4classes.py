_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    './xray_detection_4classes.py',
    './schedule_1x.py', './default_runtime_xray_4classes.py'
]
# optimizer
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.001)
