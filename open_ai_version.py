import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
import PyPDF2
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class PDFTranslator(GridLayout):

    def __init__(self, **kwargs):
        super(PDFTranslator, self).__init__(**kwargs)
        self.cols = 1

        self.select_file_button = Button(text="Select File", size_hint=(None, None), size=(150, 50))
        self.select_file_button.bind(on_press=self.select_file)
        self.add_widget(self.select_file_button)

        self.file_chooser = FileChooserIconView()
        self.file_chooser.bind(selection=self.update_file_path)

        self.text_input = TextInput(multiline=True, hint_text="Enter text to translate")
        self.add_widget(self.text_input)

        self.target_language_label = Label(text="Select target language:")
        self.add_widget(self.target_language_label)

        self.target_language = TextInput(hint_text="e.g. Spanish")
        self.add_widget(self.target_language)

        self.translate_button = Button(text="Translate", size_hint=(None, None), size=(150, 50))
        self.translate_button.bind(on_press=self.translate_text)
        self.add_widget(self.translate_button)

        self.text_output = TextInput(multiline=True, hint_text="Translated text will appear here")
        self.add_widget(self.text_output)

    def select_file(self, instance):
        self.file_chooser.path = "."
        self.file_chooser.filters = ["*.pdf"]
        self.add_widget(self.file_chooser)

    def update_file_path(self, instance, value):
        file_path = value[0]
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            self.text_input.text = text

    def translate_text(self, instance):
        source_text = self.text_input.text
        target_language = self.target_language.text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Translate the following text from English to {target_language}:\n{source_text}",
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0
        )
        translation = response.choices[0].text.strip()
        self.text_output.text = translation


class PDFTranslatorApp(App):
    def build(self):
        return PDFTranslator()


if __name__ == '__main__':
    # print(openai.api_key)
    PDFTranslatorApp().run()
