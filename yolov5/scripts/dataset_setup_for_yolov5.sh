cd yolov5
bash scripts/download_road2022.sh
bash scripts/prepare_test.sh
python3 scripts/xml2yolo.py
