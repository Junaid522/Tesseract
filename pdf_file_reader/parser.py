import re

import cv2
import pytesseract
from PIL import Image

from pdf_reader.split_pdf import split_pdf


def split_pdf_and_save_data_util(receipt_path):
    output_path = 'splitted_pages/'

    page_count = split_pdf(input_path=f'{receipt_path}', output_path=output_path)
    print(f'page_count: {page_count}')

    if page_count > 0:
        print(page_count)
    else:
        print('No page found in pdf document')

    return output_path


def main():
    receipt_path = 'file1.pdf'
    split_pdf_and_save_data_util(receipt_path)


if __name__ == '__main__':

    main()
