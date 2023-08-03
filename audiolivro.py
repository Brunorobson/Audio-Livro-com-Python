import PyPDF2, pyttsx3

#abre o ebook. Precisa sem em pdf
path = open ('arquivo.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()

#percorre as paginas do ebook, extrai os textos e faz a leitura
for pages in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()
speak.stop()