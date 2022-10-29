import argparse
import math
import os
import sys
import xml.etree.ElementTree as ET
from PIL import Image
from collections import defaultdict
from random import shuffle


#Type of image in Dataset
imageType = ["jpg","png","jpeg","JPEG","JPG","PNG"]
#dictionary to store list of image paths in each class
imageListDict = defaultdict(set)

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return [x,y,w,h]

#convert minX,minY,maxX,maxY to normalized numbers required by Yolo
def getYoloNumbers(imagePath, minX,minY,maxX, maxY):
    image=Image.open(imagePath)
    w= int(image.size[0])
    h= int(image.size[1])
    b = (minX,maxX, minY, maxY)
    bb = convert((w,h), b)
    image.close()
    return bb

def getFileList3(filePath):
    xmlFiles = []
    with open(filePath,"r") as f:
        xmlFiles = f.readlines()
        for i in range(len(xmlFiles)):
            temp = xmlFiles[i].strip().rsplit('.',1)[0]
            xmlFiles[i] = os.path.abspath(temp.replace("images","annotations/xmls")+".xml")
            labels_path = os.path.dirname(xmlFiles[i]).replace("annotations/xmls","labels")
            if not os.path.exists(labels_path):
                os.mkdir(labels_path)
            assert(os.path.exists(xmlFiles[i]))

            
    
    return xmlFiles


def main():

    parser = argparse.ArgumentParser(description='run phase2.')
    parser.add_argument('--class_file', type=str, help='path of the file containing list of classes of detection problem. sample file at "datasets/damage_classes.txt"',default='datasets/damage_classes.txt')
    parser.add_argument('--input_file', type=str, help='location to the list of images/xml files(absolute path). sample file at "datasets/train.txt"',default='datasets/train.txt')
    args = parser.parse_args()

    #assign each class of dataset to a number
    outputCtoId = {}

    f = open(args.class_file,"r")
    lines = f.readlines()
    f.close()
    num_classes=1
    for i in range(len(lines)):
        outputCtoId[lines[i].strip()] = i

    #read the path of the directory where XML and images are present
    xmlFiles = getFileList3(args.input_file)

    print("total files:", len(xmlFiles))
    
    #loop over each file under dirPath
    for file in xmlFiles:
        filePath = file
        #print(filePath)
        tree = ET.parse(filePath)
        root = tree.getroot()
        
        i = 0
        imageFile = filePath[:-4].replace("annotations/xmls","images")+"."+imageType[i]
        while (not os.path.isfile(imageFile) and i<2):
            i+=1
            imageFile = filePath[:-4].replace("annotations/xmls","images")+"."+imageType[i]

        if not os.path.isfile(imageFile):
            print("File not found:",imageFile)
            continue
        
        txtFile = imageFile.replace("images","labels")
        txtFile = txtFile[:-4]+".txt"
        yoloOutput = open(txtFile,"w")
        
        #loop over each object tag in annotation tag
        for objects in root.findall('object'):
            surfaceType = objects.find('name').text.replace(" ","")
    
            
            if surfaceType=="D00" or surfaceType=="D10" or surfaceType=="D20" or surfaceType=="D40":
                bndbox = objects.find('bndbox')
                [minX,minY,maxX,maxY] = [float(child.text) for child in bndbox]
                [x,y,w,h] = getYoloNumbers(imageFile,minX,minY,maxX, maxY)
                yoloOutput.write(str(outputCtoId[surfaceType])+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"\n")
                imageListDict[outputCtoId[surfaceType]].add(imageFile)
                
        
        yoloOutput.close()

    for cl in imageListDict:
        print(lines[cl].strip(),":",len(imageListDict[cl]))
    


if __name__== "__main__":
    main()
