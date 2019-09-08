import sys
import cv2
import numpy as np

if __name__ == '__main__':
    imPath = sys.argv[1]
    source_image = cv2.imread(imPath)
    frame_hsv = cv2.cvtColor(source_image, cv2.COLOR_BGR2HSV)
    channels = cv2.split(frame_hsv)
    brightness = np.average(channels[2])
    # Can take decision based on brightness
    # Brighness varies from 0 to 255 (128 being middle)
    brightness_variation = (128 - abs(128-brightness))

    sharpness = cv2.Laplacian(source_image, cv2.CV_64F).var()
    # Can take decision based on sharpness
    sharpness_scaled = sharpness/10

    image_size = np.size(source_image)
    image_size_scaled = image_size/10000
    # Can take decision based on image_size

    print("\nBrightness: {0}\nSharpness: {1}\nSize: {2}\n".format(brightness_variation, sharpness_scaled, image_size_scaled))
    # Coefficients to change with testing (Assing more weight to sharpness of image)
    sharpness_coefficent, size_coefficent, brightness_coefficent = 0.50, 0.20, 0.30

    score = (sharpness_coefficent * sharpness_scaled) + (size_coefficent * image_size_scaled) - (brightness_coefficent * brightness_variation)
    print("Score {}".format(int(score)))

