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

img = cv2.imread('img/300_dpi/invoice/dxphrl.jpg')

data = pytesseract.image_to_string(img)

data = re.sub(r'([\§\|\-\|\—])', '', data)
print(data)

company = ''
total = 0
date = ''
tax = 0
invoice_number = ''

if data.__contains__("Booking Reference DXPHRL"):

    words = data.split()

# print(words)




    for i in range(len(words)):
        if words[i-1].__contains__('Incl') and words[i].__contains__('taxes'):
            total = words[i+1]

        if words[i].__contains__('CAD') :
            tax = words[i+1]

        if words[i].__contains__('Invoice') and words[i+2].__contains__('Customer'):
            invoice_number = words[i + 1]

        if words[i].__contains__('Date'):
            date = words[i + 1]

        if words[i].__contains__('Airline'):
            company = words[i+1] +" "+ words[i+2]

        print(words[i])

    print(tax)
    print(total)
    print(invoice_number)
    print(date)
    print(company)
