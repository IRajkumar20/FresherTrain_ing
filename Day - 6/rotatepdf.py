from pypdf import PdfReader,PdfWriter

tilt_input=PdfReader("fake.pdf")
rotate1=PdfWriter()

tilt_page=tilt_input.pages[0]

tilt_page.rotate(270)

rotate1.add_page(tilt_page)

rotate1.write('rotate_pdf.pdf')



