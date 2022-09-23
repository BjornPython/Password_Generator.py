from tkinter import *
import pandas
GRAY = "#6d6d6d"
FONT = ("Courier")
# WINDOW
window = Tk()
window.title("Password Maker")
window.config(bg=GRAY)
window.geometry("400x600")

def save():
    web = website_input.get()
    email = email_input.get()
    pword = password_input.get()
    print(web,email,pword)
    dictionary = {
        "website: ": web,
        "email: ": email,
        "password: ": pword
    }
    print(dictionary)
    pass_file = pandas.DataFrame.from_dict(dictionary)
    pass_file.to_csv("PASSWORDS.csv", index = False, header=True)



# LABELS

website_label = Label(text="Website: ", bg=GRAY, fg="white", font=(FONT, 12, "bold"))
website_label.place(x=25, y=380)

email_label = Label(text="Email: ", bg=GRAY, fg="white", font=(FONT, 12, "bold"))
email_label.place(x=25, y=410)

password_label = Label(text="Password: ", bg=GRAY, fg="white", font=(FONT, 12, "bold"))
password_label.place(x=25, y=440)

password_len_label = Label(text="Length: ", bg=GRAY, fg="white", font=(FONT, 12, "bold"))
password_len_label.place(x=250, y=440)

# PADLOCK
padlock = Canvas(width=350, height=300, bg=GRAY, highlightthickness=0)
padlock_img = PhotoImage(file="padlock.png")
padlock.create_image(176, 150, image=padlock_img)
padlock.place(x=25, y=25)

website_input = Entry(width=40)
website_input.place(x=120, y=380)
website_input.focus()

email_input = Entry(width=40)
email_input.place(x=120, y=410)

password_input = Entry(width=20)
password_input.place(x=120, y=440)

password_len = Entry(width=5)
password_len.place(x=330, y=440)


generate_button = Button(text="GENERATE PASS", bg=GRAY, fg="white", font=(FONT, 8, "bold"), width=15)
generate_button.place(x=250, y=470)

save_button = Button(text="SAVE", bg=GRAY, fg="white", font=(FONT, 8, "bold"), width=15, command=save)
save_button.place(x=120, y=470)

window.mainloop()
