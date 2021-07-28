# Converting Image to sketch

import cv2 # import open cv


class Sketch():
    def read_image(self):
        get_image_file = input('Path or file name of the image: ')
        read_image = cv2.imread(get_image_file)
        cv2.imshow('scren', read_image)
        cv2.waitKey(0)

    



get_sketch = Sketch()
get_sketch.read_image()
