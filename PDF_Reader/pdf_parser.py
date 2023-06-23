import PyPDF2

 

with open('example.pdf', 'rb') as pdf_file:

    read_pdf = PyPDF2.PdfFileReader(pdf_file)

    number_of_pages = read_pdf.getNumPages()

    pages_to_parse = 2

    if pages_to_parse > number_of_pages:

        pages_to_parse = number_of_pages

    for i in range(pages_to_parse):

        page = read_pdf.getPage(i)

        page_content = page.extractText()

        print(page_content)