from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


pages_to_delete = [] # page numbering starts from 0
infile = PdfFileReader('RESUME.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i not in pages_to_delete:
        p = infile.getPage(i)
        output.addPage(p)

with open('Junaid_CV.pdf', 'wb') as f:
    output.write(f)




# from PyPDF2 import PdfFileWriter, PdfFileReader
# pages_to_keep = [0,1] # page numbering starts from 0
# infile = PdfFileReader('RESUME.pdf', 'rb')
# output = PdfFileWriter()
#
# for i in pages_to_keep:
#     p = infile.getPage(i)
#     output.addPage(p)
#
# with open('newfile.pdf', 'wb') as f:
#     output.write(f)