from time import sleep

import imutils
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

def rotate_image(img, angle):

    rotated = imutils.rotate(img, angle)
    return rotated


def co_op_reader():
    data_dict = {}
    data_list = []

    # config = ('-l eng --oem 1 --psm 3')

    img = cv2.imread('co-op/img20190502_19290242-10.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('co-op/img20190502_19290242-08.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('co-op/img20190502_19290242-09.jpg', cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 103, 5)
    # cv2.imshow('rotated', th3)
    # cv2.waitKey(0)

    data = pytesseract.image_to_string(th3)

    data = re.sub(r'([\§\|\-\|\—])', '', data)
    # print(data)

    str_lists = data.splitlines()
    company_name = ''
    gst_included = ''
    total = ''
    rec_no = ''

    for str in str_lists:

        if str.__contains__('end Coop') or str.__contains__('emd Coop'):
            company_name = 'Riverbend Coop'
        elif str.__contains__('Pumps]'):
            gst_included = str
        elif str.__contains__('Total') or str.__contains__("Tota' "):
            total = str
        elif str.__contains__('Receipt#'):
            rec_no = str
        else:
            continue

    # print('Company Name: ' ,company_name)
    # print('GST :',gst_included)
    # print('Total :',total)
    # print('Receipt no. :',rec_no)
    gst = ''
    total_amount = ''
    receipt_no = ''
    gst_str_list = gst_included.split(' ')
    total_str_list = total.split(' ')
    rec_str_list = rec_no.split(' ')

    gst = gst_str_list[-1]

    total_amount = total_str_list[-1]

    receipt_no = rec_str_list[-1]

    print('Company Name: ', company_name)
    print('GST :', float(gst))
    print('Total :', float(total_amount))
    print('Receipt no. :', int(receipt_no))


def uber_reader():
    print("In uber parser")
    # img = cv2.imread(receipt_path)
    # data = pytesseract.image_to_string(img)
    # print(data)

    img = cv2.imread('img/uber/3.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('co-op/img20190502_19290242-08.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('co-op/img20190502_19290242-09.jpg', cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 103, 5)
    # cv2.imshow('rotated', th3)
    # cv2.waitKey(0)

    data = pytesseract.image_to_string(th3)

    # data = re.sub(r'([\§\|\-\|\—])', '', data)
    # data = pytesseract.image_to_string(Image.open('img/uber/1.jpg'))
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)



    time = ''
    company = 'Uber'
    date = ''
    subtotal = 0
    total = 0
    hst = 0

    if data.__contains__('Uber'):

        date = data.split('Uber')
        date = date[1].split('\n')
        date = date[0].strip('\n')
        # print(date)

        words = data.splitlines()
        # print(words)

        for w in words:
            if w.__contains__("Total"):
                total = w
            if w.__contains__("HST"):
                hst = w
            if w.__contains__("Subtotal"):
                subtotal = w
            if w.__contains__("am"):
                time = w

            if w.__contains__("pm"):
                time = w
        total = total.split(' ')
        hst = hst.split(' ')
        subtotal = subtotal.split(' ')
        time = time.split(' ')

        total = total[-1]
        hst = hst[-1]
        subtotal = subtotal[-1]
        time = time[0]
        #
        # for i in range(len(words)):
        #
        #     if words[i].__contains__("Total"):
        #         total = words[i + 1]
        #
        #     if words[i].__contains__("HST"):
        #         hst = words[i + 1]
        #
        #     if words[i].__contains__("Subtotal"):
        #         if words[i + 1] != ':' or words[i + 1] != ';':
        #             subtotal = words[i + 1]
        #         else:
        #             subtotal = words[i + 2]
        #
        #
        #     # time = re.findall(r'am', words[i])
        #     if words[i].__contains__("am"):
        #         time = words[i]
        #
        #     if words[i].__contains__("pm"):
        #         time = words[i]

    data = [subtotal, hst, total, company, date, time]

    print(data)
    return data

def sask_power_reader():

    print("In sask power parser")
    # img = cv2.imread(receipt_path)
    # data = pytesseract.image_to_string(img)
    # print(data)

    img = cv2.imread('img/sask_power/3.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('co-op/img20190502_19290242-08.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('co-op/img20190502_19290242-09.jpg', cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 103, 5)
    # cv2.imshow('rotated', th3)
    # cv2.waitKey(0)

    data = pytesseract.image_to_string(th3)

    # data = re.sub(r'([\§\|\-\|\—])', '', data)
    # data = pytesseract.image_to_string(Image.open('img/uber/1.jpg'))
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)
    # img = cv2.imread('img/sask_power/1.jpg')
    # img = cv2.imread('img/sask_power/2.jpg')
    # img = cv2.imread('img/sask_power/3.jpg')
    # img = cv2.imread('img/sask_power/4.jpg')
    # img = cv2.imread('img/sask_power/5.jpg')
    # img = cv2.imread('img/sask_power/6.jpg')
    # img = cv2.imread('img/sask_power/7.jpg')
    # img = cv2.imread('img/sask_power/8.jpg')
    # img = cv2.imread('img/sask_power/9.jpg')
    # img = cv2.imread('img/sask_power/10.jpg')

    # data = pytesseract.image_to_string(img)

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

            if words[i].__contains__('automatic') and words[i + 1].__contains__('payment') and words[i - 1].__contains__('by'):
                total = words[i + 2]

            if words[i].__contains__("Invoice"):
                invoice_number = words[i + 1]
            if words[i].__contains__("Tax") and words[i - 1].__contains__("Surcharge"):
                tax = words[i + 1]
            if words[i].__contains__("Issued"):
                date = words[i + 1] + "/" + words[i + 2].replace(',', '') + "/" + words[i + 3]

            # print(words[i])
        print(invoice_number)
        print(tax)
        print(company)
        print(total, "total")
        print(date, "date")


def amex_reader():

    print("In american express parser")
    # img = cv2.imread(receipt_path)
    # data = pytesseract.image_to_string(img)
    # print(data)

    img = cv2.imread('amex/dxphrl.jpg', cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 103, 5)
    # cv2.imshow('rotated', th3)
    # cv2.waitKey(0)

    data = pytesseract.image_to_string(th3)

    # data = re.sub(r'([\§\|\-\|\—])', '', data)
    # data = pytesseract.image_to_string(Image.open('img/uber/1.jpg'))
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)
    # img = cv2.imread('img/sask_power/1.jpg')
    # img = cv2.imread('img/sask_power/2.jpg')
    # img = cv2.imread('img/sask_power/3.jpg')
    # img = cv2.imread('img/sask_power/4.jpg')
    # img = cv2.imread('img/sask_power/5.jpg')
    # img = cv2.imread('img/sask_power/6.jpg')
    # img = cv2.imread('img/sask_power/7.jpg')
    # img = cv2.imread('img/sask_power/8.jpg')
    # img = cv2.imread('img/sask_power/9.jpg')
    # img = cv2.imread('img/sask_power/10.jpg')

    # data = pytesseract.image_to_string(img)

    company = "Amex Canada"
    invoice_number = ""
    invoice_date = ""
    gst = ""
    total = ""
    # print(data)

    lines = data.splitlines()
    for l in lines:
        if l.__contains__("invoice ") or l.__contains__("Invoice "):
            invoice_number = l
        if l.__contains__("Invoice Date"):
            invoice_date = l
        if l.__contains__("G.S.T/H.S.T Amount"):
            gst = l
        if l.__contains__("Total Amount"):
            total = l

    invoice_number = invoice_number[5].split(" ")
    invoice_date = invoice_date.split(" ")
    gst = gst.split(" ")
    total = total.split(" ")

    invoice_number = invoice_number[-1]
    invoice_date = invoice_date[-1]
    gst = gst[-1]
    total = total[-1]

    data = [invoice_number, invoice_date, gst, total]
    print(data)





    # if data.__contains__("SaskPower"):
    #
    #     company = "SaskPower"
    #     # print(data)
    #
    #     for i in range(len(words)):
    #         # print(words[i])
    #
    #         if words[i].__contains__('automatic') and words[i + 1].__contains__('payment') and words[i - 1].__contains__('by'):
    #             total = words[i + 2]
    #
    #         if words[i].__contains__("Invoice"):
    #             invoice_number = words[i + 1]
    #         if words[i].__contains__("Tax") and words[i - 1].__contains__("Surcharge"):
    #             tax = words[i + 1]
    #         if words[i].__contains__("Issued"):
    #             date = words[i + 1] + "/" + words[i + 2].replace(',', '') + "/" + words[i + 3]
    #
    #         # print(words[i])
    #     print(invoice_number)
    #     print(tax)
    #     print(company)
    #     print(total, "total")
    #     print(date, "date")

