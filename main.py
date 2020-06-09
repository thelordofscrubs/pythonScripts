import pdfkit
import wkhtmltopdf

config = pdfkit.configuration(wkhtmltopdf='C:/Users/Eli/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/wkhtmltopdf')

css = "codenamesBase.css"
pdfkit.from_file("codenamesBase.html", "out.pdf")