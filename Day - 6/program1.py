from pypdf import PdfReader
from pypdf import PdfWriter
from pathlib import Path

pdf_name1=PdfReader("covid.pdf")
for page in pdf_name1.pages:
    page.extract_text()


pdf_name=PdfWriter()
pdf_name.add_page(pdf_name1.pages[0])
pdf_name.write("fake.pdf")

