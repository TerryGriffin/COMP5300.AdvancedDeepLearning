_base_ = './retinanet_r50_fpn_1x_tbx11k_single.py'
# learning policy
lr_config = dict(step=[16, 22])
total_epochs = 24
