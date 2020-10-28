import tensorflow as tf
import numpy as np
import os
import tensorflow_datasets as tfds
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPooling2D

def normalize_img(image,label):
     return tf.cast(image, tf.float32) / 255., label



(emnist_train,emnist_test),emnist_info = tfds.load('emnist',split=['train','test'],shuffle_files=True,as_supervised=True,with_info=True)

emnist_train = emnist_train.map(normalize_img,num_parallel_calls=tf.data.experimental.AUTOTUNE) #TFDS are uint8 by default, need to be converted to float32 and then normalized
emnist_train = emnist_train.cache() #cache dataset in memory
emnist_train = emnist_train.shuffle(emnist_info.splits['train'].num_examples) #shuffles dataset for better learning
emnist_train = emnist_train.batch(128) #batches dataset
emnist_train = emnist_train.prefetch(tf.data.experimental.AUTOTUNE) #prefetching? No clue what that is

emnist_test = emnist_test.map(normalize_img, num_parallel_calls=tf.data.experimental.AUTOTUNE)
emnist_test = emnist_test.batch(128)
emnist_test = emnist_test.cache()
emnist_test = emnist_test.prefetch(tf.data.experimental.AUTOTUNE)

print(emnist_info)

# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
#   tf.keras.layers.Dense(256,activation='relu'),
#   tf.keras.layers.Dense(62, activation='softmax')
# ])
# model.compile(
#     loss='sparse_categorical_crossentropy',
#     optimizer='adam',
#     metrics=['accuracy'],
# )

model = Sequential()
model.add(Conv2D(128,(3,3),input_shape=(28,28,1)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(128,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(128))

model.add(Dense(62))
model.add(Activation("sigmoid"))

model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(
    emnist_train,
    epochs=6,
    validation_data=emnist_test
)

model.save('64x64x3.model')
model.save_weights('hi.weights')