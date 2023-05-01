import glob
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import textwrap

relevant_path = 'source/*.txt'
w, h = A4
file_paths = glob.glob(relevant_path)
c = canvas.Canvas('result.pdf', pagesize=A4)

for file_path in file_paths:

    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # header
    c.setFont('Helvetica-Bold', 20)
    c.drawString(30, h - 50, file_name.title())

    with open(file_path) as f:
        context = f.read()
        c.setFont('Helvetica', 15)
        # Use textwrap to wrap the text into multiple lines
        lines = textwrap.wrap((' '*4)+context, width=80)
        textobject = c.beginText(30, h - 70)
        for line in lines:
            textobject.textLine(line)
        c.drawText(textobject)

        # c.drawString(30, h - 70, lines.replace("\n", "<br />"))

    c.showPage()

c.save()