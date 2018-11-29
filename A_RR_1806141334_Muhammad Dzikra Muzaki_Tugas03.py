from tkinter import *
from tkinter.messagebox import showinfo

class Barcode_Program_GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("EAN-13 [by Muhammad Dzikra Muzaki]")
        self.root.geometry("500x500")

        self.label_pack()

    def label_pack(self):
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

        self.barcode_input = Entry(self.root)
        self.barcode_input.bind("<Return>", self.generate_barcode)
        self.barcode_input.pack()

        self.barcode_canvas = Barcode_Generator()
        self.barcode_canvas.pack()

        self.filename_input.focus_set()

    def next_form(self):
        self.barcode_input.focus_set()

    def generate_barcode(self):
        try:
            pass
        except:
            pass

    def mainloop(self):
        self.root.mainloop()

class Barcode_Generator(Canvas):
    pass

def main():
    program_window = Barcode_Program_GUI()
    program_window.mainloop()

if __name__ == '__main__':
    main()
