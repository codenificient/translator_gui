# PDF Translator

PDF Translator is a Python/Kivy app that allows you to translate PDF documents from English to Spanish using the Google Translate or OpenAI's GPT models. The app provides a user-friendly graphical interface that allows you to select a PDF file from your computer, extract the text, and translate it into Spanish.

## Requirements

- Python 3.x
- PyPDF2
- googletrans
- openai
- Kivy

## Installation

1. Clone the repository to your local machine.
2. Install the required packages using pip:

`pip install -r requirements.txt`


3. Set the environment variable `OPENAI_API_KEY` to your OpenAI API key, depending on your use case.

I have created a `.env` file in the root directory and added the OpenAI API key.

## Usage

To start the app, run the `main.py` file:

`python main.py`


When the app starts, you will see a window with three buttons: "Select File", "Extract Text", and "Translate". Here's how to use the app:

1. Click the "Select File" button to select a PDF file from your computer.
2. Click the "Extract Text" button to extract the text from the selected PDF file. The extracted text will be displayed in the input field.
3. Click the "Translate" button to translate the text into Spanish. The translated text will be displayed in the output field.

## Notes

- The app uses the Google Translate API by default. If you want to use the OpenAI GPT model instead, uncomment the `use_openai` variable in the `translate_text` function and make sure you have set the `OPENAI_API_KEY` environment variable.

- The app may not work correctly if the PDF file contains non-Latin characters or other complex formatting.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Credits

This project was created by [CodenificienT](https://github.com/codenificient) and is based on the PyPDF2 library, the Google Translate API, and the OpenAI GPT models.
