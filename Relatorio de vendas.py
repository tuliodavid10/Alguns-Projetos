from fpdf import FPDF

pdf = FPDF(orientation='p', unit='cm')
pdf.add_page()

pdf.set_font("helvetica", "B", 16)
pdf.cell(w=0, h=0.5, txt='Relatório de Vendas',align='c', new_x='LMARGIN', new_y='NEXT')
pdf.ln(1)

pdf.set_font("helvetica", style='', size=12)
pdf.multi_cell(w=0, h=0.5, txt='Para o mês de dezembro, foram registrados um total de 190 vendas para o setor de veículos importados', align='j', new_x='LMARGIN', new_y='NEXT')
pdf.ln(0.5)

pdf.set_font("helvetica", "B", 16)
pdf.cell(w=0, h=0.5, txt='Vendas de carros americanos',align='l', new_x='LMARGIN', new_y='NEXT')
pdf.ln(0.2)

pdf.set_font("helvetica", style='', size=12)
pdf.multi_cell(w=0, h=0.5, txt='Foram vendidos 100 carros americanos', align='j', new_x='LMARGIN', new_y='NEXT')
pdf.ln(0.5)

pdf.set_font("helvetica", "B", 16)
pdf.cell(w=0, h=0.5, txt='Vendas de carros italianos',align='l', new_x='LMARGIN', new_y='NEXT')
pdf.ln(0.2)

pdf.set_font("helvetica", style='', size=12)
pdf.multi_cell(w=0, h=0.5, txt='Foram vendidos 90 carros italianos', align='j', new_x='LMARGIN', new_y='NEXT')

pdf.output("tuto1.pdf")