# Converting Image to sketch

import cv2 # import open cv


class Sketch():
    def read_image(self):
        get_image_file = input('Path or file name of the image: ')
        read_image = cv2.imread(get_image_file)
        cv2.imshow('screen', read_image)
        cv2.waitKey(0)

        
        # creating a gray image using cv2 library
        gray_image = cv2.cvtColor(read_image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('new screen', gray_image)
        cv2.waitKey(0)

        # create inverted image from grayscale
        inverted_image = 255 - gray_image
        cv2.imshow('Inverted', inverted_image)
        cv2.waitKey()

        # Gaussian Function to blur image
        



get_sketch = Sketch()
get_sketch.read_image()
