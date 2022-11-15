import PyPDF2
import re

pdfFileObj = open('cv_test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

search_word = "Python"
search_word_count = 0

for pageNum in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText().encode('utf-8')
    search_text = text.lower().split()
    for word in search_text:
        if search_word in word.decode("utf-8"):
            search_word_count += 1

print("The word {} was found {} times".format(search_word, search_word_count))