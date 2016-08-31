from PIL import Image

print ("my name")

im = Image.open("Test.jpg")

print("Format: ",im.format, "Size: ", im.size   )

print(list(im.getdata()))
