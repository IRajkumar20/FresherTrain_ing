from PIL import Image

image_name= Image.open(r'final.jpg')

outputImage = image_name.convert('RGB')

outputImage.save(r'final.pdf')
