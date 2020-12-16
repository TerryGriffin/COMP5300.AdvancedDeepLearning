_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    './xray_detection_pe.py',
    './schedule_1x.py', './default_runtime_xray_pe.py'
]
# optimizer
optimizer = dict(type='SGD', lr=0.00125, momentum=0.9, weight_decay=0.0001)
