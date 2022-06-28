from fpdf import FPDF


class PDF_Ventas(FPDF):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297

    def header(self):
        # Custom logo and positioning
        # Create an `assets` folder and put any wide and short image inside
        # Name the image `logo.png`
        # self.image('assets/logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 11)
        self.cell(60, 1, 'Fecha Inicio: XXX', 0, 0, 'L')
        self.cell(self.WIDTH - 180)
        self.cell(60, 1, 'Reporte de Ventas', 0, 0, 'R')
        self.ln(3)
        self.cell(60, 1, 'Fecha Fin: XXX', 0, 0, 'L')
        self.ln(20)

    def footer(self):
        # Page numbers in the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')

    def page_body(self, data):
        line_height = self.font_size * 2.5
        col_width = self.WIDTH / 8
        self.set_font("Arial", size=10)

        self.cell(40, line_height, "Fecha", 2, 0)
        self.cell(60, line_height, "Producto", 2, 0)
        self.cell(40, line_height, "Presentacion", 2, 0)
        self.cell(15, line_height, "Cant.", 2, 0)
        self.cell(15, line_height, "Total Bs", 2, 0)
        self.ln(line_height)

        print(f"Reporte Ventas - Pandas Data: {data}")
        for index, row in data.iterrows():
            print(f"Reporte Ventas - Row: {row}")

            self.cell(40, line_height, str(row["Fecha"]), 1, 0)
            self.cell(60, line_height, str(row["producto"]), 1, 0)
            self.cell(40, line_height, str(row["presentacion"]), 1, 0)
            self.cell(15, line_height, str(row["cantidad"]), 1, 0)
            self.cell(15, line_height, str(row["total Bs"]), 1, 0)

            self.ln(line_height)


    def print_page(self, data):
        # Generates the report
        self.add_page()
        self.page_body(data)