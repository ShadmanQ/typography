import numpy as np
import tensorflow as tf
import os
import cv2
import string
import random
import pickle

DIR = os.getcwd() + "/nist"
CLASSES = list(string.digits) + list(string.ascii_letters)
training_data = []


print(len(CLASSES))
for char in CLASSES:
    print("Now loading data for: " + char)
    fullpath = os.path.join(DIR,char)
    class_num = CLASSES.index(char)
    for folder in os.listdir(fullpath):
        folder_path = (os.path.join(fullpath,folder))
        for img in os.listdir(folder_path)[0:1500]:
            img = cv2.imread(os.path.join(folder_path,img),cv2.IMREAD_GRAYSCALE)
            img_array = cv2.resize(img, (32,32))
            training_data.append([img_array,class_num])

print(str(len(training_data)) + " datapoints have been loaded")

X=[]
y=[]


random.shuffle(training_data)

for (features, label) in training_data:
    X.append(features)
    y.append(label)
print(max(y),min(y))
X = np.array(X).reshape(-1,32,32,1)


# np.savetxt('X.txt',gee)
# np.savetxt('y.txt',y)
# with open('test.txt','wb') as f:
#     np.save(f,X)

# with open('test2.text','wb') as g:
#     np.save(g,y)

X_dump = open("X.pickle","wb")
pickle.dump(X,X_dump)
X_dump.close()

y_dump = open("y.pickle","wb")
pickle.dump(y,y_dump)
y_dump.close()
