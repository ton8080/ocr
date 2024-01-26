import io

import pytesseract
import fitz
from PIL import Image


class PDFProcessor:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    def extract_text_from_pdf_page(self, pdf_path, page_number):
        try:
            pdf_document = fitz.open(pdf_path)
            page = pdf_document[page_number - 1]
            text = page.get_text()
            return text
        except Exception as e:
            return str(e)


    def extract_img_from_pdf_page(self, pdf_path, page_number):
        try:
            pdf_document = fitz.open(pdf_path)
            page = pdf_document[page_number - 1]
            image_list = page.get_images(full=True)

            if image_list:
                image_index = image_list[0][0]
                base_image = pdf_document.extract_image(image_index)
                image_bytes = base_image["image"]
                img = Image.open(io.BytesIO(image_bytes))

                return img
            else:
                raise Exception("No images found on the specified page.")
        except Exception as e:
            return str(e)
