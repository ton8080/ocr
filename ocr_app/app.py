from flask import Flask, render_template, request
from ocr_app.ocr_processor import PDFProcessor
import pytesseract
import os

class OCRApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.pdf_processor = PDFProcessor()
        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/processar', 'processar', self.processar, methods=['POST'])

    def index(self):
        return render_template('index.html')

    def processar(self):
        try:
            pdf_file = request.files['pdf_file']
            page_number = int(request.form['page_number'])

            caminho_temporario_pdf = 'temp.pdf'
            pdf_file.save(caminho_temporario_pdf)

            # img = self.pdf_processor.extract_img_from_pdf_page(caminho_temporario_pdf, page_number)
            text_ocr = self.perform_ocr(caminho_temporario_pdf, page_number)

            os.remove(caminho_temporario_pdf)

            return render_template('index.html', resultado=text_ocr)
        except Exception as e:
            return render_template('index.html', resultado=str(e))

    def perform_ocr(self, img_path, page_number):
        try:
            img = self.pdf_processor.extract_img_from_pdf_page(img_path, page_number)
            text = pytesseract.image_to_string(img)
            return text
        except Exception as e:
            return str(e)

