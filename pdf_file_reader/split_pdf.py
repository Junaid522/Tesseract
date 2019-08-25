import re

import cv2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path


def split_pdf(input_path, output_path):
    pages = convert_from_path(input_path, 300, fmt='jpg')
    page_count = 0
    for page in pages:
        page_count += 1
        print(f'splitting page # {page_count}')
        page.save(f'{output_path}/page{page_count}.jpg', 'JPEG')
        img = cv2.imread(f'{output_path}/page{page_count}.jpg')
        cv2.imwrite(f'{output_path}/page{page_count}.jpg', img)

    return page_count
