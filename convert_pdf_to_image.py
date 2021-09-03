import os

from pdf2image import convert_from_path

DPI = 500
POPPLER_PATH = r'C:\\Program Files\\poppler\\bin'
USERPWD = None
USER_CROPBOX = False
STRICT = False
IMAGES_OUTPUT_PATH = ".\\{0}\\output-imgs\\page_{1}.jpg"


def generate_image_from_pdf(pdf_file_path, start_page, end_page, file_output_dir):
    images_dir = os.path.join(os.path.abspath(os.getcwd()), file_output_dir,"output-imgs")
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    pages = convert_from_path(
        pdf_file_path, 
        dpi=DPI, 
        first_page = start_page,
        last_page = end_page,
        userpw = USERPWD,
        use_cropbox = USER_CROPBOX,
        strict = STRICT,
        poppler_path=POPPLER_PATH
    )

    image_counter = 0
    for page in pages:
        filename = IMAGES_OUTPUT_PATH.format(file_output_dir, start_page + image_counter)
        page.save(filename, 'JPEG')
        print("Pages created: {0}".format(start_page + image_counter))
        image_counter = image_counter + 1


if __name__ == "__main__":
    pdf_file_path = 'd.pdf'
    file_output_dir = "temp"
    start_page = 2
    end_page = 2
    generate_image_from_pdf(pdf_file_path, start_page, end_page, file_output_dir)