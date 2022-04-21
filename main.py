import tkinter
from tkinter import messagebox
import random
# import pyperclip


FONT_INFO = ("Arial", 16)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # Pyperclip automatically ctrl+c the new password 
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# def save_password():
#     website = website_entry.get()
#     email = email_un_entry.get()
#     pw = password_entry.get()
    
#     if len(website) == 0 or len(pw) == 0 or len(email) == 0:
#         messagebox.showerror(title="Oh noes...", message="You shant leave any fields empty")
#     else:
#         # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nWebsite: {website}\nEmail: {email}\nPassword: {pw}\nIs it okay to save?")
#         # if is_ok:
#             with open("data.txt", "a") as d:
#                 d.write(f"{website} | {email} | {pw} \n")
#             password_entry.delete(0, 'end')
#             website_entry.delete(0, 'end')
#             messagebox.showinfo(title="Accepted", message="Accepted")
            
# ----------------------- SAVE PASSWORD WITH JSON (BETTER) ----------------------- #
import json

def save_password():
    website = website_entry.get()
    email = email_un_entry.get()
    pw = password_entry.get()
    new_data = {website: {
                    "email": email,
                    "password": pw
                }}
    
    if len(website) == 0 or len(pw) == 0 or len(email) == 0:
        messagebox.showerror(title="Oh noes...", message="You shant leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        
        else:
            # Updating old data with new data
            data.update(new_data)
            
            # Saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                
        finally:
            password_entry.delete(0, 'end')
            website_entry.delete(0, 'end')
            messagebox.showinfo(title="Accepted", message="Accepted")
            
            
# ---------------------------- SEARCH FUNCTION ------------------------------- #

def search():
    try:
        website = website_entry.get()
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            pw = data[website]["password"]
            messagebox.showinfo(title=website, message=f"For {website}:\nEmail: {email}\nPassword: {pw}")
    except FileNotFoundError:
        messagebox.showerror(title="Not Found", message="No entries have been made yet")
        
    except KeyError:
        messagebox.showerror(title="Not Found", message="This website does not have an entry yet")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

img = tkinter.PhotoImage(file="logo.png")

canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


website_label = tkinter.Label(text="Website:", font=FONT_INFO)
website_label.grid(row=1, column=0)
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tkinter.Button(text="Search", command=search, width=13)
search_button.grid(row=1, column=2)

email_un_label = tkinter.Label(text="Email/Username:", font=FONT_INFO)
email_un_label.grid(row=2, column=0)
email_un_entry = tkinter.Entry(width=38)
email_un_entry.grid(row=2, column=1, columnspan=2)
email_un_entry.insert(0, "seanthewonderful@gmail.com")

password_label = tkinter.Label(text="Password:", font=FONT_INFO)
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

gen_pw_button = tkinter.Button(text="Generate Password", command=gen_password)
gen_pw_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", command=save_password, width=36)
add_button.grid(row=5, column=1, columnspan=2)



# columnspan, 

window.mainloop()