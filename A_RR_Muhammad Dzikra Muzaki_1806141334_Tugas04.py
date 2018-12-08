from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import sys
import os

class Main_Program:

    def __init__(self):
        self.root = Tk()
        self.root.title("Hidden Message Creator")
        self.root.geometry("500x250")
        self.introduction_screen()

    def introduction_screen(self):
        self.introduction_frame = Frame(self.root)
        self.introduction_frame.pack()

        introduction = Label(
                                  self.introduction_frame,
                                  text = (
                                          "This is a program "
                                          "to hide a message inside an image. "
                                          "Please use it wisely!"
                                          "\nIf you are ready, press Continue. "
                                          "Otherwise, click Exit."
                                          "\n\n Note: "
                                          "As of the current version, "
                                          "this program can only use the "
                                          "\n.jpg and .png format of an image."
                                         )
                                 )
        introduction.pack()

        self.continue_button = Button(
                                      self.introduction_frame,
                                      text = "Continue",
                                      command = self.first_screen
                                     )
        self.continue_button.pack()

        self.exit_button = Button(
                                  self.introduction_frame,
                                  text = "Exit",
                                  command = self.root.destroy
                                 )
        self.exit_button.pack()

    def first_screen(self):

        def path_assertion():
            try:
                self.image_path = self.image_name.get()

                if self.image_path == "":
                    showinfo("Invalid Input", "You have not chosen a file.")

                elif self.image_path[-4:] != ".jpg":
                    raise TypeError

                elif os.path.exists(self.image_path):
                    return True

                else:
                    raise FileNotFoundError

            except TypeError:
                self.image_name.delete(0, END)
                showinfo("Invalid Input", "The file you have chosen is not compatible.")

            except FileNotFoundError:
                self.image_name.delete(0, END)
                showinfo("Invalid Input", "The file you have chosen does not exists.")

        def choose_image():
            '''Choose file as input using GUI.'''

            try:
                # Ask for input file
                self.image_name.delete(0, END)
                self.image_path = ""

                input_window = Tk()
                input_window.withdraw()

                # Return chosen file
                self.image_path = filedialog.askopenfilename()
                self.image_name.delete(0, END)
                self.image_name.insert(0, f"{self.image_path}")

                if self.image_path == () or self.image_path == "":
                    self.image_name.delete(0, END)
                    showinfo("Invalid Input", "You have not chosen a file.")

                elif self.image_path[-4:] != ".jpg":
                    raise TypeError

            except TypeError:
                self.image_name.delete(0, END)
                showinfo("Invalid Input", "The file you have chosen is not compatible.")


        def next_screen(event = 1):
            if path_assertion():
                with open(self.image_path, 'rb') as self.image:
                    self.image_binary = ""
                    self.image_binary = self.image.read()
                self.second_screen()

        self.introduction_frame.destroy()

        self.first_frame = Frame(self.root)
        self.first_frame.pack()

        image_prompt = Label(
                                  self.first_frame,
                                  text = ("Please specify the path of the .jpg file that you wish to use. "
                                  "\nOr browse it interactively with a predesigned GUI."
                                 ))
        image_prompt.pack(side = TOP)

        self.image_name = Entry(self.first_frame, text = "Choose file")
        self.image_name.bind("<Return>", next_screen)
        self.image_name.pack(side = LEFT)
        self.image_name.focus_set()

        self.continue_button = Button(self.first_frame, text = "Next", command = next_screen)
        self.continue_button.pack(side = RIGHT)

        self.browse_image = Button(self.first_frame, text = "Browse", command = choose_image)
        self.browse_image.pack(side = RIGHT)

    def second_screen(self):

        def message_insertion(event = 1):
            pass

        self.first_frame.destroy()

        self.second_frame = Frame(self.root)
        self.second_frame.pack()

        message_prompt = Label(self.second_frame, text = "Write your message below.")
        message_prompt.pack()

        self.message_entry_box = Entry(self.second_frame, text = "Example message")
        self.message_entry_box.pack(side = LEFT)

        self.insert_button = Button(self.second_frame, text = "Insert", command = message_insertion)
        self.insert_button.pack(side = RIGHT)

    def mainloop(self):
        self.root.mainloop()

def main():
    program_window = Main_Program()
    program_window.mainloop()

if __name__ == '__main__':
    main()
