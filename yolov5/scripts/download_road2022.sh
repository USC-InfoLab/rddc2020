cd datasets/
echo "downloading train dataset..."
wget https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/RDD2022.zip
python3 extract_road2022.py
cd -
