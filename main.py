from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('files/topics.csv')
print(pd)
for index, row in df.iterrows():
    number_of_pages = int(row['Pages'])
    for _ in range(number_of_pages):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
        pdf.line(10, 22, 200, 22)

        pdf.ln(257)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")


pdf.output('output.pdf')