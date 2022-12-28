from fpdf import FPDF

class Shirtificate():
    def __init__(self, name):
        self._name = name
        self._pdf =  FPDF()

    def get_shirt(self, header, imageFile):
        self._pdf.add_page()
        self._pdf.set_font('helvetica', 'B', size=50)
        self._pdf.cell(0, 60, header, new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image(imageFile, w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=47.5,y=140,txt=f'{self._name} took CS50')

    def save(self, fileName):
        self._pdf.output(fileName)



def main():
    name = input('Name:')
    pdf = Shirtificate(name)
    pdf.get_shirt('CS50 Shirtificate', './shirtificate.png')
    pdf.save('shirtificate.pdf')

if __name__ == '__main__':
    main()