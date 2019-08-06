import re

import cv2
import pytesseract
from PIL import Image

from new_rec.split_pdf import split_pdf


# def get_company_name(receipt_path):
#     # img = cv2.imread(receipt_path, cv2.IMREAD_GRAYSCALE)
#
#     # img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
#     # th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 7)
#     img = Image.open(receipt_path, 'r')
#     data = pytesseract.image_to_string(img)
#     data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)
#
#     data = " ".join(data.split('\n'))
#     data = data.replace("  ", " ")
#     print(data)
#     company_name = ''
#
#     return company_name


def split_pdf_and_save_data_util(receipt_path):
    output_path = 'splitted_pages/'

    page_count = split_pdf(input_path=f'{receipt_path}', output_path=output_path)
    print(f'page_count: {page_count}')

    if page_count > 0:

        print(page_count)
    # company_name = get_company_name(f'{output_path}/page78.jpg')
    # print(f'company_name: {company_name}')
        # if company_name == 'SettlementReport':
        #     header = ['Company Name', 'Date', 'Total Margin Paid']
        #     with open(company_name + '.csv', 'w') as my_file:
        #         for item in header:
        #             my_file.write(str(item) + ', ')
        #         my_file.write('\n')
        #
        # elif company_name == 'Uber':
        #     header = ['Subtotal', 'HST', 'Total', 'Company Name', 'Date', 'Time']
        #     with open(company_name + '.csv', 'w') as my_file:
        #         for item in header:
        #             my_file.write(str(item) + ', ')
        #         my_file.write('\n')

        # for i in range(page_count):
        #     data = parse_reciept(company_name, f'{output_path}/page{i+1}.jpg')
        #     with open(company_name + '.csv', 'a') as my_file:
        #         for item in data:
        #             my_file.write(str(item) + ', ')
        #         my_file.write('\n')

        # print(type(my_file))
        # with open(company_name+'.csv', 'rb') as f:
        #     csv = CSV(document=File(f, company_name+'.csv'))
        #     csv.save()
        # my_file.close()
    else:
        print('No page found in pdf document')

    return output_path


def main():
    receipt_path = 'Receipts-July/300dip(2).pdf'
    split_pdf_and_save_data_util(receipt_path)


if __name__ == '__main__':

    main()
