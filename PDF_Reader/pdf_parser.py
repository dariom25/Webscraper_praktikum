from PyPDF2 import PdfReader

abgeordnete = []

reader = PdfReader("Abgeordnetenportraits_RLP.pdf")
number_of_pages = len(reader.pages)

for site in range(118):
    pass

page = reader.pages[21]
text = page.extract_text()
abgeordnete.append(text)
abgeordnete = abgeordnete[0].split("\n")
print(abgeordnete)