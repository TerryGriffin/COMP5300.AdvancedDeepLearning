_base_ = './mask_rcnn_r50_fpn_2x_xray_ac.py'
model = dict(pretrained='torchvision://resnet101', backbone=dict(depth=101))
