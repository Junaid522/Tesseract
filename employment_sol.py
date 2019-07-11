import pytesseract
import re
import cv2
import glob

data_list = []

img = cv2.imread('img/employment_solution/1.jpg')

data = pytesseract.image_to_string(img)
# print(data)
company = ''
total = 0
date = ''
gst = 0
deposit_no = 0
words = data.split()

# print(words)
# print(data)
if data.__contains__("The Employment Solution"):

    for i in range(len(words)):
        print(words[i])
        if words[i].__contains__("DATE"):
            date = words[i+1]

        if words[i].__contains__("PAID"):
            total = words[i+1]

        if words[i].__contains__("GST"):
            gst = words[i + 2]


        if words[i].__contains__("DEPOSIT"  and 'NO:'):
            deposit_no = words[i + 1]

print(date)
print(total)
print(gst)
print(deposit_no)