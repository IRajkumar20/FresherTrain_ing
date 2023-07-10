from pathlib import Path
from pypdf import PdfReader,PdfWriter

pdf_name1=PdfReader("covid.pdf")

for i,page in enumerate(pdf_name1.pages[0:4]):
    output=PdfWriter()
    output.add_page(page)
    output.write(f"output{i+1}.pdf")

