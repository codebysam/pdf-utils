from convert_pdf_to_image import generate_image_from_pdf
from convert_image_to_searchable_pdf import generate_pdf_from_image

if __name__ == "__main__":
    file_name_without_extension = "Samir Ahmad"
    pdf_file_path = file_name_without_extension + ".pdf"
    start_page = 1
    end_page = 1
    file_output_dir = file_name_without_extension
    for index in range(start_page, end_page + 1):
        generate_image_from_pdf(pdf_file_path, index, index, file_output_dir)

    generate_pdf_from_image(start_page, end_page, file_output_dir)