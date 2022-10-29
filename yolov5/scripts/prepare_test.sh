cd datasets/CRDD2022/RDD2022_all_countries/
echo "move test images to a flat directory structure required by yolo..."
mkdir all_test_images
cp -r Japan/test/images/* all_test_images/
cp -r United_States/test/images/* all_test_images/
cp -r India/test/images/* all_test_images/
cp -r Czech/test/images/* all_test_images/
cp -r China_MotorBike/test/images/* all_test_images/
cp -r Norway/test/images/* all_test_images/
cd -
