from utils.convert.PdfToTextConverter import convert_pdf_to_string, save_string_in_txt_file


if __name__ == '__main__':
    save_string_in_txt_file(convert_pdf_to_string("data/DragonBook.pdf"))
