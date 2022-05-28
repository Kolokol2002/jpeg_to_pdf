import os


import img2pdf

imagelist = os.listdir('.')
print(imagelist)

imagefiles = []
for i in imagelist:
    if i.endswith('.jpg'):
        imagefiles.append(i)

with open("1images.pdf", "wb") as f:
    f.write(img2pdf.convert(imagefiles))





