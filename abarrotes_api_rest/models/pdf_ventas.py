import datetime

from fpdf import FPDF


class PDF_Ventas(FPDF):
    def __init__(self, desde, hasta):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        self.desde = desde
        self.hasta = hasta

    def header(self):
        # Custom logo and positioning
        # Create an `assets` folder and put any wide and short image inside
        # Name the image `logo.png`
        # self.image('assets/logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 18)
        line_height = self.font_size * 2.5
        self.cell(self.w, line_height, 'Reporte de Ventas', "B", line_height, 'C')

        self.set_font('Arial', 'B', 11)
        self.ln(line_height)
        line_height = self.font_size * 2.5
        self.cell(60, 1, f'Desde: {self.desde}', 0, 0, 'L')
        self.set_x(self.w - 80)
        now = datetime.datetime.now()
        self.cell(60, 1, f'Fecha Impresión: {now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}', 0, 0, 'L')
        self.ln(line_height)
        self.cell(60, 1, f'Hasta: {self.hasta}', 0, line_height, 'L')
        self.ln(line_height)
        self.cell(self.w, line_height, '', "T", line_height)

    def footer(self):
        # Page numbers in the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')

    def page_body(self, data):
        line_height = self.font_size * 2.5

        total_products = 0
        total_cash = 0.0

        self.set_font("Arial", 'B', size=10)

        self.cell(40, line_height, "Fecha", 1, 0)
        self.cell(60, line_height, "Producto", 1, 0)
        self.cell(40, line_height, "Presentacion", 1, 0)
        self.cell(15, line_height, "Cant.", 1, 0)
        self.cell(15, line_height, "Total Bs", 1, 0)
        self.ln(line_height)
        self.set_font("Arial", size=10)

        print(f"Reporte Ventas - Pandas Data: {data}")
        for index, row in data.iterrows():
            print(f"Reporte Ventas - Row: {row}")
            self.cell(40, line_height, str(row["Fecha"]), 1, ln=0)
            producto = row["producto"] if len(row["producto"]) < 35 else row["producto"][:31] + "..."
            self.cell(60, line_height, producto, 1, ln=0)
            presentacion = row["presentacion"] if len(row["presentacion"]) < 23 else row["presentacion"][:21] + "..."
            self.cell(40, line_height, presentacion, 1, ln=0)
            self.cell(15, line_height, str(int(row["cantidad"])), 1, ln=0)
            self.cell(15, line_height, str(row["total Bs"]), 1, ln=0)

            total_products += int(row["cantidad"])
            total_cash += row["total Bs"]

            self.ln(line_height)

        self.ln(line_height)
        self.set_font('Arial', 'B', 11)
        self.set_x(self.w - 80)
        self.cell(25, line_height, "# Productos", 1, ln=0)
        self.cell(25, line_height, "Total Bs.", 1, ln=0)
        self.ln(line_height)
        self.set_x(self.w - 80)
        self.set_font('Arial', 'BU', 11)
        self.cell(25, line_height, str(total_products), 1, ln=0)
        self.cell(25, line_height, str(total_cash), 1, ln=0)

    def print_page(self, data):
        # Generates the report
        self.add_page()
        self.page_body(data)
