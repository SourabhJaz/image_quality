import sys
import cv2
import numpy as np

if __name__ == '__main__':
    image_name = "test17.jpeg"
    source_image = cv2.imread(image_name)
    frame_hsv = cv2.cvtColor(source_image, cv2.COLOR_BGR2HSV)
    channels = cv2.split(frame_hsv)
    brightness = np.average(channels[2])
    # Can take decision based on brightness
    sharpness = cv2.Laplacian(source_image, cv2.CV_64F).var()
    # Can take decision based on sharpness
    image_size = np.size(source_image)
    # Can take decision based on image_size
    print("\nBrightness: {0}\nSharpness: {1}\nSize: {2}\n".format(brightness, sharpness, image_size))
    # Coefficients to change with testing (Assing more weight to sharpness of image)
    sharpness_coefficent, size_coefficent, brightness_coefficent = 0.50, 0.25, 0.25
    # Brighness varies from 0 to 255 (128 being middle)
    brightness_variation = abs(128-brightness)
    score = (sharpness_coefficent * sharpness) + (size_coefficent * image_size) + (brightness_coefficent * brightness_variation)
    print("Score {}".format(score))

