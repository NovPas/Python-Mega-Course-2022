from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd

df = pd.read_csv('topics.csv')

w, h = A4
c = canvas.Canvas("report.pdf", pagesize=A4)

for index, row in df.iterrows():

    # header
    c.setFont('Helvetica-Bold', 20)
    c.drawString(30, h - 25, row['Topic'])
    # c.line(10, h - 30, w - 10, h - 30)

    for i in range(row['Pages']):

        # lines
        for line in range(1, 41):
            y_coord = h-(line*20)-10
            c.line(30, y_coord, w - 20, y_coord)

            # footer
        c.setFont('Helvetica', 10)
        c.drawRightString(w - 20, 10, row['Topic'])

        c.showPage()

c.save()
