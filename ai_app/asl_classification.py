# -*- coding: utf-8 -*-
"""ASL-Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HTaPkTjeJ3ZOnmiIo178Y1iZO-3Y70r_
"""

# dataset link
# https://www.kaggle.com/grassknoted/asl-alphabet

# from google.colab import drive
# drive.mount("/content/gdrive", force_remount=True)

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds

import cv2
# from google.colab.patches import cv2_imshow
import os
import numpy as np
np.random.seed(5) 
import tensorflow as tf
#tf.set_random_seed(2)
import matplotlib.pyplot as plt
# %matplotlib inline
import keras.utils
print("packages imported")
test_tf= tf.test.gpu_device_name()
print("test_tf : ",test_tf)

# link to connect kaggle with google colab
# https://medium.com/unpackai/how-to-use-kaggle-datasets-in-google-colab-f9b2e4b5767c

# ! pip install -q kaggle

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/gdrive/MyDrive/Colab\ Notebooks/

# os.environ['KAGGLE_CONFIG_DIR'] = "."
# os.environ['KAGGLE_CONFIG_DIR'] = "/content/gdrive/MyDrive/Colab Notebooks/"

# !kaggle datasets download grassknoted/asl-alphabet

# !unzip "/content/gdrive/MyDrive/Colab Notebooks/asl-alphabet.zip"

import pathlib
print("1")
data_dir = tf.keras.utils.get_file(fname='/home/project1/major-project/MDA-Major-Project/asl_alphabet_train/asl_alphabet_train', origin=False, untar=False)

print("2")
data_dir = pathlib.Path(data_dir)
print(data_dir)

train_ds = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=0.1, subset='training', seed=100, image_size=(200,200))

# split => 0.2 (80:20)
# Found 87000 files belonging to 29 classes.
# Using 69600 files for training.

# split => 0.1 (90:10)
# Found 87000 files belonging to 29 classes.
# Using 78300 files for training.

validation_ds = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=0.2, subset='validation', seed=100, image_size=(200, 200))

# split => 0.1
# Found 87000 files belonging to 29 classes.
# Using 8700 files for validation.

class_names = train_ds.class_names
print(class_names)

# plt.figure(figsize=(10, 10))
# for images, labels in train_ds.take(1):
#   for i in range(9):
#     ax = plt.subplot(3, 3, i + 1)
#     plt.imshow(images[i].numpy().astype("uint8"))
#     plt.title(class_names[labels[i]])
#     plt.axis("off")

normalization_layer = tf.keras.layers.Rescaling(1./255)

batch_size = 128
img_height = 200
img_width = 200

# train_dir = '/content/gdrive/MyDrive/Colab Notebooks/asl_alphabet_train/asl_alphabet_train'

# image = train_dir + "/B/B1.jpg"

# image = cv2.imread(image)
# image.shape

# cv2_imshow(image)

from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Conv2D, Dense, Dropout, Flatten
from keras.layers import Flatten, Dense
from keras.models import Sequential
from tensorflow.keras import layers, models

num_classes = 29
#build the model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3), padding='same'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.BatchNormalization())

model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.BatchNormalization())


model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.BatchNormalization())


model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.BatchNormalization())


model.add(layers.Flatten())
model.add(layers.Dropout(0.5))


model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(29, activation='softmax'))

model.summary()

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

history = model.fit(
  train_ds,
  batch_size=batch_size,
  validation_data=validation_ds,
  epochs=15,
)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

# plt.figure(figsize=(8, 8))
# plt.subplot(1, 2, 1)
# plt.plot(epochs_range, acc, label='Training Accuracy')
# plt.plot(epochs_range, val_acc, label='Validation Accuracy')
# plt.legend(loc='lower right')
# plt.title('Training and Validation Accuracy')

# plt.subplot(1, 2, 2)
# plt.plot(epochs_range, loss, label='Training Loss')
# plt.plot(epochs_range, val_loss, label='Validation Loss')
# plt.legend(loc='upper right')
# plt.title('Training and Validation Loss')
# plt.show()

# #save model
# model.save('ASL.model')

#load model
model=tf.keras.models.load_model('./ASL.model')

#prepare image to prediction
def prepare(filepath):
    image = cv2.imdecode(np.fromfile(filepath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (64, 64))
    image=image.reshape(-1, 64, 64, 1)
    image=image.astype('float32')/255.0
    return  image

#use this function to predict images
def predict(my_model, filepath):
    prediction = model.predict([prepare(filepath)]) 
    category = np.argmax(prediction[0])
    return  class_names[category]

image = '/asl_alphabet_train/asl_alphabet_train/T/T2348.jpg'
category = predict(model, image)
print("The image class is: " + str(category))

