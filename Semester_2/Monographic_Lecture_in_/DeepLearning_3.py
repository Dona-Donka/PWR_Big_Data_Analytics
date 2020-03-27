# Based on: https://www.kaggle.com/ruchibahl18/cats-vs-dogs-basic-cnn-tutorial
# https://www.geeksforgeeks.org/python-data-augmentation/


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, Activation, Conv2D, MaxPooling2D

# We should check training data before start training our model. We created '/input_dl_hw3" direcotry
# that stores the following files:
# sampleSubmission.csv" -
# "/train" - a file with sample images of dogs and cats. We use it for train the model. 
# "/test" - a file with sample images for testing. 

# Input data files, that should print: ['sampleSubmission.csv', 'train', 'test1']
import os
print(os.listdir("/home/dona/PycharmProjects/bigDataAlgorithms/input_dl_hw3/"))

main_dir = "../input_dl_hw3/"
train_dir = "/home/dona/PycharmProjects/bigDataAlgorithms/input_dl_hw3/train"
path = os.path.join(main_dir,train_dir)

# We applied 'break' here to display one image
for p in os.listdir(path):
    category = p.split(".")[0]
    img_array = cv2.imread(os.path.join(path,p),cv2.IMREAD_GRAYSCALE)
    new_img_array = cv2.resize(img_array, dsize=(80, 80))
    plt.imshow(new_img_array,cmap="gray")
    break


######################################################################################
# Declare a training array of pixels X
X = []
# Declare a target binary array y
y = []

convert = lambda category: int(category == 'dog')


# Importing necessary library
import Augmentor

# Passing the path of the image directory
#p = Augmentor.Pipeline(path)
# Defining augmentation parameters and generating 5 samples
#p.flip_left_right(0.5)
#p.black_and_white(0.1)
#p.rotate(0.3, 10, 10)
#p.skew(0.4, 0.5)
#p.zoom(probability=0.2, min_factor=1.1, max_factor=1.5)
#p.sample(5)

# It appends resized images (80x80) to X array and thei category value into y array.
def create_test_data(path):

    for p in os.listdir(path):
        category = p.split(".")[0]
        category = convert(category)
        img_array = cv2.imread(os.path.join(path, p), cv2.IMREAD_GRAYSCALE)
        try:
            new_img_array = cv2.resize(img_array, dsize=(80, 80))
        except:
            print(p, "cv2.error: OpenCV(4.1.2) /io/opencv/modules/imgproc/src/resize.cpp:3720: error: (-215:Assertion failed) !ssize.empty() in function 'resize'")
        X.append(new_img_array)
        y.append(category)

create_test_data(path)
X = np.array(X).reshape(-1,80,80,1)
y = np.array(y)

#Normalize data
X = X/255.0

# Define our CNN model, add layers

# Define a Sequential model
model = Sequential()

# Adds a densely-connected layer with 64 units to the model:
model.add(Conv2D(64,(3,3), activation = 'relu', input_shape = X.shape[1:]))
model.add(MaxPooling2D(pool_size = (2,2)))
# Add another:
model.add(Conv2D(64,(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
# Add a softmax layer with 10 output units:
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer="adam",
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

# Preporcess the test data also same as that the training data.

train_dir = "/home/dona/PycharmProjects/bigDataAlgorithms/input_dl_hw3/test1"
path = os.path.join(main_dir,train_dir)
#os.listdir(path)

X_test = []
id_line = []
def create_test1_data(path):
    for p in os.listdir(path):
        id_line.append(p.split(".")[0])
        img_array = cv2.imread(os.path.join(path,p),cv2.IMREAD_GRAYSCALE)
        new_img_array = cv2.resize(img_array, dsize=(80, 80))
        X_test.append(new_img_array)
create_test1_data(path)
X_test = np.array(X_test).reshape(-1,80,80,1)
X_test = X_test/255



# Feed the model with test data to predict
predictions = model.predict(X_test)

predicted_val = [int(round(p[0])) for p in predictions]
submission_df = pd.DataFrame({'id':id_line, 'label':predicted_val})


# Write the data frame to a csv file
submission_df.to_csv("submission.csv", index=False)