from tkinter import *
from tkinter import messagebox
import pandas
import random
import string
import json

# ------------------------------#
GRAY = "#6d6d6d"  # Color
FONT = "Courier"  # Font used
FILE = "PASSWORDS.csv"  # File name where the information will be saved to.
# ------------------------------#
# WINDOW
window = Tk()
window.title("Password Maker")  # Name of the window
window.config(bg=GRAY)
window.geometry("400x600")

# ----------------------------------------------------------------------------------------------#

"""FUNCTIONS"""


def web_search():
    website = website_input.get().upper()  # Gets the user's website input.
    try:  # Tries to open the file.
        with open("account_info.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:  # Throws a messagebox if the file cannot be found.
        messagebox.showinfo(title="WEBSITE INFO", message="No Data File Found")

    else:
        if website in data:          
            web = data[website]
            email_input.insert(0, web["email"])
            password_input.insert(0, web["password"])
            messagebox.showinfo(title="WEBSITE INFO", message=f"Website: {website}\nEmail: {web['email']}\n"
                                                              f"Password: {web['password']}\n"
                                                              f"Please use the user input to copy")
        else:
            messagebox.showinfo(title="WEBSITE INFO", message=f"cannot account find information on {website}.")


def save():
    """Saves the information inputted in the FILE. Called by the button SAVE"""
    web = str(website_input.get()).upper()  # Gets the value inputted in the website_input
    email = str(email_input.get())  # Gets the value inputted in the email_input
    pword = str(password_input.get())  # Gets the value inputted in the password_input
    none = ""
    if len(web) == 0 or len(email) == 0 or len(pword) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure all fields are not empty")
    else:

        info = {
            web: {
                "email": email,
                "password": pword
            }
        }
        # only continue if user inputs yes in popup message.
        if messagebox.askokcancel(title="SAVE", message=f"Do you want to save?\n"
                                                        f"WEBSITE: {web}\nEMAIL: {email}\nPASSWORD: {pword}"):
            try:
                with open("account_info.json", "r") as data_file:  # Loads the data if the file exists.
                    data = json.load(data_file)
            except FileNotFoundError:  # If the file does not exist, create the file and dump the info.
                with open("account_info.json", "w") as data_file:
                    json.dump(info, data_file, indent=4)
            else:  # If the file exists, dump the data into the file.
                data.update(info)
                with open("account_info.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
                saved_label.config(
                    text=f"Information has been successfully\nsaved to {FILE}")  # Edits the text in saved_label.
                ok_button.place(x=120, y=550)  # shows the ok button.


def generate_pass():
    """Generates a random password with a given length."""
    length = int(password_len.get())  # Gets the required length from the password_len Entry. Default is 12
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")  # list of random characters
    random.shuffle(characters)  # Shuffles the characters
    password = [random.choice(characters) for num in range(length)]  # list of random combinations of characters
    password_input.delete(0, END)  # Deletes the previous text in the password_input
    password_input.insert(0, "".join(password))  # Inserts the new password generated


def ok():
    """Resets the text in saved_label, and removes the ok button.
    called by the ok button."""
    saved_label.config(text="")
    ok_button.place_forget()


# ----------------------------------------------------------------------------------------------#
"""LABELS"""

website_label = Label(text="Website: ", bg=GRAY, fg="white", font=(FONT, 12, "bold"))
website_label.place(x=25, y=380)

email_label = Label(text="Email: ", bg=GRAY, fg="white", font=(FONT, 12, "bold"))
email_label.place(x=25, y=410)

password_label = Label(text="Password: ", bg=GRAY, fg="white", font=(FONT, 12, "bold"))
password_label.place(x=25, y=440)

password_len_label = Label(text="Length: ", bg=GRAY, fg="white", font=(FONT, 12, "bold"))
password_len_label.place(x=250, y=440)

saved_label = Label(bg=GRAY, fg="white", font=(FONT, 12, "bold"))
saved_label.place(x=25, y=500)

# ----------------------------------------------------------------------------------------------#
"""PADLOCK"""
padlock = Canvas(width=350, height=300, bg=GRAY, highlightthickness=0)
padlock_img = PhotoImage(file="padlock.png")
padlock.create_image(176, 150, image=padlock_img)
padlock.place(x=25, y=25)

# ----------------------------------------------------------------------------------------------#
"""INPUTS"""

website_input = Entry(width=31)
website_input.place(x=120, y=380)
website_input.focus()

email_input = Entry(width=40)
email_input.place(x=120, y=410)

password_input = Entry(width=20)
password_input.place(x=120, y=440)

password_len = Entry(width=5)
password_len.place(x=330, y=440)
password_len.insert(0, "12")

# ----------------------------------------------------------------------------------------------#
"""BUTTONS"""

generate_button = Button(text="GENERATE PASS", bg=GRAY, fg="white", font=(FONT, 8, "bold"), width=15,
                         command=generate_pass)
generate_button.place(x=250, y=470)

save_button = Button(text="SAVE", bg=GRAY, fg="white", font=(FONT, 8, "bold"), width=15, command=save)
save_button.place(x=120, y=470)

ok_button = Button(text="OK", bg=GRAY, fg="white", font=(FONT, 8, "bold"), width=15, command=ok)

search_web_button = Button(text="SEARCH", bg=GRAY, fg="white", font=(FONT, 8, "bold"), width=6,
                           command=web_search)
search_web_button.place(x=315, y=380)
# ----------------------------------------------------------------------------------------------#

window.mainloop()