def settlement_parser():

    print("In settlement report parser")
    img = cv2.imread('img/settlement_report/page12.jpg', cv2.IMREAD_GRAYSCALE)
    sleep(3)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    (h, w) = img.shape[:2]
    # calculate the center of the image
    center = (w / 2, h / 2)

    angle90 = 90
    angle180 = 180
    angle270 = 270


    scale = 1.0
    M = cv2.getRotationMatrix2D(center, angle180, scale)
    img = cv2.warpAffine(img, M, (w, h))
    # img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    # th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 103, 5)
    # cv2.imshow('the', img)
    # cv2.waitKey(0)

    # data = pytesseract.image_to_string(th3)
    data = pytesseract.image_to_string(img)

    data = re.sub(r'([\§\|\-\|\—])', '', data)
    print(data)

    str_lists = data.splitlines()
    company_name = ''
    date = ''
    total_margin_paid = ''

    for str in str_lists:

        if str.__contains__('SETTLEMENT REPORT'):
            company_name = 'SETTLEMENT REPORT'
        elif str.__contains__(' a.m.') or str.__contains__(' a.m,') or str.__contains__(' p.m,') or str.__contains__(' p.m.'):
            date = str.replace(',', '.')
        elif str.__contains__(' Margin Paid'):
            total_margin_paid = str.replace(',', '.')
        # elif str.__contains__('Total') or str.__contains__("Tota' "):
        #     total = str
        # elif str.__contains__('Receipt#'):
        #     rec_no = str
        # else:
        #     continue


    # gst_str_list = gst_included.split(' ')
    total_margin_paid = total_margin_paid.split(' ')
    # rec_str_list = rec_no.split(' ')
    #
    # gst = gst_str_list[-1]
    #
    total_margin_paid = total_margin_paid[-1]
    #
    # receipt_no = rec_str_list[-1]
    #
    # data = [company_name, float(gst), float(total_amount), int(receipt_no)]
    data = [company_name, date, total_margin_paid]
    print(data)

