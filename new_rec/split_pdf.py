import re

import cv2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path


def get_company_name(receipt_path):
    # img = cv2.imread(receipt_path, cv2.IMREAD_GRAYSCALE)

    # img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    # th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 7)
    img = Image.open(receipt_path, 'r')
    data = pytesseract.image_to_string(img)
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)

    data = " ".join(data.split('\n'))

    data = data.replace("  ", " ")
    # print(data)
    company_name = ''
    if data.__contains__('Aviva General Insurance Company'):
        print('AVIVA:  ',data)
    if data.__contains__('Insurance Coverages : '):
        print('Insurance Coverages : ',data)
    if data.__contains__('ROGERS') or data.__contains__('My Rogers at'):
        print('ROGERS:  ',data)
    if data.__contains__('407 ETR') or data.__contains__('Rogers Cup'):
        print('407 ETR:  ',data)
    if data.__contains__(' TD Rewards ') or data.__contains__(' TD ') or data.__contains__('TD Canada Trust') or \
            data.__contains__('TD BUSINESS TRAVEL VISA') or data.__contains__('TD Bank') or \
            data.__contains__('THE TORONTODOMINION BANK') or data.__contains__('THE TORONTO-DOMINION BANK'):
        print('TD:    ',data)
    if data.__contains__('Canada Revenue'):
        print('CANADA REVENUE:   ',data)

    return company_name


def split_pdf(input_path, output_path):
    pages = convert_from_path(input_path, 300, fmt='jpg')
    page_count = 0
    for page in pages:
        page_count += 1
        print(f'splitting page # {page_count}')
        page.save(f'{output_path}/page{page_count}.jpg', 'JPEG')
        img = cv2.imread(f'{output_path}/page{page_count}.jpg')
        (h, w) = img.shape[:2]
        # calculate the center of the image
        center = (w / 2, h / 2)

        angle90 = 90
        angle180 = 180
        angle270 = 270

        scale = 1.0
        M = cv2.getRotationMatrix2D(center, angle180, scale)
        img = cv2.warpAffine(img, M, (w, h))
        cv2.imwrite(f'{output_path}/page{page_count}.jpg', img)
        company_game = get_company_name(f'{output_path}/page{page_count}.jpg')
        # page.save(f'page{page_count}.png', 'PNG')

    return page_count
