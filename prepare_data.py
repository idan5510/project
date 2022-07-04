import os
import shutil
from glob import glob

import numpy as np

import OPTIONS


def prepare_data():
    data_dir = OPTIONS.DATA_DIR
    dataset_dir = OPTIONS.DATA_DIR / 'dataset'
    train_size = OPTIONS.TRAIN_SIZE
    test_size = OPTIONS.TEST_SIZE

    print('Preparing data')

    train_dir = data_dir / 'split' / 'train'
    test_dir = data_dir / 'split' / 'test'
    val_dir = data_dir / 'split' / 'val'

    classes = os.listdir(dataset_dir)
    for cls in classes:
        os.makedirs(train_dir / cls, exist_ok=True)
        os.makedirs(test_dir / cls, exist_ok=True)
        os.makedirs(val_dir / cls, exist_ok=True)

    for cls in classes:
        images = glob(str(dataset_dir / cls / '*.png'))
        train, test, val = np.split(np.array(images), [int(len(images)*train_size), int(len(images)*(train_size + test_size))])

        for img in train:
            shutil.copy(img, train_dir / cls)

        for img in test:
            shutil.copy(img, test_dir / cls)

        for img in val:
            shutil.copy(img, val_dir / cls)

    print('Finished preparing data')
