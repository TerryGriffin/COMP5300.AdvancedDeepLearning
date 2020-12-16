_base_ = './mask_rcnn_r50_fpn_2x_tbx11k_single.py'
model = dict(pretrained='torchvision://resnet101', backbone=dict(depth=101))
