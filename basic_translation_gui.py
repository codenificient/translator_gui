import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QTextEdit, QGridLayout
from googletrans import Translator


class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create labels and buttons
        self.file_label = QLabel("Select file:")
        self.translate_button = QPushButton("Translate")
        self.input_label = QLabel("Input text:")
        self.output_label = QLabel("Translated text:")
        self.input_field = QTextEdit()
        self.output_field = QTextEdit()

        # Connect buttons to functions
        self.translate_button.clicked.connect(self.translate_text)

        # Set up layout
        grid = QGridLayout()
        grid.addWidget(self.file_label, 0, 0)
        grid.addWidget(self.translate_button, 0, 1)
        grid.addWidget(self.input_label, 1, 0)
        grid.addWidget(self.input_field, 1, 1)
        grid.addWidget(self.output_label, 2, 0)
        grid.addWidget(self.output_field, 2, 1)
        self.setLayout(grid)

        self.show()

    def translate_text(self):
        # Get input text
        input_text = self.input_field.toPlainText()

        # Translate input text
        translator = Translator()
        output_text = translator.translate(input_text, dest='es').text

        # Set output text field
        self.output_field.setText(output_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TranslatorApp()
    sys.exit(app.exec_())
