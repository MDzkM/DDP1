from tkinter import *
from tkinter.messagebox import showinfo

# Main GUI Class
class Barcode_Program_GUI:
    def __init__(self):

        # Root intialization
        self.root = Tk()
        self.root.title("EAN-13 [by Muhammad Dzikra Muzaki]")
        self.root.geometry("350x350")

        # Calls function to build GUI content
        self.pack_label()

    def pack_label(self):
        '''Creates main GUI content and layout.'''

        # Filename prompt message intialization
        filename_prompt = Label(
                    self.root,
                    text = "Save barcode to PS file [eg: EAN13.eps]:",
                    font = ("Helvetica", 10, "bold")
                    )
        filename_prompt.pack()

        # Filename input box intialization
        self.filename_input = Entry(self.root)
        self.filename_input.bind("<Return>", self.next_form)
        self.filename_input.pack()

        # Barcode prompt initialization
        barcode_prompt = Label(
                    self.root,
                    text = "Enter code (first 12 decimal digits):",
                    font = ("Helvetica", 10, "bold")
                    )
        barcode_prompt.pack()

        # Barcode input box initialization
        self.barcode_input = Entry(self.root)
        self.barcode_input.bind("<Return>", self.generate_barcode)
        self.barcode_input.pack()

        # Initialize the drawing canvas
        self.barcode_canvas = Barcode_Generator(self.root)

        # Automatically sets the cursor in the first entry box
        self.filename_input.focus_set()

    def next_form(self, event):
        '''Jumps to the next entry box when pressed enter.'''

        self.barcode_input.focus_set()

    def check_sum(self, barcode):
        '''Finds the check digit of the barcode from the first 12 digits.'''

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

        # Get the input from the entry box
        filename = self.filename_input.get()
        barcode = self.barcode_input.get()

        # Initialize error message
        error_message = ""

        # List of restricted characters to use in naming files
        reserved_chars = ['/', '\\', '?', '%', '*', ':', '|', '"', '<', '>']

        # Sets error boolean value
        filename_invalid = False
        barcode_invalid = False

        # Checks for invalid characters in filename input
        for chr in reserved_chars:
            if chr in filename:
                filename_invalid = True
                error_message += (
                                 "FilenameError: Cannot use reserved "
                                 "characters. Please input a filename without "
                                 "/, \\, ?, %, *, :, |, \", <, >."
                                 )
                break

        # Checks for invalid file extensions
        if filename[-4:] != ".eps":
            filename_invalid = True
            if error_message != "":
                error_message += "\n\n"
            error_message += (
                             "FilenameError: File extension not valid. "
                             "Please input a .eps filename."
                             )

        # Checks for invalid barcode input
        if not (len(barcode) == 12 and barcode.isnumeric()):
            barcode_invalid = True
            if error_message != "":
                error_message += "\n\n"
            error_message += (
                             "BarcodeError: Barcode length is not correct "
                             "or not an integer."
                             )

        # Shows error message if error boolean is true
        if filename_invalid or barcode_invalid:
            showinfo("Invalid Input", error_message)

        # Draw barcode if there are no errors
        else:
            barcode = self.check_sum(barcode)
            self.barcode_canvas.create_barcode(self.root, filename, barcode)

    # Starts the main program
    def mainloop(self):
        self.root.mainloop()

class Barcode_Generator(Canvas):

    # Dictionary for barcode pattern mapping
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

        # Main canvas initialization
        self.draw_canvas = Canvas(
                                 root,
                                 width = 350,
                                 height = 275,
                                 background = "white"
                                 )
        self.draw_canvas.pack()

    # Draw bars corresponding with the codes
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
        '''Draw and save barcode to a .eps file.'''

        # Start location of pointer
        pos_x = 60
        pos_y = 20

		# Clear before reusing the canvas
        self.draw_canvas.delete("all")

		# Write the barcode title
        self.draw_canvas.create_text(
                                    pos_x + 114,
                                    pos_y + 40,
                                    text = "EAN-13 Barcode:",
                                    font = ("Helvetica", 10, "bold")
                                    )

		# Write the barcode underneath the black and blue bars
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
                                        text = barcode[i + 1],
                                        font = ("Helvetica", 10, "bold")
                                        )

        for i in range(0, 6):
            self.draw_canvas.create_text(
                                        pos_x + 130 + i * 12,
                                        pos_y + 166,
                                        text = barcode[i + 7],
                                        font = ("Helvetica", 10, "bold")
                                        )

		# Draw blue separator lines at the left, right, and middle of barcode
        self.draw_lines(pos_x + 20, pos_y + 60, "101", 100, "blue")
        self.draw_lines(pos_x + 110, pos_y + 60, "01010", 100, "blue")
        self.draw_lines(pos_x + 204, pos_y + 60, "101", 100, "blue")

		# Loop for drawing each bars for every digit in the barcode
        for i in range(0, 6):
            start_pos = 0
            digit_encoding = self.first_index[barcode[0]][i]
            if (digit_encoding == "G"):
                start_pos = 7
            codes = self.each_digit[barcode[i + 1]][start_pos:start_pos + 7]
            self.draw_lines(
                            pos_x + 26 + i * 14,
                            pos_y + 60,
                            codes,
                            90
                            )

        for i in range(0, 6):
            start_pos = 14
            codes = self.each_digit[barcode[i + 7]][start_pos: start_pos + 7]
            self.draw_lines(
                            pos_x + 120 + i * 14,
                            pos_y + 60,
                            codes,
                            90
                            )

		# Write check digit underneath the barcode number
        check_sum = barcode[-1:]
        self.draw_canvas.create_text(
                                    pos_x + 114,
                                    pos_y + 188,
                                    text = "Check Digit: {}".format(check_sum),
                                    font = ("Helvetica", 10, "bold"),
                                    fill = "orange"
                                    )

		# Output canvas drawing to a .eps file
        self.draw_canvas.postscript(file = filename, colormode = "color")

def main():
    program_window = Barcode_Program_GUI()
    program_window.mainloop()

if __name__ == '__main__':
    main()
