# COMP5300.AdvancedDeepLearning Fall 2020

This repository contains the code associated with the final project for COMP.5300 Advanced Deep Learning,
Fall 2020.

This project compares the performance of several networks for object detection 
and instance segmentation on four datasets for chest x-rays (CXRs). The codde
for some utility scripts for training and testing are included. Most of the work
for this project was in testing the various configurations. The configuration scripts
for each network/dataset combination are included. 

The code depends on the Pytorch version 1.6.0 (https://pytorch.og). Three CNN architectures tested
for this project rely on three libraries:
* The latest version of MMDetection for Faster R-CNN, Mask R-CNN, RetinaNet, SSD, and YOLOv3 (https://github.com/open-mmlab/mmdetection).
* A forked (older) version of MMDetection supporting SOLOv2 at (https://github.com/WXinlong/SOLO).
* The AdelaiDet library for BlendMask (https://github.com/aim-uofa/AdelaiDet). This library uses the 
Detectron2 framework (https://github.com/facebookresearch/detectron2).

The file layout is:

root
    
* doc - the final report and presentation.
* dataset_tools - scripts for working with the datasets.
* mmdetection - code and config files for use with the MMDetection library.
* mmdetection_solo - code and config files for use with the SOLOv2 version of the
MMDetection library.
* adelaidet - config files for use with the AdelaiDet library.

The config files follow this format:

<network type>_<network size>_<data set>

The datasets are:
xray_ac - Only Airspace Consolidation for the UML/Peru dataset.
xray_cav - Only Cavitation for the UML/Peru dataset
xray_ly - Only Lymphadenopathy for the UML/Peru dataset
xray_pe - Only Pleural Effusioin for the UML/Peru dataset
xray_4classes - Airspace Consolidation, Cavitation, Lyphmadenopathy, and Pleural Effusion
for the UML/Peru dataset
xray_all_classes_single - All annotations for the UML/Peru dataset as a single class (Abnormal).

nih - The NIH ChestX-ray14 dataset
nih_single - The NIH ChestX-ray14 dataset with all annotations as a single class.

nih_chestx_det - The ChestX-Det10 dataset
nih_chestx_det_single - The ChestX-Det10 dataset with all annotations as a single class.

tbx11k - The TBX11K dataset
tbx11k_single -  The TBX11K dataset with all annotations as a single class.

The network types are:
faster_rcnn
mask_rcnn
fcos
retinanet
ssd
yolov3
solov2
blendmask

The config files in the mmdetection tree use an "include" structure, where larger
networks include the config file for smaller networks, and use common files for
dataset configuration. The config files under the mmdetection_solo and adelaidet 
tree use a single file for each configuration.


    