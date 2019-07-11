import pytesseract
import re
import cv2
import glob



# img = cv2.imread('img/300_dpi/invoice/sask_power.jpg')
img = cv2.imread('img/sask_power/1.jpg')
# img = cv2.imread('img/sask_power/2.jpg')
# img = cv2.imread('img/sask_power/3.jpg')
# img = cv2.imread('img/sask_power/4.jpg')
# img = cv2.imread('img/sask_power/5.jpg')
# img = cv2.imread('img/sask_power/6.jpg')
# img = cv2.imread('img/sask_power/7.jpg')
# img = cv2.imread('img/sask_power/8.jpg')
# img = cv2.imread('img/sask_power/9.jpg')
# img = cv2.imread('img/sask_power/10.jpg')

data = pytesseract.image_to_string(img)

company = ""
total = 0
tax = 0
date = ''
invoice_number = ''

# print(data)

words = data.split()
if data.__contains__("SaskPower"):

    company = "SaskPower"
    # print(data)

    for i in range(len(words)):
        # print(words[i])

        if words[i].__contains__('automatic') and words[i+1].__contains__('payment') and words[i-1].__contains__('by'):
            total = words[i+2]

        if words[i].__contains__("Invoice"):
            invoice_number = words[i+1]
        if words[i].__contains__("Tax") and words[i-1].__contains__("Surcharge"):
           tax = words[i+1]
        if words[i].__contains__("Issued"):
           date = words[i+1]+"/"+words[i+2].replace(',', '')+"/"+words[i+3]


        # print(words[i])
    print(invoice_number)
    print(tax)
    print(company)
    print(total, "total")
    print(date, "date")

