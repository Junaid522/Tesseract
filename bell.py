import cv2
import re
import scanner
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

data_list = []

# scanner.main('odd.png')
img = cv2.imread('odd.png')



data = pytesseract.image_to_string(img)
# data = pytesseract.image_to_string(Image.open('img/bell/4.jpg'))
print(data)
data = re.sub(r'([\|\-\|\—])', '', data)

# data =" ".join(data.split('\n'))
data = data.replace("  ", " ")
# print(data)
company = ''
total = 0
date = ''
gst = 0
hst = 0
words = data.split('\n')

# print(words)



# print(words)
# print(data)
if data.__contains__("Mobility" and 'bell'):

    for i in range(len(words)):
        # words[i].replace('  ', ' ')

        if words[i].__contains__("Total current charges including taxes"):
            total = words[i].replace("Total current charges including taxes", '').strip()
            # if

        if words[i].__contains__("Bill Date"):
            if "Next Bill Date" not in words[i]:
                date = words[i].replace("Bill Date", '').strip()

        if words[i].__contains__("Total GST included in this bill"):
            gst = words[i].replace("Total GST included in this bill", '').strip()

        if words[i].__contains__("Total HST included in this bill"):
            hst = words[i].replace("Total HST included in this bill", '').strip()

    print("total ",total)
    print("date ",date)
    print("gst ",gst)
    print("hst ",hst)
