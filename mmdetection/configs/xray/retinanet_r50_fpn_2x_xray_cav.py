_base_ = './retinanet_r50_fpn_1x_xray_cav.py'
# learning policy
lr_config = dict(step=[16, 22])
total_epochs = 24
