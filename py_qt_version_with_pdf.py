import sys
import os
import PyPDF2
from googletrans import Translator
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QPushButton

class TranslateApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle('PDF Translator')
        self.setGeometry(100, 100, 800, 600)

        # Create text input and output widgets
        self.input_text = QTextEdit(self)
        self.input_text.setPlaceholderText('Enter text or select a PDF file')
        self.input_text.setGeometry(20, 20, 760, 240)

        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        self.output_text.setGeometry(20, 280, 760, 240)

        # Create file menu actions
        self.open_file_action = QAction('Open', self)
        self.open_file_action.setShortcut('Ctrl+O')
        self.open_file_action.triggered.connect(self.open_file_dialog)

        self.exit_action = QAction('Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.triggered.connect(self.close)

        # Create file menu
        self.file_menu = self.menuBar().addMenu('File')
        self.file_menu.addAction(self.open_file_action)
        self.file_menu.addAction(self.exit_action)

        # Create select file button
        self.select_file_button = QPushButton('Select File', self)
        self.select_file_button.setGeometry(20, 540, 150, 40)
        self.select_file_button.clicked.connect(self.open_file_dialog)

        # Create translate button
        self.translate_button = QPushButton('Translate', self)
        self.translate_button.setGeometry(200, 540, 150, 40)
        self.translate_button.clicked.connect(self.translate_text)

    def open_file_dialog(self):
        # Open file dialog to select PDF file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select PDF file', '', 'PDF Files (*.pdf)', options=options)

        # Check if file was selected and extract text if it was
        if file_name:
            self.file_name = file_name
            self.extract_text()

    def extract_text(self):
        # Extract text from selected PDF file and add it to input_text area
        with open(self.file_name, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text = ""
            for page in range(pdf_reader.numPages):
                page_obj = pdf_reader.getPage(page)
                text += page_obj.extractText()
            # Set extracted text as the input_text content
            self.input_text.setText(text)

    def translate_text(self):
        # Get text to translate from input_text area
        text_to_translate = self.input_text.toPlainText()

        # Translate text using Google Translate API
        translator = Translator()
        translated_text = translator.translate(text_to_translate, src='en', dest='es').text

        # Set translated text as the output_text content
        self.output_text.setText(translated_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translate_app = TranslateApp()
    translate_app.show()
    sys.exit(app.exec_())
