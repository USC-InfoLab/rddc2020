import zipfile
fname = "RDD2022.zip"

with zipfile.ZipFile(fname, "r") as zip_ref:
    zip_ref.extractall("CRDD2022")

fname_list = ["CRDD2022/RDD2022_all_countries/Japan.zip",
        "CRDD2022/RDD2022_all_countries/India.zip",
        "CRDD2022/RDD2022_all_countries/Czech.zip",
        "CRDD2022/RDD2022_all_countries/Norway.zip",
        "CRDD2022/RDD2022_all_countries/China_MotorBike.zip",
        "CRDD2022/RDD2022_all_countries/China_Drone.zip",
        "CRDD2022/RDD2022_all_countries/United_States.zip"]

for fname in fname_list:
    with zipfile.ZipFile(fname, "r") as zip_ref:
        zip_ref.extractall("CRDD2022/RDD2022_all_countries/")