def bell_reader():
    print("In bell parser")

    img = cv2.imread('img/bell/6.jpg', cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 103, 5)

    data = pytesseract.image_to_string(th3)
    data = re.sub(r'([\\\+\*\?\[\^\]\(\)\{\}\!\<\>\|\-\|])', '', data)

    # data =" ".join(data.split('\n'))
    data = data.replace("  ", " ")
    print(data)
    company = 'Bell'
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

            if words[i].__contains__("Total current charges Including taxes"):
                total = words[i].replace("Total current charges Including taxes", '').strip()
                # if

            if words[i].__contains__("Bill Date"):
                if "Next Bill Date" not in words[i]:
                    date = words[i].replace("Bill Date", '').strip()

            if words[i].__contains__("Total GST included in this bill"):
                gst = words[i].replace("Total GST included in this bill", '').strip()

            if words[i].__contains__("Total HST included in this bill"):
                hst = words[i].replace("Total HST included in this bill", '').strip()

        # print("total ", total)
        # print("date ", date)
        # print("gst ", gst)
        # print("hst ", hst)

        data = [company, total, gst, hst, date]
        print(data)
        # return data


def tax_payer():
    print("In tax_payer parser")

    img = cv2.imread('tax-payer/A-J.png', cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 103, 5)
    # cv2.imshow('th3', th3)
    # cv2.waitKey(0)

    data = pytesseract.image_to_string(th3)
    data = re.sub(r'([\§\|\-\|\—])', '', data)

    # data =" ".join(data.split('\n'))
    data = data.replace("  ", " ")
    data = data.replace(".", "")
    print(data)
    lines = data.splitlines()
    company_name = ""
    business_number = ""
    year = ""
    dict_data = {}

    header = ['Company Name', 'Business Number', 'Year']
    with open('tax_payer.csv', 'w') as f:
        for item in header:
            f.write(str(item) + ', ')
        f.write('\n')
    for l in lines:
        words = l.split(' ')
        for w in range(len(words)):
            if words[w].__contains__('TED') or words[w].__contains__('INC') or words[w].__contains__('CORP') or words[w].__contains__('TION') or words[w].__contains__('LTD'):
                company_name = words[0:w+1]
                # print(company_name)
                seperator = ' '
                company_name = seperator.join(company_name)
                # print(company_name)
                business_number = words[w]
                # print(business_number)
                year = words[w]
                # print(year)
                dict_data = [company_name, business_number, year]
                with open('tax_payer.csv', 'a') as f:
                    for item in dict_data:
                        f.write(str(item) + ', ')
                    f.write('\n')




def main():
    # co_op_reader()
    # uber_reader()
    # sask_power_reader()
    # amex_reader()
    # settlement_parser()
    bell_reader()
    # tax_payers()

if __name__ == '__main__':
    main()








# data_list = []

# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_210811.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_210817.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_210828.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_210837.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211048.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211053.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211100.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211106.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211113.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211121.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211128.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211135.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211138.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /IMG_20190503_211143.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/New Receipts & Scans -20190506T110536Z-001/New Receipts _ Scans /new_a.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/new_1/img20190502_07304218-3.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('img/new_1/img20190502_07304218-5.jpg', cv2.IMREAD_GRAYSCALE)
# img = 	rotated = imutils.rotate(img, 360)
# img = 	rotated = imutils.rotate(img, 90)

# img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
# img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
# cv2.imshow('rotated', img)
# cv2.waitKey(0)

# img = cv2.resize(img, None, fx=1.5, fy=2.0, interpolation=cv2.INTER_CUBIC)
# ret, thresh2 = cv2.threshold(img,172,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,37, 13)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,65, 27)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,69, 29)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,69, 29)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,17, 7)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,23, 7)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,33, 7)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,43, 7)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,93, 7)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,103, 2)




# cv2.imshow('rotated', th3)
# cv2.imshow('rotated', thresh2)
# cv2.waitKey(0)


# img = cv2.resize(img, (1030, 2048))
# cv2.imshow('img', img)
# cv2.waitKey(0)

# data = pytesseract.image_to_string(th3)

# data = re.sub(r'([\§\|\-\|\—])', '', data)
# print(data)
