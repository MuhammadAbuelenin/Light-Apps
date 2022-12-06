from pdf2docx import Converter

pdf_file = 'Muhammad Abuelenin CV.pdf'
docx_file = 'sample.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
