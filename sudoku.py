import cv2 as cv
import numpy as np
from tensorflow.keras.models import load_model
import imutils

model_OCR = load_model('model-OCR.h5')

