from utils.convert.PdfToTextConverter import convert_pdf_to_string, save_string_in_txt_file


def convert_books_to_pdf():
    save_string_in_txt_file("resources/AGameOfThrones.txt", convert_pdf_to_string("resources/AGameOFThrones.pdf"))
    save_string_in_txt_file("resources/StormOfSwords.txt", convert_pdf_to_string("resources/StormOfSwords.pdf"))


if __name__ == '__main__':
    print("Hello")
