import cv2 as cv
import numpy as np
from tensorflow.keras.models import load_model
import imutils

model_OCR = load_model('model-OCR.h5')

def perspektif_al(img, location, height = 900, width = 900):

    # Bölgenin konumunu alır ve persfektif dönüşümünü uygular.

    pts1 = np.float32([location[0], location[3], location[1], location[2]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    matrix = cv.getPerspectiveTransform(pts1, pts2)
    result = cv.warpPerspective(img, matrix, (width, height))

    return result


def alanı_bul(img):

    # Aldığı fotoğraftan sudoku alanını bulur.
     
    # Alınan fotoğraflarda çizgi tespiti için gerekli filtrasyonlar.
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    bfilter = cv.bilateralFilter(gray, 13, 20, 20)
    edged = cv.Canny(bfilter, 30, 180)
    
    
    # Filtrasyonlar sonucu sürekli çizgi tespiti yapar.
    keypoints = cv.findContours(edged.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours  = imutils.grab_contours(keypoints)

    newimg = cv.drawContours(img.copy(), contours, -1, (0, 255, 0), 3)

    contours = sorted(contours, key=cv.contourArea, reverse=True)[:15]
    location = None
    
    # Diktörgen arar.
    for contour in contours:
        approx = cv.approxPolyDP(contour, 15, True)
        if len(approx) == 4:
            location = approx
            break

    result = perspektif_al(img, location)
    return result, location


def kutulara_bol(board):

    # 9x9'luk matrisi 81 adet kutucuğa böler.

    board = cv.cvtColor(board, cv.COLOR_BGR2GRAY)
    rows = np.vsplit(board,9) # yatay bölme
    boxes = []

    for r in rows:
        cols = np.hsplit(r,9) # dikey bölme
        for box in cols:
            box = cv.resize(box, (input_size, input_size))/255.0
            cv.imshow("Bölünen kutucuk", box)
            cv.waitKey(50)
            boxes.append(box)

    cv.destroyAllWindows()
    return boxes
