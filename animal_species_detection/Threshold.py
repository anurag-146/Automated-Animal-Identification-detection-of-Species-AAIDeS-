# Python program to illustrate
# simple thresholding type on an image
     
# organizing imports
import cv2
import numpy as np
import os

from .  import models
def img_preprocessing(imgpath1='NA',carpartType='NA',srno=0,title="na"):
    # path to input image is specified and 
    # image is loaded with imread command
    UPLOAD_DIR=os.getcwd()+"\\DataSet\\" 
    UPLOAD_DIR1=os.getcwd()+"\\DataSet\\train\\" 
    UPLOAD_DIR2=os.getcwd()+"\\DataSet\\test\\" 
    print("type="+carpartType)
    try:
        os.mkdir(UPLOAD_DIR1+str(srno))
        os.mkdir(UPLOAD_DIR2+str(srno))
    except FileExistsError:
        print("directory exist")
    imgpath=UPLOAD_DIR+imgpath1
    image1 = cv2.imread(imgpath)
    
    # cv2.cvtColor is applied over the
    # image input with applied parameters
    # to convert the image in grayscale
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    
    # applying different thresholding
    # techniques on the input image
    # all pixels value above 120 will
    # be set to 255
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
    
    # the window showing output images
    # with the corresponding thresholding
    # techniques applied to the input images

    #cv2.imshow('Binary Threshold', thresh1)
    #cv2.imshow('Binary Threshold Inverted', thresh2)
    width = 64
    height = 64
    dim = (width, height)
    
    # resize image
    #resized = cv2.resize(thresh2, dim, interpolation = cv2.INTER_AREA)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(UPLOAD_DIR+"\\test\\"+str(srno)+"\\"+imgpath1,resized)
    cv2.imwrite(UPLOAD_DIR+"\\train\\"+str(srno)+"\\"+imgpath1,resized)
    #cv2.imshow('Truncated Threshold', thresh3)
    #cv2.imshow('Set to 0', thresh4)
    #cv2.imshow('Set to 0 Inverted', thresh5)
    
    # De-allocate any associated memory usage 
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
 

def img_preprocessing1(imgpath1='NA',category='NA', title="NA"):
    # path to input image is specified and 
    # image is loaded with imread command
    print("in processing")
    UPLOAD_DIR=os.getcwd()+"\\DataSet\\temp\\" 
    print(UPLOAD_DIR)
    UPLOAD_DIR1=os.getcwd()+"\\DataSet\\"+title+"\\train\\"
    print(UPLOAD_DIR1) 
    UPLOAD_DIR2=os.getcwd()+"\\DataSet\\"+title+"\\test\\" 
    print(UPLOAD_DIR2)
    print("imgpath="+imgpath1)
    srno=models.getSrno(category)
    print("type="+category)
    try:
        os.mkdir(UPLOAD_DIR1+str(srno))
        os.mkdir(UPLOAD_DIR2+str(srno))
    except FileExistsError:
        print("directory exist")
    imgpath=UPLOAD_DIR+"/"+title+"/"+imgpath1
    print(imgpath)
    image1 = cv2.imread(imgpath)
    
    # cv2.cvtColor is applied over the
    # image input with applied parameters
    # to convert the image in grayscale
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    
    # applying different thresholding
    # techniques on the input image
    # all pixels value above 120 will
    # be set to 255
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
    
    # the window showing output images
    # with the corresponding thresholding
    # techniques applied to the input images

    #cv2.imshow('Binary Threshold', thresh1)
    #cv2.imshow('Binary Threshold Inverted', thresh2)
    width = 64
    height = 64
    dim = (width, height)
    
    # resize image
    #resized = cv2.resize(thresh2, dim, interpolation = cv2.INTER_AREA)
    #resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    resized = cv2.resize(image1, dim, interpolation = cv2.INTER_AREA)
    
    cv2.imwrite(UPLOAD_DIR1+str(srno)+"\\"+imgpath1,resized)
    cv2.imwrite(UPLOAD_DIR2+str(srno)+"\\"+imgpath1,resized)
    #cv2.imshow('Truncated Threshold', thresh3)
    #cv2.imshow('Set to 0', thresh4)
    #cv2.imshow('Set to 0 Inverted', thresh5)
    
    # De-allocate any associated memory usage 
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

def preprocessInput(imgpath1='NA',path="NA"):
    # path to input image is specified and 
    # image is loaded with imread command
    UPLOAD_DIR=path+"\\InputImg\\"  
     
     
    imgpath=UPLOAD_DIR+"/"+imgpath1
    image1 = cv2.imread(imgpath)
    
    # cv2.cvtColor is applied over the
    # image input with applied parameters
    # to convert the image in grayscale
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    
    # applying different thresholding
    # techniques on the input image
    # all pixels value above 120 will
    # be set to 255
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
    
    # the window showing output images
    # with the corresponding thresholding
    # techniques applied to the input images

    #cv2.imshow('Binary Threshold', thresh1)
    #cv2.imshow('Binary Threshold Inverted', thresh2)
    width = 64
    height = 64
    dim = (width, height)
    
    # resize image
    #resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    resized = cv2.resize(image1, dim, interpolation = cv2.INTER_AREA)
    
     #cv2.imshow('Truncated Threshold', thresh3)
    #cv2.imshow('Set to 0', thresh4)
    #cv2.imshow('Set to 0 Inverted', thresh5)
    cv2.imwrite(UPLOAD_DIR+"\\temp\\1\\processed_"+imgpath1,resized)
    # De-allocate any associated memory usage 
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    return resized