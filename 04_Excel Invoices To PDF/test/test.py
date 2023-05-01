from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Create a PDF file
pdf_file = "example.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a table with some data
data = [['Name', 'Age', 'Gender'],
        ['John', '25', 'Male'],
        ['Jane', '30', 'Female'],
        ['Bob', '40', 'Male']]

table = Table(data)

# Add style to the table
table.setStyle(TableStyle([    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),    ('FONTSIZE', (0, 0), (-1, 0), 14),    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),    ('FONTSIZE', (0, 1), (-1, -1), 12),    ('BOTTOMPADDING', (0, 1), (-1, -1), 8),    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

# Add the table to the PDF document
story = []
story.append(table)
document.build(story)

# Confirm creation of PDF file
print(f"PDF file {pdf_file} created successfully!")