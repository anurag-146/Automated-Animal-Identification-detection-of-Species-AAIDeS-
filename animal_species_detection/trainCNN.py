#!C:\Users\Spider Projects\AppData\Local\Programs\Python\Python39\python
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D, Dropout
#from keras.optimizers import Adam, SGD
#from keras.optimizers import SGD
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
import itertools
import random
import warnings
import numpy as np
import cv2
import os
import cgi
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import ModelCheckpoint, EarlyStopping
 
#from matplotlib import pyplot as plt
try:
    print("Content-type: text/html")
    print()
    form=cgi.FieldStorage()
    warnings.simplefilter(action='ignore', category=FutureWarning)
    #title=form.getvalue("title")
   
    path="D:\\django-setup\\animal_species_detection\\Scripts/animal_species_detection/static"
    UPLOAD_DIR=path+"\\dataset\\"
    UPLOAD_DIR_Model=UPLOAD_DIR+"\\model\\"
    try:
        os.mkdir(UPLOAD_DIR_Model) 
    except FileExistsError:
        print("directory exist")
    train_path=path+"\\dataset\\train\\"
    test_path=path+"\\dataset\\test\\"
    #train_path = r'\\train\\'
    #test_path = r'E:\\gesture\\test\\'
    lblcnt=5
    """
    try:
        lblcnt=int(getLabelCount())
    except Exception as e:
        print("error lbl")
        print(e)
    """
    print("lblcnt")
    print(str(lblcnt))
    train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=train_path, target_size=(64,64), class_mode='categorical', batch_size=lblcnt,shuffle=True)
    test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=test_path, target_size=(64,64), class_mode='categorical', batch_size=lblcnt, shuffle=True)

    imgs, labels = next(train_batches)


    #Plotting the images...
    """
    def plotImages(images_arr):
        fig, axes = plt.subplots(1, 10, figsize=(30,20))
        axes = axes.flatten()
        for img, ax in zip( images_arr, axes):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            ax.imshow(img)
            ax.axis('off')
        plt.tight_layout()
        plt.show()
    """

    #plotImages(imgs)
    print(imgs.shape)
    print("input lables")
    print(labels)

    model = Sequential()

    model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(64,64,3)))
    model.add(MaxPool2D(pool_size=(2, 2), strides=2))

    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding = 'same'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=2))

    model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu', padding = 'valid'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=2))

    model.add(Flatten())

    model.add(Dense(64,activation ="relu"))
    model.add(Dense(128,activation ="relu"))
    #model.add(Dropout(0.2))
    model.add(Dense(128,activation ="relu"))
    #model.add(Dropout(0.3))
    #model.add(Dense(10,activation ="softmax"))
    model.add(Dense(lblcnt,activation ="softmax"))


    # In[23]:


    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=1, min_lr=0.0001)
    early_stop = EarlyStopping(monitor='val_loss', min_delta=0, patience=2, verbose=0, mode='auto')



    model.compile(optimizer=SGD(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=1, min_lr=0.0005)
    early_stop = EarlyStopping(monitor='val_loss', min_delta=0, patience=2, verbose=0, mode='auto')


    history2 = model.fit(train_batches, epochs=10, callbacks=[reduce_lr, early_stop],  validation_data = test_batches)#, checkpoint])
    imgs, labels = next(train_batches) # For getting next batch of imgs...
    print("displaylables")
    print(labels)
    imgs, labels = next(test_batches) # For getting next batch of imgs...
    scores = model.evaluate(imgs, labels, verbose=0)
    print(f'{model.metrics_names[0]} of {scores[0]}; {model.metrics_names[1]} of {scores[1]*100}%')


    #model.save('best_model_dataflair.h5')
    model.save(UPLOAD_DIR_Model+'\\best_model_dataflair3.h5')
    UPLOAD_DIR_Model=UPLOAD_DIR_Model+"\\best_model_dataflair3.h5"
    print(history2.history)

    imgs, labels = next(test_batches)

    #model = keras.models.load_model(r"best_model_dataflair3.h5")
    model = keras.models.load_model(UPLOAD_DIR_Model)
    scores = model.evaluate(imgs, labels, verbose=0)
    print(f'{model.metrics_names[0]} of {scores[0]}; {model.metrics_names[1]} of {scores[1]*100}%')

    model.summary()

    scores #[loss, accuracy] on test data...
    model.metrics_names


    #word_dict = {0:'One',1:'Ten',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
    #word_dict = {0:'Four',1:'One',2:'Ten',3:'Three',4:'Two',5:'Y'}
    word_dict =getDictionary()
    #word_dict = {0:'Four',1:'One',2:'Three',3:'Two'}
    predictions = model.predict(imgs, verbose=0)
    print("predictions on a small set of test data--")
    print("")
    print(predictions)
    for ind, i in enumerate(predictions):
        print(word_dict[np.argmax(i)], end='   ')

    #plotImages(imgs)
    print('Actual labels')
    for i in labels:
        print(word_dict[np.argmax(i)], end='   ')

    print(imgs.shape)

    history2.history
    """
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=http://localhost:8080/frompython1?sts=success'/>")
    print("</head>")
    print("</html>")
    """ 
    
except Exception as e:
    print("error")
    print(e)