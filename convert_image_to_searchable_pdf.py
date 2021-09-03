import os

from PIL import Image
import pytesseract
from PyPDF2 import PdfFileMerger, PdfFileReader

# pytesseract.pytesseract.tesseract_cmd = r'D:\\development\\learning\\pdf-to-text\\tesseract\\tesseract-ocr-w64-setup-v5.0.0-alpha.20210811.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
tessdata_dir_config="--tessdata-dir C:\\Program Files\\Tesseract-OCR\\tessdata"


PDF_OUTPUT_PATH = ".\\{0}\\output-pdf\\{0}_{1}-{2}.pdf"
IMAGES_OUTPUT_PATH = ".\\{0}\\output-imgs\\page_{1}.jpg"

def generate_pdf_from_image(start_page, end_page, file_output_dir):
    outfile = PDF_OUTPUT_PATH.format(file_output_dir, start_page, end_page)
    pdf_dir = os.path.join(os.path.abspath(os.getcwd()), file_output_dir,"output-pdf")
    
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    # f = open(outfile, "ab")

    for i in range(start_page, end_page + 1):
        filename = IMAGES_OUTPUT_PATH.format(file_output_dir, i)
        pdf_b64_text = pytesseract.image_to_pdf_or_hocr(Image.open(filename), extension='pdf')
        temp_pdf_file = open(pdf_dir + "/temp_{0}.pdf".format(i), "ab")
        temp_pdf_file.write(pdf_b64_text)
        temp_pdf_file.close()
        
        print("Image processed: {0}".format(i))
 
    mergedObject = PdfFileMerger()

    for i in range(start_page, end_page + 1):
        mergedObject.append(PdfFileReader(pdf_dir + "/temp_{0}.pdf".format(i), 'rb'))
        os.remove(pdf_dir + "/temp_{0}.pdf".format(i))

    mergedObject.write(outfile)
    
    # f.close()
    

if __name__ == "__main__":
    start_page = 1
    end_page = 3
    file_output_dir = "Issues and Messaging - Customer"
    generate_pdf_from_image(start_page, end_page, file_output_dir)