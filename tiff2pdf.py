# Sean Kincaid
# Sean-In-Dezine on GitHub

# https://github.com/sean-in-dezine
# @yyyeatho on Instagram

# Make sure the directory is set properly to where the IMAGE FILES are
# Make sure the terminal is LOCATED to that directory
# Run the script and it'll iterate through each .tiff file
# Then converting it to a .pdf
# That .pdf will not be searchable


import img2pdf
import os
dirname = (
    r"C:\pathname")
filesarray = os.listdir(dirname)
for filename in filesarray:
    if not filename.endswith(".tiff"):
        continue
    print(filename)
    print(filename[:-5])
    extPDF = ".pdf"
    newFile = filename[:-5] + extPDF
    print(newFile)
    path = os.path.join(dirname, filename)
    with open(newFile, "wb") as fn:
        if os.path.isdir(path):
            continue
        fn.write(img2pdf.convert(path))
        continue
