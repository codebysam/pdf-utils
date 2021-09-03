import os

from PIL import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'D:\\development\\learning\\pdf-to-text\\tesseract\\tesseract-ocr-w64-setup-v5.0.0-alpha.20210811.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
tessdata_dir_config="--tessdata-dir C:\\Program Files\\Tesseract-OCR\\tessdata"

TEXT_OUTPUT_PATH = ".\\{0}\\output-text\\{0}_{1}-{2}.txt"
IMAGES_OUTPUT_PATH = ".\\{0}\\output-imgs\\page_{1}.jpg"

def generate_raw_text_from_image(start_page, end_page, file_output_dir):
    outfile = TEXT_OUTPUT_PATH.format(file_output_dir, start_page, end_page)
    text_dir = os.path.join(os.path.abspath(os.getcwd()), file_output_dir,"output-text")
    
    if not os.path.exists(text_dir):
        print("Making")
        os.makedirs(text_dir)

    f = open(outfile, "a", encoding='utf-8')

    for i in range(start_page, end_page + 1):
        filename = IMAGES_OUTPUT_PATH.format(file_output_dir, i)
        custom_config = r'--oem 3 --psm 1'
        text = str(((pytesseract.image_to_string(Image.open(filename), config=custom_config))))
        text = text.replace('-\n', '')
        f.write(text)
        print("Text written: {0}".format(i))
    
    # Close the file after writing all the text.
    f.close()

if __name__ == "__main__":
    start_page = 2
    end_page = 2
    file_output_dir = "temp"
    generate_raw_text_from_image(start_page, end_page, file_output_dir)