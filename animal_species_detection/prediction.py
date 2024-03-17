#!C:\Users\Spider Projects\AppData\Local\Programs\Python\Python38\python
# Import modules for CGI handling
import cgi, cgitb, jinja2 
import numpy as np
import cv2
import tensorflow as tf
import keras
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import os
from . import models
from . import Threshold

def Prediction(filenm="NA",UPLOAD_DIR_Model="NA"):
    path=UPLOAD_DIR_Model
    UPLOAD_DIR_Model=UPLOAD_DIR_Model+"\\dataSet\\model\\best_model_dataflair3.h5"
    model = keras.models.load_model(UPLOAD_DIR_Model)
    #filenm=path+"/InputImg/"+filenm
    word_dict=models.getDictionary()
    background = None
    accumulated_weight = 0.5

    ROI_top = 100
    ROI_bottom = 300
    ROI_right = 150
    ROI_left = 350
    print("file="+filenm)
    thresholded =  Threshold.preprocessInput(filenm,path)
    
    #thresholded = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2RGB)
    #thresholded = np.reshape(thresholded, (1,thresholded.shape[0],thresholded.shape[1],3))
    """
    pred = model.predict(thresholded, verbose=0)
    print(pred)
    print(np.argmax(pred))
    print(word_dict[np.argmax(pred)]) 
"""            



    UPLOAD_DIR=path+"\\InputImg\\temp\\"  
    test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=UPLOAD_DIR, target_size=(64,64), class_mode='categorical', batch_size=1, shuffle=True)
    imgs, labels = next(test_batches)
    predictions = model.predict(imgs, verbose=0)
    print(predictions)
    print(word_dict[np.argmax(predictions)])
    cv2.destroyAllWindows()
    return word_dict[np.argmax(predictions)]
def Prediction1(filenm="NA",UPLOAD_DIR_Model="NA",category="na"):
    path=UPLOAD_DIR_Model
    UPLOAD_DIR_Model=UPLOAD_DIR_Model+"\\dataSet\\"+category+"\\model\\best_model_dataflair3.h5"
    model = keras.models.load_model(UPLOAD_DIR_Model)
    #filenm=path+"/InputImg/"+filenm
    word_dict=models.getDictionary1(category)
    background = None
    accumulated_weight = 0.5

    ROI_top = 100
    ROI_bottom = 300
    ROI_right = 150
    ROI_left = 350
    print("file="+filenm)
    #thresholded =  Threshold.preprocessInput(filenm,path)
    
    #thresholded = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2RGB)
    #thresholded = np.reshape(thresholded, (1,thresholded.shape[0],thresholded.shape[1],3))
    """
    pred = model.predict(thresholded, verbose=0)
    print(pred)
    print(np.argmax(pred))
    print(word_dict[np.argmax(pred)]) 
"""            



    UPLOAD_DIR=path+"\\InputImg\\temp\\"  
    test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=UPLOAD_DIR, target_size=(64,64), class_mode='categorical', batch_size=1, shuffle=True)
    imgs, labels = next(test_batches)
    predictions = model.predict(imgs, verbose=0)
    print(predictions)
    print(word_dict[np.argmax(predictions)])
    cv2.destroyAllWindows()
    return word_dict[np.argmax(predictions)]
