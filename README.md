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
- [RDCC Dataset Setup](#RDCC-Dataset-Setup)
- [Detection / Submission](#Detection)
- [Training](#Training)
- [Citation](#Citation)

## Prerequisites

You need to install:
- [Python3](https://www.python.org/downloads/)
- Use `yolov5/requirements.txt` to install required python dependencies

    ```Shell
    # Python 3 is needed
    pip3 install -r yolov5/requirements.txt
    ```
   

## Quick-start
1. Clone the road-damage-detection repo into $RDD: 

    ```Shell
    git clone https://github.com/dweeptrivedi/road-damage-detection.git
    ```

2. Install python packages:

    ```Shell
    pip3 install -r yolov5/requirements.txt
    ```


## RDCC Dataset Setup

1. download dataset from [RDDC](https://github.com/sekilab/RoadDamageDetector#dataset-for-global-road-damage-detection-challenge-2020) website

2. Generate the label files for Darknet using [yolov5/scripts/xml2Yolo.py](https://github.com/USC-InfoLab/rddc2020/tree/master/yolov5/scripts/xml2Yolo.py)
    - Use `python3 xml2Yolo.py --help` for command line option details

IGNORE THIS: NOTE: It is expected that the Dataset be structured in PASCAL VOC format (images under JPEGImages, XML files under Annotations directory)


## Detection

