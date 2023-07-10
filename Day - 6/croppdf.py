from pypdf import PdfReader,PdfWriter


crop_name=PdfReader('fake.pdf')

cropoutput=PdfWriter()

page1=crop_name.pages[0]

page1.mediabox.upper_left=[5,50]

page1.mediabox.lower_right=[50,112]

cropoutput.add_page(page1)

cropoutput.write('crop_output.pdf')

