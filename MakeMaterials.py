import cv2
import os
from random import *
from settings import *

# нужно прописать условие, чтобы рисовал П, потом О (500 на каждый)

img = cv2.imread(os.path.join("neurotesting/images", "blank.jpg"))
height, width = img.shape[:2]
for i in range(height):
    for j in range(width):
        if random() > 0.5:
            img[i, j] = [0, 0, 0]
        else:
            img[i, j] = [255, 255, 255]

cv2.imwrite(os.path.join("neurotesting/teaching_materials", "customized_image_" + str(1) + '.jpg'), img)
cv2.waitKey(0)
os.startfile("teaching_materials")