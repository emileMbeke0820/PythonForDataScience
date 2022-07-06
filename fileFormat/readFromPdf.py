import PyPDF2


def reading_pdf():
    with open('recipe-book.pdf', 'r+b') as file:
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
        print(reader.getDocumentInfo())

        for page in range(0, reader.numPages):
            pageObj = reader.getPage(page)
            print("\n" + pageObj.extractText())


if __name__ == '__main__':
    reading_pdf()



