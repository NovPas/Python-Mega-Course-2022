import pandas as pd
from fpdf import FPDF

df = pd.read_csv('articles.csv')

class Article:
    def __init__(self, code):
        self.data = df.loc[df['id'] == int(code)].to_dict('records')[0]

    def available(self):
        return self.data['in stock'] > 0


class Receipt:
    def __init__(self, number):
        self.number = number

    def print_to_pdf(self, article):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt {self.number}", ln=1)

        # pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {article.data['name']}", ln=1)

        # pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {article.data['price']}", ln=1)

        pdf.output("receipt.pdf")


if __name__ == '__main__':
    print(df)
    article_code = input("Choose a code of an article to buy:")
    article = Article(article_code)
    if article.available():
        receipt = Receipt(1)
        receipt.print_to_pdf(article)
    else:
        print('Out of stock')
