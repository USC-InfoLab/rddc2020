cd yolov5
bash scripts/download_road2020.sh
bash scripts/prepare_test.sh
python3 scripts/xml2yolo.py
