import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import keras

import OPTIONS


def test_model():
    try:
        model = keras.models.load_model('saved_model.h5')
    except Exception as e:
        print('Cant load the saved_model.h5 file')
        return

    data = __get_data()
    class_names = ['car', 'non-car']

    loss, accuracy = model.evaluate(data)

    print('Test loss: ' + str(loss))
    print('Test accuracy: ' + str(accuracy))

    data = __get_data(batch_size=None)
    # plt.figure(figsize=(10, 10))
    count = 0
    for i, (x, y) in enumerate(data):
        if count >= 10:
            return

        img_arr = tf.expand_dims(x, 0)

        predictions = model.predict(img_arr)

        score = tf.nn.softmax(predictions[0])
        percent = int(100 * np.max(score))
        title = "{} - {} %".format(class_names[np.argmax(score)], percent)

        plt.imshow(x.numpy().astype(int))
        plt.title(title)
        plt.axis("off")
        plt.show()

        count += 1

def __get_data(batch_size=32):
    data_dir = OPTIONS.DATA_DIR
    image_height = OPTIONS.IMAGE_HEIGHT
    image_width = OPTIONS.IMAGE_WIDTH

    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir / 'split' / 'test',
        image_size=(image_height, image_width),
        batch_size=batch_size)

    return test_ds
