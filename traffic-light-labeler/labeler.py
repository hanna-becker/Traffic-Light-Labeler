from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np
from user_input import get_user_input

IMG_DIR = 'images'
LABELED_DATA_FILE = "labeled_data.csv"


def _print_finish_msg():
    print("\n******************************")
    print("Finished labeling all images!")
    print("******************************\n")


def run():
    labeled_data_file = open(LABELED_DATA_FILE, "a")
    img_paths = Path(IMG_DIR).glob('**/*.jpg')
    tl_state = None
    plt.ion()
    plot = plt.imshow(np.zeros((600, 800)))
    for img_path in img_paths:
        path = str(img_path)

        # check if image has already been labeled
        if path in open(LABELED_DATA_FILE).read():
            continue

        image = cv2.imread(path)
        plot.set_data(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.pause(0.05)

        tl_state = get_user_input()
        if tl_state == "p":
            break
        labeled_data_file.write("%s, %s\n" % (path, tl_state))

    labeled_data_file.close()

    if tl_state != "p":
        _print_finish_msg()
