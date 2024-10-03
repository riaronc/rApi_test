import PyPDF2
import nltk


def pdf_to_sentences(pdf_path: str):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    sentences = nltk.tokenize.sent_tokenize(text)
    return sentences
