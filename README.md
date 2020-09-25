# rddc2020
road damage detection challenge 2020


# road damage detection challange 2020 IMSC submission

This repository contains source code and trained models for [Road Damage Detection and Classification Challenge](https://rdd2020.sekilab.global/overview/) that was held as part of 2020 IEEE Big Data conference.

The best model achieved mean F1-score of 0.664291771220962 on test1 and 0.650065074526981 on test2 dataset of the competition.

Sample predictions:

![](examples/sample1.jpg=250x250) ![](examples/sample2.jpg=250x250) ![](examples/sample3.jpg=250x250) ![](examples/sample4.jpg=250x250)

## Table of contents

- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [RDCC Dataset Setup for YOLOv5](#RDCC-Dataset-Setup)
- [IMSC YOLOv5 Model zoo](#IMSC-YOLOv5-Model-zoo)
- [Detection / Submission](#Detection)
- [Performance on RDDC test datasets](#Performance-on-RDDC-test-datasets)
- [Training](#Training)

## Prerequisites

You need to install:
- [Python3 >= 3.6](https://www.python.org/downloads/)
- Use `requirements.txt` to install required python dependencies

    ```Shell
    # Python >= 3.6 is needed
    pip3 install -r requirements.txt
    ```
   

## Quick-start
1. Clone the road-damage-detection repo into $RDD: 

    ```Shell
    git clone https://github.com/USC-InfoLab/rddc2020.git
    ```

2. Install python packages:

    ```Shell
    pip3 install -r requirements.txt
    ```


## [RDCC](https://github.com/sekilab/RoadDamageDetector#dataset-for-global-road-damage-detection-challenge-2020) Dataset Setup for YOLOv5

**NOTE: Entire process (step 1-4 explained in this section) of downloading and preparing GRDDC 2020 dataset can be done by executing `yolov5/scripts/dataset_setup_for_yolov5.sh`**

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
    bash scripts/download_road2020.sh
    ```

3. **Detection:** strcutre test datasets for inference using yolov5
    ```Shell
    bash scripts/prepare_test.sh
    ```

4. **Training:** Generate the label files for yolov5 using [scripts/xml2Yolo.py](https://github.com/USC-InfoLab/rddc2020/tree/master/yolov5/scripts/xml2Yolo.py)
    ```Shell
    python3 scripts/xml2yolo.py
    ```
    - Use `python3 scripts/xml2Yolo.py --help` for command line option details


## IMSC YOLOv5 Model zoo

1. Go to `yolov5` directory
    ```Shell
    cd yolov5
    ```

2. download YOLOv5 model zoo:
    ```Shell
    bash scripts/download_IMSC_grddc2020_weights.sh
    ```
   
## Detection / Submission
1. Download weights as mentioned in [IMSC YOLOv5 Model zoo](#IMSC-YOLOv5-Model-zoo)

2. Go to `yolov5` directory
    ```Shell
    cd yolov5
    ```
3. Execute one of the follwoing commands to generate `results.csv`(competition format) and predicated images under `inference/output/`:
    ```Shell
    # inference using best ensemble model for test1 dataset
    python3 detect.py --weights weights/IMSC/last_95_448_32_aug2.pt weights/IMSC/last_95_640_16.pt weights/IMSC/last_120_640_32_aug2.pt --img 640 --source datasets/road2020/test1/test_images/ --conf-thres 0.22 --iou-thres 0.9999 --agnostic-nms --augment
    ```

    ```Shell
    # inference using best ensemble model for test2 dataset
    python3 detect.py --weights weights/IMSC/last_95_448_32_aug2.pt  weights/IMSC/last_95_640_16.pt  weights/IMSC/last_120_640_32_aug2.pt weights/IMSC/last_100_100_640_16.pt --img 640 --source datasets/road2020/test2/test_images/ --conf-thres 0.22 --iou-thres 0.9999 --agnostic-nms --augment
    ```

    ```Shell
    # inference using best non-ensemble model for test1 dataset
    python3 detect.py --weights weights/IMSC/last_95.pt --img 640 --source datasets/road2020/test1/test_images/ --conf-thres 0.20 --iou-thres 0.9999  --agnostic-nms --augment
    ```

    ```Shell
    # inference using best non-ensemble model for test2 dataset
    python3 detect.py --weights weights/IMSC/last_95.pt --img 640 --source datasets/road2020/test2/test_images/ --conf-thres 0.20 --iou-thres 0.9999  --agnostic-nms --augment
    ```

## Performance on RDDC test datasets

| YOLOv5x_448_32_aug2 | YOLOv5x_640_16_95 | YOLOv5x_640_16_100 | YOLOv5x_640_32     | YOLOv5x_640_16_aug2 | YOLOv5x_640_32_aug2 | test1 F1-score | test2 F1-score |
|------- |------------------- |------------------- |------------------- |------------------- |------------------- |------------------- |------------------- |
|                    | :heavy_check_mark: |                    |                    |                    |                    | 0.66697383879131 |0.651389430313506                 |
| :heavy_check_mark: | :heavy_check_mark: |                    |                    |                    | :heavy_check_mark: |**0.674878682854973**                  | 0.665632401648316                   |
| :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    | :heavy_check_mark: |0.674198239966431                 |  **0.666213894130645**                 |


## Training
1. download pre-trained weights from yolov5 repo
    ```Shell
    bash weights/download_weights.sh
    ```
    
2. run following command
    ```Shell
    python3 train.py --data data/road.yaml --cfg models/yolov5x.yaml --weights weight/yolov5x.pt --batch-size 64
    ```
visit [yolov5](https://github.com/ultralytics/yolov5) official source code for more training and inference time arguments







