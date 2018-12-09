from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import os
import binascii

class Hidden_Message_Creator:

    def __init__(self):
        self.root = Tk()
        self.root.title("Hidden Message Creator")
        self.root.geometry("500x500")
        self.introduction_frame = Frame(self.root)
        self.first_frame = Frame(self.root)
        self.second_frame = Frame(self.root)
        self.third_frame = Frame(self.root)
        self.current_frame = 0
        self.delimiter = "\\" + str(hex(1111111111111110))[1:]
        self.delimiter = self.delimiter.encode('utf-8')
        self.introduction_screen()

    def introduction_screen(self):

        if self.current_frame == 1:
            self.first_frame.destroy()
            self.first_frame = Frame(self.root)

        elif self.current_frame == 2:
            self.second_frame.destroy()
            self.second_frame = Frame(self.root)

        elif self.current_frame == 3:
            self.third_frame.destroy()
            self.third_frame = Frame(self.root)

        self.introduction_frame.pack()

        introduction = Label(
                             self.introduction_frame,
                             text = (
                                     "\n\nThis is a program "
                                     "to hide a message inside an image. "
                                     "Please use it wisely!"
                                     "\nIf you are ready, press Continue. "
                                     "Otherwise, click Exit."
                                     "\n\n Note: "
                                     "As of the current version, "
                                     "this program is only for the "
                                     "\n .png format of an image.\n"
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

                elif self.image_path[-4:] != ".png":
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

                elif self.image_path[-4:] != ".png":
                    raise TypeError

            except TypeError:
                self.image_name.delete(0, END)
                showinfo("Invalid Input", "The file you have chosen is not compatible.")

        def next_screen(event = 1):
            if path_assertion():
                with open(self.image_path, "rb") as self.image:
                    self.image_binary = self.image.read()
                self.second_screen()

        self.introduction_frame.destroy()
        self.introduction_frame = Frame(self.root)

        self.first_frame.pack()

        self.current_frame = 1

        image_prompt = Label(
                             self.first_frame,
                             text = (
                                     "\n\nPlease specify the path of the "
                                     ".png file that you wish to use "
                                     "\nor browse it interactively with "
                                     "a predesigned GUI:"
                                    )
                            )
        image_prompt.pack()

        self.image_name = Entry(self.first_frame, text = "Choose file")
        self.image_name.bind("<Return>", next_screen)
        self.image_name.pack()
        self.image_name.focus_set()

        self.browse_image = Button(self.first_frame, text = "Browse", command = choose_image)
        self.browse_image.pack()

        self.continue_button = Button(self.first_frame, text = "Next", command = next_screen)
        self.continue_button.pack()

    def second_screen(self):

        def message_insertion(event = 1):
            self.message = self.message_entry_box.get()
            self.message_binary = ""

            for _ in self.message:
                self.message_binary += "\\" + str(hex(ord(_)))[1:]

            self.message_binary = self.message_binary.encode('utf-8')

            self.result = self.image_binary + self.delimiter + self.message_binary

            insertion_success()

        def insertion_success():
            success_message = Label(self.second_frame, text = "\nInsertion successful!")
            success_message.pack()

            new_image_path_prompt = Label(self.second_frame, text = "\nPlease specify the path to save the new image file:")
            new_image_path_prompt.pack()

            self.new_image_entry_box = Entry(self.second_frame)
            self.new_image_entry_box.bind("<Return>", save_file)
            self.new_image_entry_box.pack()
            self.new_image_entry_box.focus_set()

            self.new_path_browse_button = Button(self.second_frame, text = "Browse", command = choose_path)
            self.new_path_browse_button.pack()

            self.save_button = Button(self.second_frame, text = "Save", command = save_file)
            self.save_button.pack()

        def choose_path():
            try:
                self.new_image_path = filedialog.asksaveasfilename(defaultextension = '.png')
                self.new_image_entry_box.delete(0, END)
                self.new_image_entry_box.insert(0, f"{self.new_image_path}")

                if self.new_image_path == () or self.new_image_path == "":
                    self.new_image_entry_box.delete(0, END)
                    showinfo("Invalid Input", "You have not specified the filename.")

                elif self.new_image_path[-4:] != ".png":
                    raise TypeError

            except TypeError:
                self.new_image_entry_box.delete(0, END)
                showinfo("Invalid Input", "The file you have chosen is not compatible.")

        def save_file(event = 1):
            try:
                self.new_image_path = self.new_image_entry_box.get()

                if self.new_image_path == "":
                    showinfo("Invalid Input", "You have not chosen a file.")

                elif self.new_image_path[-4:] != ".png":
                    raise TypeError

                else:
                    with open(self.new_image_path, "wb") as self.new_image:
                        self.new_image.write(self.result)
                    final_success()

            except TypeError:
                self.new_image_entry_box.delete(0, END)
                showinfo("Invalid Input", "The file you specified is not compatible.")

        def final_success():
            final_message = Label(
                                  self.second_frame,
                                  text = (
                                          "\nImage successfully saved!"
                                          "\n\n You can retrieve the message "
                                          "you have hidden or another message "
                                          "\nthat have been hidden previously, "
                                          "return to the introduction screen, "
                                          "\nor you can exit the program.\n"
                                         )
                                 )
            final_message.pack()

            self.final_retrieve_button = Button(
                                                self.second_frame,
                                                text = "Retrieve",
                                                command = self.third_screen
                                               )
            self.final_retrieve_button.pack()

            self.return_introduction_button = Button(
                                                     self.second_frame,
                                                     text = "Introduction",
                                                     command = self.introduction_screen
                                                    )
            self.return_introduction_button.pack()

            self.final_exit_button = Button(
                                            self.second_frame,
                                            text = "Exit",
                                            command = self.root.destroy
                                           )
            self.final_exit_button.pack()

        self.first_frame.destroy()
        self.first_frame = Frame(self.root)

        self.second_frame.pack()

        self.current_frame = 2

        message_prompt = Label(self.second_frame, text = "\n\nWrite your message below:")
        message_prompt.pack()

        self.message_entry_box = Entry(self.second_frame, text = "Example message")
        self.message_entry_box.bind("<Return>", message_insertion)
        self.message_entry_box.pack()
        self.message_entry_box.focus_set()

        self.insert_button = Button(self.second_frame, text = "Insert", command = message_insertion)
        self.insert_button.pack()

    def third_screen(self):

        def path_assertion():
            try:
                self.image_path = self.image_name.get()

                if self.image_path == "":
                    showinfo("Invalid Input", "You have not chosen a file.")

                elif self.image_path[-4:] != ".png":
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

                elif self.image_path[-4:] != ".png":
                    raise TypeError

            except TypeError:
                self.image_name.delete(0, END)
                showinfo("Invalid Input", "The file you have chosen is not compatible.")

        def find_message():
            pass

        def find_delimiter():
            pass

        def decrypt_message():
            pass

        if self.current_frame == 0:
            self.introduction_frame.destroy()
            self.introduction_frame = Frame(self.root)

        elif self.current_frame == 2:
            self.second_frame.destroy()
            self.second_frame = Frame(self.root)

        self.third_frame.pack()

    def mainloop(self):
        self.root.mainloop()

def main():
    program_window = Hidden_Message_Creator()
    program_window.mainloop()

if __name__ == '__main__':
    main()
