import pytesseract
import re
import cv2
import re
import glob

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

data_list = []

img = cv2.imread('img/300_dpi/invoice/air_canada.jpg')
# img = cv2.resize(img, None, fx=1.5, fy=2.0, interpolation=cv2.INTER_CUBIC)
# img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# img = cv2.resize(img, (1030, 2048))
# cv2.imshow('img', img)
# cv2.waitKey(0)

data = pytesseract.image_to_string(img)

data = re.sub(r'([\§\|\-\|\—])', '', data)
print(data)