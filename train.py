import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import OPTIONS


def train_model():
    epochs = OPTIONS.EPOCHS

    print('Training')

    model = __get_model()
    train_ds, validation_ds = __get_data()

    history = model.fit(train_ds, validation_data=validation_ds, epochs=epochs)
    model.save('saved_model.h5')

    print('Done training')
    print('Saved model to saved_model.h5 file')

    accuracy = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(epochs)
    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, accuracy, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

def __get_model():
    image_height = OPTIONS.IMAGE_HEIGHT
    image_width = OPTIONS.IMAGE_WIDTH
    num_classes = OPTIONS.NUM_CLASSES

    model = Sequential([
        layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(image_height, image_width, 3)),
        layers.Conv2D(16, 3, padding='same', activation='sigmoid'),
        layers.Dropout(0.25),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation='sigmoid'),
        layers.Dropout(0.25),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='sigmoid'),
        layers.Dropout(0.25),
        layers.MaxPooling2D(),
        layers.Conv2D(128, 3, activation='sigmoid'),
        layers.Dropout(0.25),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='Adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                  metrics=['accuracy'])
    model.summary()

    return model

def __get_data():
    data_dir = OPTIONS.DATA_DIR
    image_height = OPTIONS.IMAGE_HEIGHT
    image_width = OPTIONS.IMAGE_WIDTH
    batch_size = OPTIONS.BATCH_SIZE

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir / 'split' / 'train',
        image_size=(image_height, image_width),
        batch_size=batch_size)
    validation_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir / 'split' / 'val',
        image_size=(image_height, image_width),
        batch_size=batch_size)

    return train_ds, validation_ds
