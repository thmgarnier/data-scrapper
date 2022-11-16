import re
from PyPDF2 import PdfFileReader as pfr

with open('test.pdf', 'rb') as file:
    pdfReader = pfr(file)
    page = pdfReader.getPage(0)
    print(page.extractText())
