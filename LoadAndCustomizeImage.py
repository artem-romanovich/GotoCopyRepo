import cv2
import os
import numpy
from settings import *


def load_images():
    images = []
    for filename in os.listdir("images"):
        img = cv2.imread(os.path.join("images", filename)) #!!!
        if img is not None:
            images.append(img)
    return images


def get_avg_color(current_img):
    avg_color_per_row = numpy.average(current_img, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    return sum(avg_color) / 3 - DELTA_COLOR


def do_black_white(height, width, color_compare, img):
    for i in range(height):
        for j in range(width):
            if numpy.all(img[i, j] <= [color_compare, color_compare, color_compare]):
                img[i, j] = [0, 0, 0] #!!!
            else:
                img[i, j] = [255, 255, 255]


# ----------------------------------------------------------------------------------------------------------------------
images = load_images()

for n in range(len(images)):
    current_img = images[n]

    color_compare = get_avg_color(current_img)
    height, width = current_img.shape[:2] #!!!
    img = cv2.resize(current_img, (width, height))

    do_black_white(height, width, color_compare, img)

    cv2.imwrite(os.path.join("received_text", "customized_image_" + str(n) + '.jpg'), img)
    cv2.waitKey(0)
    os.startfile("received_text")
