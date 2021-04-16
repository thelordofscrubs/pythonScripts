from PIL import Image
import os

files = os.listdir()

if not os.path.exists("Upscaled Images"):
    os.makedirs("Upscaled Images")

print(files)

for file in files:
    if file.endswith("png"):
        im = Image.open(file)
        print(file)
        im = im.resize((2160,2160),Image.ANTIALIAS)
        im.save("Upscaled Images/"+file, "PNG")
    if file.endswith("jpeg") or file.endswith("jpg"):
        im = Image.open(file)
        print(file)
        im = im.resize((2160,2160),Image.ANTIALIAS)
        im.save("Upscaled Images/"+file, "JPEG")

input("Continue...")