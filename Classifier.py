# %%
import tensorflow
import keras
from keras import layers
from keras.models import Sequential
from keras.utils import image_dataset_from_directory
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

# %%
traindata = image_dataset_from_directory('data/train', labels='inferred', label_mode='categorical', color_mode='grayscale', batch_size=64)
testdata = image_dataset_from_directory('data/test', labels='inferred', label_mode='categorical', color_mode='grayscale', batch_size=64)

# %%
classifier = Sequential()
classifier.add(layers.Input(shape=(256, 256, 1)))
classifier.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
classifier.add(layers.MaxPool2D((2, 2), padding='same'))
classifier.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
classifier.add(layers.MaxPool2D((2, 2), padding='same'))
classifier.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
classifier.add(layers.MaxPool2D((2, 2), padding='same'))
classifier.add(layers.Flatten())
classifier.add(layers.Dense(units=128, activation='relu'))
classifier.add(layers.Dropout(rate=0.4))
classifier.add(layers.Dense(units=96, activation='relu'))
classifier.add(layers.Dropout(rate=0.4))
classifier.add(layers.Dense(units=64, activation='relu'))
classifier.add(layers.Dense(units=36, activation='softmax'))

classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# %%
classifier.summary()

# %%
classifier.fit(traindata,
               epochs=100,
               batch_size=64,
               shuffle=True,
               validation_data=testdata)

# %%
classjson = classifier.to_json()

# %%
with open('models/classifier_model.json', "w") as jsdump:
    jsdump.write(classjson)
    print("Successful Model Save")
    classifier.save_weights('classifier.weights.h5')
    print("Weights successfully saved")

# %% [markdown]
# Lighting and camera quality (main) tend to cause issues with the classification and parts of the image themself are unclear in the scenario and cause lower accuracy.


