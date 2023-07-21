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

def sudoku_coz(sudoku):
    # Tahtanın boş hücrelerini bulma
    bos_hucre = bul_bos_hucre(sudoku)

    # Eğer boş hücre kalmadıysa Sudoku tamamlandı demektir
    if not bos_hucre:
        return True

    # Boş hücreleri doldurma denemeleri
    for sayi in range(1, 10):
        # Eğer sayı, boş hücreye yerleştirilebilirse
        if sayi_uygun(sudoku, bos_hucre, sayi):
            # Sayıyı yerleştir
            sudoku[bos_hucre[0]][bos_hucre[1]] = sayi

            # Sudoku çözümünü tekrar çağır
            if sudoku_coz(sudoku):
                return True

            # Yanlış bir yerleştirme yapıldıysa geri al
            sudoku[bos_hucre[0]][bos_hucre[1]] = 0

    # Sudoku çözülemedi
    return False


def bul_bos_hucre(sudoku):
    # Boş hücreleri bulma
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None


def sayi_uygun(sudoku, hucre, sayi):
    # Satırda sayı kontrolü
    for i in range(9):
        if sudoku[hucre[0]][i] == sayi:
            return False

    # Sütunda sayı kontrolü
    for i in range(9):
        if sudoku[i][hucre[1]] == sayi:
            return False

    # 3x3 kutuda sayı kontrolü
    baslangic_satir = (hucre[0] // 3) * 3
    baslangic_sutun = (hucre[1] // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[baslangic_satir + i][baslangic_sutun + j] == sayi:
                return False

    # Sayı uygun
    return True

# Görüntü'yü al
img_name = input("\nEnter the name of the sudoku picture:")
img = cv.imread("Sudoku/"+img_name)

# Sudoku'nun bulunduğu alanı bul ve kes
board, location = alanı_bul(img)
cv.imshow("Bulunan kutu", board)
cv.waitKey(250)

# Bulunan alandaki 9x9'luk büyük kutuyu 81 parçaya böl ve yeniden boyutlandır
input_size = 48
rois = kutulara_bol(board)
rois = np.array(rois).reshape(-1, input_size, input_size, 1)

# Model kutucuğu işler ve sayıyı döndürür
prediction = model_OCR.predict(rois)

classes = np.arange(0, 10)
predicted_numbers = []

for i in prediction: 
    index = (np.argmax(i))
    predicted_number = classes[index]
    predicted_numbers.append(predicted_number)

# Alınan 81 sayıyı 9x9'luk matrise dönüştürür 
board_num = np.array(predicted_numbers).astype('uint8').reshape(9, 9)

print("\nSudoku:")
print(board_num)

# Sudoku çözümünü çağırır
if sudoku_coz(board_num):
    print("\nSudoku çözümü:\nSudoku answer:")
    for i in range(9):
        for j in range(9):
            print(board_num[i][j], end=" ")
        print()
else:
    print("Bu Sudoku çözülemez.\nThis sudoku can't be solved")

secim = input("\nKapatmak için bir tuşa basın\nPress a key to close the app")

secim = exit()
