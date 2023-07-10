from pathlib import Path
from pypdf import PdfMerger

pdfs=["blockfungi.pdf","covid.pdf"]

merger=PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("output.pdf")
merger.close()
