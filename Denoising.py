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
TRAINSIZE = 421*36
TESTSIZE = 151*36

# %%
xtrain = image_dataset_from_directory('data/train', labels=None, label_mode=None, color_mode='grayscale', batch_size=TRAINSIZE)
xtest = image_dataset_from_directory('data/test', labels=None, label_mode=None, color_mode='grayscale', batch_size=TESTSIZE)

# %%
xtrain = np.asarray(tuple(xtrain))
xtrain = xtrain.astype('float32')/255
xtrain = xtrain[0]
xtest = np.asarray(tuple(xtest))
xtest = xtest.astype('float32')/255
xtest = xtest[0]
print(xtrain.shape, xtest.shape)

# %%
noise = 0.5
xtrain_noisy = xtrain + noise + np.random.normal(loc = 0, scale = 1, size = xtrain.shape)
xtrain_noisy = np.clip(xtrain_noisy, 0., 1)
xtest_noisy = xtest + noise + np.random.normal(loc=0, scale=1, size = xtest.shape)
xtest_noisy = np.clip(xtest_noisy, 0., 1)

# %%
n = 10
plt.figure(figsize=(20, 2))
for i in range(1, n + 1):
    ax = plt.subplot(1, n, i)
    plt.imshow(xtrain_noisy[i].reshape(256, 256))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()

# %%
n = 10
plt.figure(figsize=(20, 2))
for i in range(1, n + 1):
    ax = plt.subplot(1, n, i)
    plt.imshow(xtest_noisy[i].reshape(256, 256))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()

# %%
imginput = keras.Input(shape = (256, 256, 1))
x = layers.Conv2D(32, (3, 3), activation = 'relu', padding = 'same')(imginput)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
encoded = layers.MaxPooling2D((2, 2), padding='same')(x)
#end of convolution layers
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(encoded)
x = layers.UpSampling2D((2, 2))(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.UpSampling2D((2, 2))(x)
decoded = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)
#end of upsampling
autoencoder = keras.Model(imginput, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# %%
autoencoder.fit(xtrain_noisy, xtrain,
                epochs = 100,
                batch_size=64,
                shuffle=True,
                validation_data=(xtest_noisy, xtest))

# %%
autoencoder.summary()

# %%
aejson = autoencoder.to_json()
with open('models/autoencoder_model.json', "w") as jsdump:
    jsdump.write(aejson)
    print("Successful Model Save")
    autoencoder.save_weights('autoencoder.weights.h5')
    print("Weights successfully saved")


