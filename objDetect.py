import cv2.cv as cv
import cv2 as cv2
import numpy as np
import time
import RPi.GPIO as GPIO

Hmin = 42
Hmax = 92
Smin = 62
Smax = 255
Vmin = 63
Vmax = 235

rangeMin = np.array([Hmin, Smin, Vmin], np.uint8)
rangeMax = np.array([Hmax, Smax, Vmax], np.uint8)

minArea = 50

cv.NamedWindow("Video")

capture = cv2.VideoCapture(0)

width = 160
height = 120

if capture.isOpened():
	capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, width)
	capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, height)
