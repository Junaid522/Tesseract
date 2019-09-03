import re
from time import sleep

import cv2
import pytesseract
from PIL import Image
import csv

def aviva_parser(receipt_path):
    img = cv2.imread(receipt_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    sleep(3)
    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 7)
    img = Image.open(receipt_path, 'r')
    data = pytesseract.image_to_string(img)
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)
    data = " ".join(data.split('\n'))
    data = data.replace("  ", " ")
    print(data)
    company_name = ''

    # return company_name


def rogers_parser(receipt_path):
    img = cv2.imread(receipt_path, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # sleep(3)
    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 7)
    img = Image.open(receipt_path, 'r')
    data = pytesseract.image_to_string(img)
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)
    # data = " ".join(data.split('\n'))
    data = data.replace("  ", " ")
    # print(data)
    lines = data.splitlines()
    # print(words)
    # print(lines)
    new_lines = []
    for i in range(0,len(lines)):
        if lines[i] == '' or lines[i] == ' ' or lines[i] == '   ':
            continue
        else:
            new_lines.append(lines[i])

    for i in range(0, len(new_lines)):
        # print(new_lines[i])
        # if new_lines[i].__contains__('C3 internet'):
        #     digits = new_lines[i].split()
        #     amount = ''.join(digits[5])
        #     print(amount)
        # if new_lines[i].__contains__('Account number'):
        #     digits = new_lines[i+1].split()
        #     amount = ''.join(digits[0])
        #     print(amount)

        if new_lines[i].__contains__('Bill date'):
            # print(new_lines[i])
            details = new_lines[i+1].split(' ')
            # account_number = details[0]
            # print(account_number)
            date = details[0:len(details)]
            billing_date = ''
            for d in date:
                billing_date += d + ' '
            print(billing_date)
        # if new_lines[i].__contains__('Bill date'):
        #     digits = new_lines[i+1].split()
        #     amount = ''.join(digits[0:3])
        #     print(amount)
        # if new_lines[i].__contains__('Rogers 12 Digit'):
        #     digits = new_lines[i].split()
        #     amount = ''.join(digits[0])
        #     print(amount)
        # if new_lines[i].__contains__('Required Payment Date: '):
        #     digits = new_lines[i].split()
        #     amount = ''.join(digits[3:6])
        #     print(amount)


def etr_407_parser(receipt_path):
    img = cv2.imread(receipt_path, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # sleep(3)
    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 7)
    img = Image.open(receipt_path, 'r')
    data = pytesseract.image_to_string(img)
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)
    # data = " ".join(data.split('\n'))
    data = data.replace("  ", " ")
    print(data)


def td_canada_parser(receipt_path):
    # img = cv2.imread(receipt_path, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # sleep(3)
    # img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    # th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 7)
    img = Image.open(receipt_path, 'r')
    data = pytesseract.image_to_string(img)
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)
    # data = " ".join(data.split('\n'))
    data = data.replace("  ", " ")
    # print(data)
    lines = data.splitlines()
    for i in range(0, len(lines)):
        if lines[i].__contains__('Bill date'):
            # str = ""
            # for ele in lines[i]:
            #     str += ele


            # print(lines[i])
            digits =lines[i+1].split()
            amount = ''.join(digits[1:4])
            print(amount)

        if lines[i].__contains__('Total amount due:'):
            # str = ""
            # for ele in lines[i]:
            #     str += ele
            # print(lines[i+2])

            digits =lines[i].split()
            amount = ''.join(digits[-1])
            print(amount)

        if lines[i].__contains__('Account number '):
            # str = ""
            # for ele in lines[i]:
            #     str += ele
            # print(lines[i])

            # digits =lines[i].split()
            # amount = digits[2:5]
            # str = ""
            # for ele in amount:
            #     str += ele
            digits = lines[i+1].split()

            amount = ''.join(digits[0:1])
            print(amount)

def main ():
    # receipt_path = 'splitted_pages/page1.jpg'
    receipt_path = 'splitted_pages/page5.jpg'
    # receipt_path = 'splitted_pages/page11.jpg'
    # receipt_path = 'splitted_pages/page13.jpg'
    # receipt_path = 'splitted_pages/page27.jpg'
    # receipt_path = 'splitted_pages/page21.jpg'
    # aviva_parser(receipt_path)
    # etr_407_parser(receipt_path)
    rogers_parser(receipt_path)
    # td_canada_parser(receipt_path)


if __name__ == '__main__':
    main()
