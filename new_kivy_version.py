import os
import PyPDF2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from googletrans import Translator
from kivy.uix.filechooser import FileChooserListView

class TranslateApp(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'

        # Create text input and output widgets
        self.input_text = TextInput(multiline=True, hint_text='Enter text or select a PDF file')
        self.add_widget(self.input_text)

        self.output_text = TextInput(multiline=True, readonly=True)
        self.add_widget(self.output_text)

        # Create select file button
        self.select_file_button = Button(text='Select File')
        self.select_file_button.size_hint_y = None
        self.select_file_button.height = 50
        self.select_file_button.bind(on_press=self.open_file_dialog)
        self.add_widget(self.select_file_button)

        # Create translate button
        self.translate_button = Button(text='Translate')
        self.translate_button.size_hint_y = None
        self.translate_button.height = 50
        self.translate_button.bind(on_press=self.translate_text)
        self.add_widget(self.translate_button)

    def open_file_dialog(self, instance):
        # Open file dialog to select PDF file
        file_chooser = FileChooserListView()
        file_chooser.path = os.path.expanduser('~')
        file_chooser.filters = ['*.pdf']
        file_chooser.bind(selection=self.select_file)
        self.add_widget(file_chooser)

    def select_file(self, instance, selection):
        # Check if file was selected and extract text if it was
        if selection:
            self.file_name = selection[0]
            self.extract_text()

    def extract_text(self):
        # Extract text from selected PDF file and add it to input_text area
        with open(self.file_name, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in range(len(pdf_reader.pages)):
                page_obj = pdf_reader.pages[page]
                text += page_obj.extract_text()
            # Set extracted text as the input_text content
            self.input_text.text = text

    def translate_text(self, instance):
        # Get text to translate from input_text area
        text_to_translate = self.input_text.text

        # Translate text using Google Translate API
        translator = Translator()
        translated_text = translator.translate(text_to_translate, src='en', dest='es').text

        # Set translated text as the output_text content
        self.output_text.text = translated_text

class TranslateAppKivy(App):

    def build(self):
        return TranslateApp()

if __name__ == '__main__':
    TranslateAppKivy().run()
