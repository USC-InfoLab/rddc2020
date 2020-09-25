# rddc2020
road damage detection challenge 2020


# road damage detection challange 2020 IMSC submission

This repository contains source code and trained models for [Road Damage Detection and Classification Challenge](https://rdd2020.sekilab.global/overview/) that was held as one of the 2020 IEEE Big Data.

The best model achieved mean F1-score of 0.664291771220962 on test1 and 0.650065074526981 on test2 dataset of the competition.

Sample predictions:

![](examples/sample1.png) ![](examples/sample2.png) ![](examples/sample3.png) ![](examples/sample4.png)

## Table of contents

- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [RDCC Dataset Setup for YOLOv5](#RDCC-Dataset-Setup)
- [YOLOv5 Model zoo](#YOLOv5-Model-zoo)
- [Detection / Submission](#Detection)
- [Training](#Training)
- [Citation](#Citation)

## Prerequisites

You need to install:
- [Python3 >= 3.6](https://www.python.org/downloads/)
- Use `yolov5/requirements.txt` to install required python dependencies

    ```Shell
    # Python 3 is needed
    cd yolov5
    pip3 install -r requirements.txt
    ```
   

## Quick-start
1. Clone the road-damage-detection repo into $RDD: 

    ```Shell
    git clone https://github.com/dweeptrivedi/road-damage-detection.git
    ```

2. Install python packages:

    ```Shell
    pip3 install -r requirements.txt
    ```


## [RDCC](https://github.com/sekilab/RoadDamageDetector#dataset-for-global-road-damage-detection-challenge-2020) Dataset Setup for YOLOv5
1. Go to `yolov5` directory
    ```Shell
    cd yolov5
    ```

2. execute `download_road2020.sh` to downlaod train and test dataset
    - Linux (wget command)
    ```Shell
    bash scripts/download_road2020_wget.sh
    
    ```
    - Mac OS (curl command)
    ```Shell
    bash scripts/download_road2020_curl.sh
    ```

3. **Detection:** strcutre test datasets for inference using yolov5
    ```Shell
    bash scripts/prepare_test.sh
    ```

4. **Training:** Generate the label files for Darknet using [yolov5/scripts/xml2Yolo.py](https://github.com/USC-InfoLab/rddc2020/tree/master/yolov5/scripts/xml2Yolo.py)
    ```Shell
    bash scripts/xml2yolo.sh
    ```
    - Use `python3 scripts/xml2Yolo.py --help` for command line option details


Entire process of downloading and preparing GRDDC 2020 dataset can be done by executing `scripts/dataset_setup_for_yolov5.sh`
    ```Shell
    bash scripts/dataset_setup_for_yolov5.sh
    ```


## YOLOv5 Model zoo

1. Go to `yolov5` directory
    ```Shell
    cd yolov5
    ```

2. download YOLOv5v5 model zoo:
    ```Shell
    bash scripts/download_grddc2020_weights_wget.sh
    ```
   
## Detection / Submission

1. Go to `yolov5` directory
    ```Shell
    cd yolov5
    ```
2. Execute follwoing command to generate `results.csv` and predicated images under `inference/images`:
```Shell
# inference using best ensemble model for test1 dataset
python3 detect.py --weights weights/last_95_448_32_aug2.pt weights/last_95_640_16.pt weights/last_120_640_32_aug2.pt --img 640 --source datasets/road2020/test1/test_images/ --conf-thres 0.22 --iou-thres 0.9999 --agnostic-nms --augment
```

```Shell
# inference using best ensemble model for test2 dataset
python3 detect.py --weights weights/last_95_448_32_aug2.pt  weights/last_95_640_16.pt  weights/last_120_640_32_aug2.pt weights/last_100_100_640_16.pt --img 640 --source datasets/road2020/test2/test_images/ --conf-thres 0.22 --iou-thres 0.9999 --agnostic-nms --augment
```

```Shell
# inference using best non-ensemble model for test1 dataset
python3 detect.py --weights weights/last_95.pt --img 640 --source datasets/road2020/test1/test_images/ --conf-thres 0.20 --iou-thres 0.9999  --agnostic-nms --augment
```

```Shell
# inference using best non-ensemble model for test2 dataset
python3 detect.py --weights weights/last_95.pt --img 640 --source datasets/road2020/test2/test_images/ --conf-thres 0.20 --iou-thres 0.9999  --agnostic-nms --augment
```

## Performance on RDDC test datasets

| YOLOv5x_448_32_aug2 | YOLOv5x_640_16_95 | YOLOv5x_640_16_100 | YOLOv5x_640_32     | YOLOv5x_640_16_aug2 | YOLOv5x_640_32_aug2 | test1 F1-score | test2 F1-score |
|------------------- |------------------- |------------------- |------------------- |------------------- |------------------- |------------------- |------------------- |
|                    | :heavy_check_mark: |                    |                    |                    |                    |                    |                    |
| :heavy_check_mark: | :heavy_check_mark: |                    |                    |                    | :heavy_check_mark: |                    |                    |
| :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    | :heavy_check_mark: |                    |                    |

## Training







