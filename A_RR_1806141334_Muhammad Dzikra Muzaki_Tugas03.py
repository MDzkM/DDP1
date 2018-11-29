from tkinter import *
from tkinter.messagebox import showinfo

class Barcode_Program_GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("EAN-13 [by Muhammad Dzikra Muzaki]")
        self.root.geometry("450x450")

        self.pack_label()

    def pack_label(self):
        filename_prompt = Label(
                    self.root,
                    text = "Save barcode to PS file [eg: EAN13.eps]:",
                    font = ("Helvetica", 10, "bold")
                    )
        filename_prompt.pack()

        self.filename_input = Entry(self.root)
        self.filename_input.bind("<Return>", self.next_form)
        self.filename_input.pack()

        barcode_prompt = Label(
                    self.root,
                    text = "Enter code (first 12 decimal digits):",
                    font = ("Helvetica", 10, "bold")
                    )
        barcode_prompt.pack()

        self.barcode_input = Entry(self.root)
        self.barcode_input.bind("<Return>", self.generate_barcode)
        self.barcode_input.pack()

        self.barcode_canvas = Barcode_Generator(self.root)

        self.filename_input.focus_set()

    def next_form(self, event):
        self.barcode_input.focus_set()

    def checksum(self):
        pass

    def generate_barcode(self, event):

        filename = self.filename_input.get()
        barcode = self.barcode_input.get()

        reserved_chars = set('/\?%*:|"<>.')

        filename_invalid = any() and filename[-4:] != ".eps"
        barcode_invalid = not (len(barcode) == 12 and barcode.isnumeric())

        self.barcode_canvas(self.filename_input.get(), self.barcode_input.get())

    def mainloop(self):
        self.root.mainloop()

class Barcode_Generator(Canvas):
    def __init__(self, root):
        self.draw_canvas = Canvas(root, width = 450, height = 400, background = "white")
        self.draw_canvas.pack()

    def create_barcode(self, filename, barcode):
        pass

def main():
    program_window = Barcode_Program_GUI()
    program_window.mainloop()

if __name__ == '__main__':
    main()
