import os
import errno

for test in ["test1", "test2"]:
    new_path = os.path.join(test, 'test_images')
    try:
        os.makedirs(new_path)
    except OSError as e:
        print("warning! {} already exists".format(new_path))
        if e.errno != errno.EEXIST:
            raise

    countries = os.listdir(test)
    for country in countries:
        if country not in ['Japan', 'India', 'Czech']:
            continue
        images_path = os.path.join(test, country, 'images')
        image_list = os.listdir(images_path)
        for img in image_list:
            full_image_path = os.path.join(images_path, img)
            cmd = 'mv ' + full_image_path + ' ' + new_path
            print(cmd)
            os.system(cmd)
