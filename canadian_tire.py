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

img = cv2.imread('img/300_dpi/receipt/tire_2.jpg')
img = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.waitKey(0)

data = pytesseract.image_to_string(img)

# data = re.sub(r'([\§\|\|\—])', '', data)
# print(data)


# data =" ".join(data.split('\n'))
# data = data.replace("  ", " ")
# print(data)
company = ''
invoice_number = ''
total = 0
date = ''
tax = 0
print(data)
if data.__contains__("CANADIAN" or "TIRE"):
    company = 'CANADIAN TIRE'
    words = data.split()

    for i in range(len(words)):
        print(words[i])
        if words[i].__contains__('Invoice'):
            invoice_number = words[i+2]
        if words[i].__contains__('TOTAL') and words[i+3].__contains__('Purchase'):
            total = words[i+2]
        if words[i].__contains__('FUEL') and words[i+1].__contains__("$"):
            tax = words[i+2]


    print("invoice_number",invoice_number)
    print("total",total)
    print("tax ", tax)




