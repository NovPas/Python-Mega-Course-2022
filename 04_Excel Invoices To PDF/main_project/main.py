from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd
import glob
import os
from reportlab.platypus import Table, TableStyle


def get_dest_file(file_name):
    file_name = os.path.splitext(os.path.basename(file_name))[0]
    return file_name + '.pdf'


relevant_path = 'source/*.xls*'
dest_folder = 'results/'
w, h = A4

file_names = glob.glob(relevant_path)

for file_name in file_names:
    df = pd.read_excel(file_name)
    due_amount = df['total_price'].sum()

    file_name_dest = get_dest_file(file_name)

    c = canvas.Canvas(dest_folder+file_name_dest, pagesize=A4)

    # header
    c.setFont('Helvetica-Bold', 20)
    c.drawString(30, h - 50, f'Invoice nr.{file_name_dest[:4]}')
    c.drawString(30, h - 70, f'Date {file_name_dest[6:15]}')

    width = 200
    height = 100
    x = 30
    y = h - 150

    column_headers = list(df.columns.values)
    data_list = df.values.tolist()
    data_list.append(['','','','',due_amount])
    data_list.insert(0, column_headers)

    f = Table(data_list)

    # Define the style for the table
    table_style = TableStyle([
        # Set the font size for the table
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        # Set the alignment of the text within each cell to center
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        # Set the border for the table
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        # Set the background color for every other row
        # ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        # Set the grid lines for the table
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        # Set the color of the first line to green
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ])

    # Apply the style to the table
    f.setStyle(table_style)

    f.wrapOn(c,1,1)
    h_cur = y-(len(data_list)*5)
    f.drawOn(c, x, h_cur)

    # under
    c.setFont('Helvetica', 15)
    c.drawString(30, h_cur - 20, f'The total due amount is {due_amount}')
    c.drawString(30, h_cur - 40, 'Python How')

    c.showPage()
    c.save()
