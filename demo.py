import os
# import the necessary packages
from imutils import paths
import argparse
import cv2


def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()


if __name__ == "__main__":

    print('good:')
    good_folder = 'images/good'
    files = [file for file in os.listdir(good_folder) if file.endswith('.jpg')]
    for file in files:
        print(file)
        path = os.path.join(good_folder, file)
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        print(fm)

    print('bad:')
    bad_folder = 'images/bad'
    files = [file for file in os.listdir(bad_folder) if file.endswith('.jpg')]
    for file in files:
        print(file)
        path = os.path.join(bad_folder, file)
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        print(fm)
