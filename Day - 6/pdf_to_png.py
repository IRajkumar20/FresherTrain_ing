import pypdfium2 as pdfium
from PIL import Image
# Load a document

filepath = "output3.pdf"

pdf = pdfium.PdfDocument(filepath)

page = pdf[0]

pil_image = page.render(scale=4).to_pil()

pil_image.save("final.jpg")
