from PyPDF2 import PdfReader

class Pdfparser:

    abgeordnete = []
    emails = []

    pdf_name = "Abgeordnetenportraits_RLP.pdf"

    def read_pdf(self, pdf_name):
        reader = PdfReader(pdf_name)
        number_of_pages = len(reader.pages)

        for site in range(118):
            pass

        page = reader.pages[21]
        text = page.extract_text()
        self.abgeordnete.append(text)
        self.abgeordnete = self.abgeordnete[0].split("\n")

    def get_emailadress(self, liste_von_abgeordneten):
        for element in liste_von_abgeordneten:
            if element.find("Email") != -1:
                self.emails.append(element)

if __name__ == "__main__":
    pdfparser = Pdfparser()
    pdfparser.read_pdf(pdfparser.pdf_name)
    pdfparser.get_emailadress(pdfparser.emails)
    print(pdfparser.emails)