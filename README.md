# crddc2022
Crowdsensing-based Road Damage Detection Challenge 2022


# road damage detection challange 2022 IMSC submission

This repository contains source code and trained models for [Crowdsensing-based Road Damage Detection Challenge](https://crddc2022.sekilab.global/) that was held as part of 2022 IEEE Big Data conference.

The best model achieved mean F1-score of 0.649399

## Table of contents

- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [RDCC Dataset Setup for YOLOv5](#RDCC-Dataset-Setup-for-YOLOv5)
- [IMSC YOLOv5 Model zoo](#IMSC-YOLOv5-Model-zoo)
- [Reproduce results for CRDDC2022 Competetion](#Reproduce-results-for-CRDDC2022-Competetion)
- [Detection](#Detection)

## Prerequisites

You need to install:
- [Python3 == 3.10](https://www.python.org/downloads/)

    ```Shell
    If using conda, use following command to create new conda virtual env
    conda create -n crddc python=3.10
    ```
    
- Use `requirements.txt` to install required python dependencies

    ```Shell
    # Python == 3.10 is needed
    pip3 install -r requirements.txt
    ```
   

## Quick-start
1. Clone the road-damage-detection repo into $RDD: 

    ```Shell
    git clone https://github.com/USC-InfoLab/rddc2020.git
    cd rddc2020
    git checkout -b crddc2022
    ```

2. Install python packages:

    ```Shell
    pip3 install -r requirements.txt
    ```


## [RDCC](https://github.com/sekilab/RoadDamageDetector#dataset-for-global-road-damage-detection-challenge-2020) Dataset Setup for YOLOv5

**NOTE: Entire process (step 1-4 explained in this section) of downloading and preparing GRDDC 2022 dataset can be done by executing `yolov5/scripts/dataset_setup_for_yolov5.sh`**

```Shell
    bash yolov5/scripts/dataset_setup_for_yolov5.sh
```

OR
    
1. Go to `yolov5` directory
    ```Shell
    cd yolov5
    ```

2. execute `download_road2020.sh` to downlaod train and test dataset
    ```Shell
    bash scripts/download_road2022.sh
    ```

3. **Detection:** strcutre test datasets for inference using yolov5
    ```Shell
    bash scripts/prepare_test.sh
    ```

4. **Training:** Generate the label files for yolov5 using [scripts/xml2Yolo.py](https://github.com/USC-InfoLab/rddc2020/tree/master/yolov5/scripts/xml2Yolo.py)
    ```Shell
    python3 scripts/xml2yolo.py --class_file datasets/damage_classes.txt --input_file datasets/train.txt
    ```
    - Use `python3 scripts/xml2Yolo.py --help` for command line option details


## IMSC YOLOv5 Model zoo

1. Go to `yolov5` directory
    ```Shell
    cd yolov5
    ```

2. download YOLOv5 model zoo:
    ```Shell
    bash scripts/download_IMSC_grddc2022_weights.sh
    ```
   
## Reproduce results for CRDDC2022 Competetion

Please complete all previous sections ([Prerequisites](#prerequisites), [Quick start](#quick-start), [RDCC Dataset Setup for YOLOv5](#RDCC-Dataset-Setup), [IMSC YOLOv5 Model zoo](#IMSC-YOLOv5-Model-zoo)) before starting this section.

1. Go to `yolov5` directory
    ```Shell
    cd yolov5
    ```

2. To generate csv files required to submit results for 5 leaderboards, run following script:
   (NOTE: This script will generate files `leaderboard_<Country Name>.csv` at the head of this repo (under `rddc2020/`).)
  
``` 
bash run.sh
```
   
## Detection
1. Download weights as mentioned in [IMSC YOLOv5 Model zoo](#IMSC-YOLOv5-Model-zoo)

2. Go to `yolov5` directory
    ```Shell
    cd yolov5
    ```
3. Execute one of the follwoing commands to generate `results_*.csv`(competition format): (to generate images with drawn predictions, remove ` --nosave` from command)
    ```Shell
    # inference using model trained with yolov5 default anchor boxes
    python3 detect.py --weights weights/IMSC/yolov5_anchor_epoch90.pt --img 640 --source datasets/CRDD2022/RDD2022_all_countries/all_test_images/ --conf-thres 0.25 --iou-thres 0.999 --agnostic-nms --augment --save-csv --nosave
    
    # inference using model trained with learnt crddc2022 dataset anchor boxes
    python3 detect.py --weights weights/IMSC/crddc_anchor_epoch80.pt --img 640 --source datasets/CRDD2022/RDD2022_all_countries/all_test_images/ --conf-thres 0.2 --iou-thres 0.999 --agnostic-nms --augment --save-csv --nosave
    
    # inference using best country specific ensemble models 
    python3 detect.py --weights weights/IMSC/yolov5_anchor_epoch90.pt weights/IMSC/crddc_anchor_epoch80.pt weights/IMSC/Japan_epoch70.pt --img 640 --source datasets/CRDD2022/RDD2022_all_countries/Japan/test/images/ --conf-thres 0.3 --iou-thres 0.999 --agnostic-nms --augment --save-csv --nosave
    python3 detect.py --weights weights/IMSC/yolov5_anchor_epoch90.pt weights/IMSC/crddc_anchor_epoch80.pt weights/IMSC/India_epoch110.pt --img 640 --source datasets/CRDD2022/RDD2022_all_countries/India/test/images/ --conf-thres 0.2 --iou-thres 0.999 --agnostic-nms --augment --save-csv --nosave
    python3 detect.py --weights weights/IMSC/yolov5_anchor_epoch90.pt weights/IMSC/crddc_anchor_epoch80.pt weights/IMSC/Czech_epoch70.pt --img 640 --source datasets/CRDD2022/RDD2022_all_countries/Czech/test/images/ --conf-thres 0.2 --iou-thres 0.999 --agnostic-nms --augment --save-csv --nosave
    python3 detect.py --weights weights/IMSC/yolov5_anchor_epoch90.pt weights/IMSC/crddc_anchor_epoch80.pt weights/IMSC/United_epoch90.pt --img 640 --source datasets/CRDD2022/RDD2022_all_countries/United_States/test/images/ --conf-thres 0.3 --iou-thres 0.999 --agnostic-nms --augment --save-csv --nosave
    python3 detect.py --weights weights/IMSC/yolov5_anchor_epoch90.pt weights/IMSC/crddc_anchor_epoch80.pt weights/IMSC/Norway_epoch100.pt --img 640 --source datasets/CRDD2022/RDD2022_all_countries/Norway/test/images/ --conf-thres 0.25 --iou-thres 0.999 --agnostic-nms --augment --save-csv --nosave
    python3 detect.py --weights weights/IMSC/yolov5_anchor_epoch90.pt weights/IMSC/crddc_anchor_epoch80.pt weights/IMSC/China_epoch120.pt --img 640 --source datasets/CRDD2022/RDD2022_all_countries/China_MotorBike/test/images/ --conf-thres 0.2 --iou-thres 0.999 --agnostic-nms --augment --save-csv --nosave 
    ```

visit [yolov5](https://github.com/ultralytics/yolov5) official source code for more training and inference time arguments







