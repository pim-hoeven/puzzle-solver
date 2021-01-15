# pylint: disable=no-member
import cv2
import matplotlib.pyplot as plt
import numpy as np


class Image(np.ndarray):
    def __new__(cls, input_array):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        # Finally, we must return the newly created object:
        return obj

    def __repr__(self):
        return f"Image with pixel shape {self.shape}"

    def pipe(self, f, *args, show_result=False, **kwargs):
        """Add pandas pipe functionality"""
        result = Image(f(self, *args, **kwargs))

        if show_result:
            result.show()
        return result

    def show(self):
        """Show image as a matrix plot"""
        plt.matshow(self, cmap="Greys_r")

    @property
    def values(self):
        """Get underlying array"""
        return np.array(self)


def read_img(path, grayscale=True):
    if grayscale:
        return Image(cv2.imread(path, cv2.IMREAD_GRAYSCALE))
    return Image(cv2.imread(path, cv2.IMREAD_GRAYSCALE))


def blur(img: Image, kernel: int = 5):
    if not kernel % 2:
        raise ValueError(f"Kernel must be odd, got {kernel}")

    return cv2.GaussianBlur(img.copy(), (kernel, kernel), 0)


def threshold(img: Image, block_size=11, constant=3):
    return cv2.adaptiveThreshold(
        img,
        maxValue=255,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType=cv2.THRESH_BINARY,
        blockSize=block_size,
        C=constant,
    )


def invert(img: Image):
    return cv2.bitwise_not(img, img)


def dilute(img: Image, kernel=None, iterations=1):
    if kernel is None:
        kernel = np.array([[0.0, 1.0, 0.0], [1.0, 1.0, 1.0], [0.0, 1.0, 0.0]], np.uint8)
    return cv2.dilate(img, kernel, iterations=iterations)


def canny(img, threshold1=90, threshold2=150):
    return cv2.Canny(img, threshold1=threshold1, threshold2=threshold2, apertureSize=3)


def erode(img, kernel=None, iterations=1):
    if kernel is None:
        kernel = np.ones((3, 3), np.uint8)
    return cv2.erode(img, kernel=kernel, iterations=iterations)
