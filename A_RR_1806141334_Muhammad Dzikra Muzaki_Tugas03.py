from tkinter import *
from tkinter.messagebox import showinfo

class Barcode_Program_GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("EAN-13 [by Muhammad Dzikra Muzaki]")
        self.root.geometry("350x350")

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

    def check_sum(self, barcode):
        last_digit = 0

        for i in range(len(barcode)):
            if (i % 2 == 0):
                last_digit += int(barcode[i])
            else:
                last_digit += int(barcode[i]) * 3

        last_digit = (10 - last_digit % 10) % 10
        barcode += str(last_digit)

        return barcode

    def generate_barcode(self, event):

        filename = self.filename_input.get()
        barcode = self.barcode_input.get()
        error_message = ""

        reserved_chars = ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>']

        filename_invalid = False
        barcode_invalid = False

        for chr in reserved_chars:
            if chr in filename:
                filename_invalid = True
                error_message += (
                                 "FilenameError: Cannot use reserved "
                                 "characters. Please input a filename without "
                                 "/, \\, ?, %, *, :, |, \", <, >."
                                 )
                break

        if filename[-4:] != ".eps":
            filename_invalid = True
            if error_message != "":
                error_message += "\n\n"
            error_message += (
                             "FilenameError: File extension not valid. "
                             "Please input a .eps filename."
                             )

        if not (len(barcode) == 12 and barcode.isnumeric()):
            barcode_invalid = True
            if error_message != "":
                error_message += "\n\n"
            error_message += (
                             "BarcodeError: Barcode length is not correct "
                             "or not an integer."
                             )

        if filename_invalid or barcode_invalid:
            showinfo("Invalid Input", error_message)

        else:
            barcode = self.check_sum(barcode)
            self.barcode_canvas.create_barcode(self.root, filename, barcode)

    def mainloop(self):
        self.root.mainloop()

class Barcode_Generator(Canvas):

    # Dictionary for EAN-13 code mapping
    first_index = {"0":"LLLLLLRRRRRR", "1":"LLGLGGRRRRRR", "2":"LLGGLGRRRRRR",
                   "3":"LLGGGLRRRRRR", "4":"LGLLGGRRRRRR", "5":"LGGLLGRRRRRR",
                   "6":"LGGGLLRRRRRR", "7":"LGLGLGRRRRRR", "8":"LGLGGLRRRRRR",
                   "9":"LGGLGLRRRRRR"}

    each_digit = {"0":"000110101001111110010", "1":"001100101100111100110",
                  "2":"001001100110111101100", "3":"011110101000011000010",
                  "4":"010001100111011011100", "5":"011000101110011001110",
                  "6":"010111100001011010000", "7":"011101100100011000100",
                  "8":"011011100010011001000", "9":"000101100101111110100"}

    def __init__(self, root):
        self.draw_canvas = Canvas(
                                 root,
                                 width = 350,
                                 height = 275,
                                 background = "white"
                                 )
        self.draw_canvas.pack()

    # Draw lines according to variable codes at some given position
    def draw_lines(self, x, y, codes, side, color="black"):
        for i in range(len(codes)):
            if (codes[i] == '1'):
                self.draw_canvas.create_line(
                                            x + 2 * i,
                                            y,
                                            x + 2 * i,
                                            y + side,
                                            width = 2,
                                            fill = color
                                            )

    def create_barcode(self, root, filename, barcode):

        # CONSTS
        pos_x = 60
        pos_y = 20

		# Clear before reusing the canvas
        self.draw_canvas.delete("all")

		# Write the title
        self.draw_canvas.create_text(
                                    pos_x + 114,
                                    pos_y + 40,
                                    text = "EAN-13 Barcode:",
                                    font = ("Helvetica", 10, "bold")
                                    )

		# Write the codes
        self.draw_canvas.create_text(
                                    pos_x + 12,
                                    pos_y + 166,
                                    text = barcode[0],
                                    font = ("Helvetica", 10, "bold")
                                    )

        for i in range(0, 6):
            self.draw_canvas.create_text(
                                        pos_x + 36 + i * 12,
                                        pos_y + 166,
                                        text = barcode[i+1],
                                        font = ("Helvetica", 10, "bold")
                                        )

        for i in range(0, 6):
            self.draw_canvas.create_text(
                                        pos_x + 130 + i * 12,
                                        pos_y + 166,
                                        text = barcode[i+7],
                                        font = ("Helvetica", 10, "bold")
                                        )

		# Draw separator lines
        self.draw_lines(pos_x + 20, pos_y + 60, "101", 100, "blue")
        self.draw_lines(pos_x + 110, pos_y + 60, "01010", 100, "blue")
        self.draw_lines(pos_x + 204, pos_y + 60, "101", 100, "blue")

		# START DRAW BARCODES
        for i in range(0, 6):
			# barcode[i+1]
            start_pos = 0
            digit_encoding = self.first_index[barcode[0]][i]
            if (digit_encoding == "G"):
                start_pos = 7
            self.draw_lines(
                            pos_x + 26 + i * 14,
                            pos_y + 60,
                            self.each_digit[barcode[i+1]][start_pos:start_pos+7],
                            90
                            )

        for i in range(0, 6):
			# barcode[i+7]
            start_pos = 14
            self.draw_lines(
                            pos_x + 120 + i * 14,
                            pos_y + 60,
                            self.each_digit[barcode[i+7]][start_pos:start_pos+7],
                            90
                            )
		# END DRAW BARCODES

		# Write check digit
        self.draw_canvas.create_text(
                                    pos_x + 114,
                                    pos_y + 188,
                                    text = "Check Digit: {}".format(barcode[-1:]),
                                    font = ("Helvetica", 10, "bold"),
                                    fill = "orange"
                                    )

		# Output canvas to eps file
        self.draw_canvas.postscript(file = filename, colormode = "color")

def main():
    program_window = Barcode_Program_GUI()
    program_window.mainloop()

if __name__ == '__main__':
    main()
