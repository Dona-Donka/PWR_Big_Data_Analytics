import librosa as lr
import glob
import scipy.misc
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, Activation, Conv2D, MaxPooling2D
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# ls -v | cat -n | while read n f; do mv -n "$f" "$n.wav"; done
# mv `ls *.wav | sort -R | sed -n 1~3p` down_test
# for file in *.png; do mv "$file" "${file/.wav/_go.png}"; done

# I used:
# https://www.youtube.com/watch?v=Z7YM-HAz-IY
# https://www.tensorflow.org/tutorials/images/classification

import os
class_names = ["down", "go", "left", "no", "off", "on", "right", "stop", "up", "yes"]
import scipy.signal


# prepare images
def getWaveData(data,type):
    audio, sfreq = lr.load(data)
    f, t, Zxx = scipy.signal.stft(audio, fs=sfreq)
    plt.figure(figsize=(10, 10))

    plt.title("STFT Magnitude")
    plt.specgram(audio, cmap=plt.get_cmap('RdYlGn'), Fs=sfreq)
    plt.savefig("train_images/" +type + "." + data[len("train_data/"):-4] + ".png")
    plt.close()

    return f, t
def createDataFiles():
    for word in glob.glob("train_data/*"):
        k = ""
        for letter in word[len("train_data/"):-4]:
            if letter.isalpha():
              k = k + letter
        getWaveData(word, k)

#createDataFiles()
def main():
    print("Number of train waves: ", len(os.listdir("train_images/")))
    print("Number of validation waves: ", len(os.listdir("test_images/")))


    train_image_generator = ImageDataGenerator(rescale=1. / 255)  # Generator for our training data
    validation_image_generator = ImageDataGenerator(rescale=1. / 255)

    batch_size = 100
    #batch_size = 40
    epochs = 10
    IMG_HEIGHT = 150
    IMG_WIDTH = 150

    train_data_gen = train_image_generator.flow_from_directory(batch_size=batch_size,
                                                               directory="train_images/",
                                                               shuffle=True,
                                                               target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                               class_mode='binary')

    val_data_gen = validation_image_generator.flow_from_directory(batch_size=batch_size,
                                                                  directory="test_images/",
                                                                  target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                                  class_mode='binary')

    # To visualize
    sample_training_images, _ = next(train_data_gen)

    # Create model
   # model = Sequential([
    #    Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
     #   MaxPooling2D(),
      #  Conv2D(32, 3, padding='same', activation='relu'),
       # MaxPooling2D(),
       # Conv2D(64, 3, padding='same', activation='relu'),
       # MaxPooling2D(),
        #Flatten(),
      #  Dense(512, activation='softmax'),
      #  Dense(10)

    #])
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))

    model.add(Flatten())
    model.add(Dense(64, activation='softmax'))
    model.add(Dense(10))

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    model.summary()

    history = model.fit_generator(
        train_data_gen,
        #steps_per_epoch=len(os.listdir("train_images/")) // batch_size,
        steps_per_epoch=29577 // batch_size,
        epochs=epochs,
        validation_data=val_data_gen,
        validation_steps=7677 // batch_size
    )
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss=history.history['loss']
    val_loss=history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.savefig("trainingPlot.jpg")

main()