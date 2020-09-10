import pdfkit
import os
from openpyxl import load_workbook
import sys
import random
from shutil import copyfile

fileAmt = int(sys.argv[1])

dirPath = os.path.dirname(os.path.abspath(__file__))

HTMLLiteral = '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8"/>\n<link rel="stylesheet", type="text/css", href="codenamesCss.css"/>\n</head>\n<body>\n<div class="mainGrid">\n        <div class = "gridRow">\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n        </div>\n        <div class = "gridRow">\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n        </div>\n        <div class = "gridRow">\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n        </div>\n        <div class = "gridRow">\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n        </div>\n        <div class = "gridRow">\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n            <div class="gridItem"><p>{}</p></div>\n        </div>\n    </div>\n</body>\n</html>'

wkLoc = "C:/wkhtmltopdf/bin/wkhtmltopdf.exe"
print(wkLoc)
htmlFiles = []

def generateCellString():
    return "B"+str(random.randint(1,57))

o = {"orientation":"landscape"}

config = pdfkit.configuration(wkhtmltopdf=wkLoc)
css = dirPath+"\\codenamesCss.css"

wb = load_workbook(filename = "bingoSheets.xlsx")
cellContents = wb['#only']

for x in range(fileAmt):
    stuff = []
    while len(stuff) < 25:
        t = cellContents[generateCellString()].value
        if not (t in stuff):
            stuff.append(t)
    htmlToMod = HTMLLiteral.format(*stuff)
    try:
        pdfkit.from_string(htmlToMod, ("bingoBoard"+str(x)+".pdf"), options = o,configuration=config, css = css)
    except:
        pass