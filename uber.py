import pytesseract
import re
import cv2
import glob

data_list = []
# img = cv2.imread('img/uber/2.jpg')

for filename in glob.glob('img/uber/3.jpg'): #assuming gif
    data_dic = {}
    img = cv2.imread(filename)


    # img = cv2.resize(img,(600, 600))
    # cv2.imshow("im", img)
    # cv2.waitKey(0)

    data = pytesseract.image_to_string(img)
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])','', data)
    # print(data)

    time = ''
    if data.__contains__('Uber'):



        # name_date = data.split('\n',1)
        # data = name_date[1]
        # name_date = name_date[0]
        # name_date = name_date.split(' ', 1)
        # data_dic["Company"] =name_date[0]
        # date = name_date[1].replace(".", '',1)
        # data_dic["Date"] = date


        date=data.split('Uber')
        date = date[1].split('Thanks')
        date = date[0].strip()
        # print(date)

        words = data.split()


        for i in range(len(words)):

            print(words[i])

            if words[i].__contains__("Total"):
                data_dic['Total'] = words[i+1]

            if words[i].__contains__("HST"):
                data_dic['HST'] = words[i+1]

            if words[i].__contains__("Subtotal"):
                data_dic['Subtotal'] = words[i + 1]

            # time = re.findall(r'am', words[i])
            if words[i].__contains__("am"):
                time = words[i]

            if words[i].__contains__("pm"):
                time = words[i]

        data_dic["Time"] = time

    data_list.append(data_dic)

# with open('uber_data.csv', 'w') as f:
#     csv_linr = "Date,Time,Company,Subtotal,HST,Total\n"
#     f.write(csv_linr)
#     for i in data_list:
#         csv_var = i['Date'] + "," + i['Time'] + "," + i['Company'] + ',' + i['Subtotal'] + "," + i['HST'] + i['Total'] + "," + "\n"
#         f.write(csv_var)


print(data_list)





