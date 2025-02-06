#This app use to create pdf file maker


from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='L', unit='mm', format='A4')

df = pd.read_csv("topics.csv")

for index , row in df.iterrows():

    pdf.add_page()

    pdf.set_font(family="Arial", size=24, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0,h= 12, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 21, 287, 21)
    

pdf.output("test.pdf")