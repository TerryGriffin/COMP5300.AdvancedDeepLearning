_base_ = 'ssd300_tbx11k.py'
input_size = 512
model = dict(
    backbone=dict(input_size=input_size),
    bbox_head=dict(
        in_channels=(512, 1024, 512, 256, 256, 256, 256),
        anchor_generator=dict(
            type='SSDAnchorGenerator',
            scale_major=False,
            input_size=input_size,
            basesize_ratio_range=(0.1, 0.9),
            strides=[8, 16, 32, 64, 128, 256, 512],
            ratios=[[2], [2, 3], [2, 3], [2, 3], [2, 3], [2], [2]])))
# dataset settings
dataset_type = 'CocoDataset'
#data_root = 'data/coco/'
data_root = 'data/xray/UMLPeru/'
img_root = '/home/dataset/tbproject_xrayimage'

img_norm_cfg = dict(mean=[123.675, 116.28, 103.53], std=[1, 1, 1], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile', to_float32=True),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='PhotoMetricDistortion',
        brightness_delta=32,
        contrast_range=(0.5, 1.5),
        saturation_range=(0.5, 1.5),
        hue_delta=18),
    dict(
        type='Expand',
        mean=img_norm_cfg['mean'],
        to_rgb=img_norm_cfg['to_rgb'],
        ratio_range=(1, 4)),
    dict(
        type='MinIoURandomCrop',
        min_ious=(0.1, 0.3, 0.5, 0.7, 0.9),
        min_crop_size=0.3),
    dict(type='Resize', img_scale=(512, 512), keep_ratio=False),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
val_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(512, 512),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=False),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(512, 512),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=False),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
classes = ('ActiveTuberculosis', 'ObsoletePulmonaryTuberculosis', 'PulmonaryTuberculosis')
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=3,
    train=dict(
        _delete_=True,
        type='RepeatDataset',
        times=5,
        dataset=dict(
        classes=classes,
        type='CocoDataset',
        ann_file='data/xray/UMLPeru/annotations/TBX11K_train_only_tb.json',
        img_prefix='/home/dataset/tbproject_xrayimage',
        pipeline=train_pipeline)
    ),
    val=dict(
        classes=classes,
        type='CocoDataset',
        ann_file='data/xray/UMLPeru/annotations/TBX11K_val_only_tb.json',
        img_prefix='/home/dataset/tbproject_xrayimage',
        pipeline=val_pipeline
        ),
    test=dict(
        classes=classes,
        type='CocoDataset',
        ann_file='data/xray/UMLPeru/annotations/TBX11K_val_only_tb.json',
        img_prefix='/home/dataset/tbproject_xrayimage',
        pipeline=test_pipeline
        ))
# optimizer
optimizer = dict(type='SGD', lr=2e-4, momentum=0.9, weight_decay=5e-3)
optimizer_config = dict(_delete_=True)
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
work_dir = '/data2/mmdetection_output/TBX11K_0031'
gpu_ids = range(0, 1)
