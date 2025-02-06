# This app use to create pdf file maker


from fpdf import FPDF # Import FPDF class
import pandas as pd # Import pandas library


pdf = FPDF(orientation='P', unit='mm', format='A4') # Create instance of FPDF class
pdf.set_auto_page_break(auto=False, margin=0) # Set auto page break to false

df = pd.read_csv("topics.csv") # Read the csv file

for index, row in df.iterrows(): # iterate through the rows of the csv file
    pdf.add_page()

    # Set the header of the pdf

    pdf.set_font(family="Arial", size=24, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
    

    # add the line to the pdf body using the loop
    for Y in range(20 ,277 ,10):
        pdf.line(x1=10, y1=Y, x2=200, y2=Y)

    # set the footer of the pdf

    pdf.ln(265)
    pdf.set_font(family="Times", size=10, style='I')
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], ln=1, align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer of the pdf in the nested loop

        pdf.ln(277)
        pdf.set_font(family="Times", size=10, style='I')
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], ln=1, align="R")

        # add the line to the pdf body using the loop
        for Y in range(20 ,277 ,10):
            pdf.line(10, Y, 200, Y)


pdf.output("Example.pdf")
