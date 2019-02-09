from tkinter import *

# Class untuk objek user
class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def get_userdata(self):
        return("Nama: {}\nEmail: {}".format(self.name, self.email))

# Class yang akan mengimplementasi GUI
class AccountManager:
    def __init__(self):
        self.root = Tk()

        # TO-DO Create Input Fields (complete this)
        self.name_field = Entry(self.root)
        self.email_id_field = Entry(master = self.root)
        self.password_field = Entry(master = self.root, show = "*") # Hint: use show="*"

        # TO-DO Create message label and buttons needed
        self.feedback_message = Label(master = self.root)
        self.delete_button = Button(master = self.root, text = "Delete Account", command = self.delete_account)
        self.create_button = Button(master = self.root, text = "Create Account", command = self.create_account)

        # TO-DO Create other necessary variables (if needed)
        self.accounts = {}

        self.create_gui()
        self.name_field.focus_set()


    def create_account(self):
        """
        Creates an account and stores it in the database,
        given valid credentials.
        """

        # TO-DO collect the input data
        name = self.name_field.get()
        email = self.email_id_field.get()
        password = self.password_field.get()

        # TO-DO implement the logic for creating an account
        if name == "" or email == "" or password == "":
            self.feedback_message.configure(text = "Please fill all the fields.")
        elif email in self.accounts:
            self.feedback_message.configure(text = "An account with this e-mail has been registered.")
            self.reset()
        else:
            user = User(name, email, password)
            self.accounts[email]= user
            self.feedback_message.configure(text = "Account {} has successfully been created.".format(name))
            self.reset()


    def delete_account(self):
        """
        Deletes an account from the database, given valid credentials.
        """

        # TO-DO collect the input data
        name = self.name_field.get()
        email = self.email_id_field.get()
        password = self.password_field.get()

        # TO-DO implement the logic for deleting an account
        if email in self.accounts:
            if name == self.accounts[email].name and password == self.accounts[email].password:
                deleted_user = self.accounts[email].name
                del self.accounts[email]
                self.feedback_message.configure(text = "Account {} has been deleted.".format(deleted_user))
                self.reset()
            else:
                self.feedback_message.configure(text = "Invalid credentials.")
                self.reset()
        else:
            self.feedback_message.configure(text = "Invalid credentials.")
            self.reset()


    def create_gui(self):
        """Initialize the layout."""

        # TO-DO complete this
        self.root.title("Account Manager")
        self.root.geometry("400x200")  # Set window size.

        # Create labels
        heading = Label(self.root, text="Manage your Account")
        name = Label(self.root, text="Name")
        email_id = Label(self.root, text="Email")
        password = Label(self.root, text="Password")

        # TO-DO Place labels in window
        heading.grid(row=1, column=1, ipadx="100")
        name.grid(row=3, column=0)
        email_id.grid(row=5, column=0)
        password.grid(row=7, column=0)

        # TO-DO Place input fields in window
        # Complete this
        self.name_field.grid(row=3, column=1, ipadx="100")
        self.email_id_field.grid(row=5, column=1, ipadx="100")
        self.password_field.grid(row=7, column=1, ipadx="100")

        # TO-DO Place message and submit button
        self.feedback_message.grid(row=9, column=1)
        self.delete_button.grid(row=11, column=1)
        self.create_button.grid(row=13, column=1)


    def reset(self):
        """Clears all the fields and move focus back to name."""
        self.name_field.focus_set()
        self.name_field.delete(0, END)

        # TO-DO complete this
        self.email_id_field.focus_set()
        self.email_id_field.delete(0, END)

        self.password_field.focus_set()
        self.password_field.delete(0, END)

        self.name_field.focus_set()

    def mainloop(self):
        """Starts the app"""
        self.root.mainloop()

if __name__ == "__main__":
    app = AccountManager()
    app.mainloop()

    #TO-DO implement cetak akun-akun
    counter = 1
    for account in app.accounts:
        print("User ke-{}:".format(counter))
        print(app.accounts[account].get_userdata() + "\n")
        counter += 1
