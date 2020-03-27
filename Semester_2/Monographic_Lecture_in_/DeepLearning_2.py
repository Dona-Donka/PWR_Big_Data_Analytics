# https://towardsdatascience.com/text-classification-in-keras-part-1-a-simple-reuters-news-classifier-9558d34d01d3

import keras
from keras.datasets import reuters
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test)=reuters.load_data(num_words=None, test_split=0.20)
word_index = reuters.get_word_index(path="reuters_word_index.json")
print(word_index)

print("train samples: {}".format(len(x_train)))
print("test samples: {}".format(len(x_test)))
num_classes=max(y_train)+1
print("# of classes: {}".format(num_classes))
print(x_train[0])
print(y_train[0])

index_to_word={}
for key, value in word_index.items():
  index_to_word[value]=key

print([index_to_word[i] for i in x_train[0]])

from keras.preprocessing.text import Tokenizer
max_words=10000
tokenizer = Tokenizer(num_words=max_words)
x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')
y_train=keras.utils.to_categorical(y_train, num_classes)
y_test=keras.utils.to_categorical(y_test, num_classes)


from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

model=Sequential()
#model.add(Dense(512, input_shape=(max_words,)))
model.add(Dense(4, input_shape=(max_words,)))

model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

batch_size=32
epochs=10
history=model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.1)

score=model.evaluate(x_test, y_test, batch_size=batch_size, verbose=1)
print('Test loss: {}'.format(score[0]))
print('Test acc: {}'.format(score[1]))

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']
print(val_acc)

import matplotlib.pyplot as plt
ep = [x for x in range(epochs)]
#plt.plot(ep, acc, 'ro')
#plt.plot(ep, val_acc, "bo")
#plt.savefig("/home/dona/Pulpit/hw_2_1.jpg")

plt.plot(ep, loss, 'ro')
plt.plot(ep, val_loss, "bo")
plt.savefig("/home/dona/Pulpit/hw_2_2.jpg")