# optimizer
optimizer = dict(type='SGD', lr=0.00125, momentum=0.9, weight_decay=0.00001)
#optimizer = dict(type='SGD', lr=0.00050, momentum=0.9, weight_decay=0.00005)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[16, 22])
total_epochs = 24
