# imports for array-handling and plotting
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

(xTrain, yTrain), (xTest, yTest) = mnist.load_data()

'''
fig = plt.figure()
for i in range(9):
  plt.subplot(3,3,i+1)
  plt.tight_layout()
  plt.imshow(xTrain[i], cmap='gray', interpolation='none')
  plt.title("Digit: {}".format(yTrain[i]))
  plt.xticks([])
  plt.yticks([])
fig

fig = plt.figure()
plt.subplot(2,1,1)
plt.imshow(xTrain[0], cmap='gray', interpolation='none')
plt.title("Digit: {}".format(yTrain[0]))
plt.xticks([])
plt.yticks([])
plt.subplot(2,1,2)
plt.hist(xTrain[0].reshape(784))
plt.title("Pixel Value Distribution")
fig
'''

print("xTrain shape", xTrain.shape)
print("yTrain shape", yTrain.shape)
print("xTest shape", xTest.shape)
print("yTest shape", yTest.shape)

xTrain = xTrain.reshape(60000, 784)
xTest = xTest.reshape(10000, 784)
xTrain = xTrain.astype('float32')
xTest = xTest.astype('float32')

xTrain /= 255
xTest /= 255

print("Train matrix shape", xTrain.shape)
print("Test matrix shape", xTest.shape)

n_classes = 10
print("Shape before one-hot encoding: ", yTrain.shape)
Y_train = np_utils.to_categorical(yTrain, n_classes)
Y_test = np_utils.to_categorical(yTest, n_classes)
print("Shape after one-hot encoding: ", Y_train.shape)

# building a linear stack of layers with the sequential model
model = Sequential()
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(10))
model.add(Activation('softmax'))

# compiling the model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

# training the model and saving metrics
'''
history = model.fit(xTrain, Y_train,history
                    batch_size=128, epochs=20,
                    verbose=2,
                    validation_data=(xTest, Y_test))

# saving the model
save_dir = "./results/"
modelName = 'keras_mnist.h5'
modelPath = os.path.join(save_dir, modelName)
model.save(modelPath)
print('Saved trained model at %s ' % modelPath)
'''
'''
# plot the metrics
fig = plt.figure()
plt.subplot(2,1,1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='lower right')

plt.subplot(2,1,2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')

plt.tight_layout()

fig
'''

mnistModel = load_model("./results/keras_mnist.h5")
lostAndMetrics = mnistModel.evaluate(xTest, Y_test, verbose=2)

print("Test Loss", lostAndMetrics[0])
print("Test Accuracy", lostAndMetrics[1])

# load the model and test it
mnistModel = load_model("./results/keras_mnist.h5")
predicted = mnistModel.predict_classes(xTest)

# check the predictions statistics
good = np.nonzero(predicted == yTest)[0]
bad = np.nonzero(predicted != yTest)[0]

print(len(good), " classified correctly")
print(len(bad), " classified incorrectly")

# adapt figure size to accomodate 18 subplots
plt.rcParams['figure.figsize'] = (7,14)

figureEval = plt.figure()

# plot 9 correct predictions
for i, correct in enumerate(good[:9]):
    plt.subplot(6,3,i+1)
    plt.imshow(xTest[correct].reshape(28, 28), cmap='gray', interpolation='none')
    plt.title(
      "Predicted: {}, Truth: {}".format(predicted[correct],
                                        yTest[correct]))
    plt.xticks([])
    plt.yticks([])

# plot 9 incorrect predictions
for i, incorrect in enumerate(bad[:9]):
    plt.subplot(6,3,i+10)
    plt.imshow(xTest[incorrect].reshape(28, 28), cmap='gray', interpolation='none')
    plt.title(
      "Predicted {}, Truth: {}".format(predicted[incorrect],
                                       yTest[incorrect]))
    plt.xticks([])
    plt.yticks([])

figureEval
           