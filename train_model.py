import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout,Activation,Flatten,Conv2D,MaxPooling2D
import numpy as np
import os
import pickle
import time

X = pickle.load(open("X.pickle",'rb'))
y = pickle.load(open("y.pickle",'rb'))
print("stuff has been loaded")

X = X/255.0
print(X.dtype)

y = np.array(y)

print(max(y),min(y))

print(type(X))
print(type(y))


model = Sequential()
model.add(Conv2D(64,(3,3),input_shape = X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])

try:
    model.fit(X,y,batch_size=64,validation_split=0.1)
except Exception as e:
    print("there was an issue")
    print(str(e)[0:120])
