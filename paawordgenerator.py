from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string
import random

# Initialize the main window
root = Tk()
root.geometry("500x500")
root.title("Password Generator")
root.config(bg="skyblue")
root.resizable(False, False)

# Function to generate the password
def password_generate():
    try:
        length_password = solidboss.get()
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation
        all_characters = small_letters + capital_letters + digits + special_characters
        password_list = random.sample(all_characters, length_password)
        random.shuffle(password_list)
        generated_password = "".join(password_list)
        password.set(generated_password)
        check_strength(generated_password)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to check the strength of the generated password
def check_strength(pwd):
    strength = "Weak"
    if len(pwd) >= 8:
        if any(char in string.ascii_lowercase for char in pwd) and \
           any(char in string.ascii_uppercase for char in pwd) and \
           any(char in string.digits for char in pwd) and \
           any(char in string.punctuation for char in pwd):
            strength = "Strong"
        elif any(char in string.ascii_lowercase for char in pwd) or \
             any(char in string.ascii_uppercase for char in pwd) or \
             any(char in string.digits for char in pwd) or \
             any(char in string.punctuation for char in pwd):
            strength = "Medium"
    strength_label.config(text=f"Strength: {strength}")

# Function to copy the password to the clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Function to clear the password
def clear_password():
    password.set("")
    strength_label.config(text="Strength:")

# Options for password length
all_no = {str(i): str(i) for i in range(1, 31)}

# UI Elements
Title = Label(root, text="Password Generator", bg="skyblue", fg="black", font=("futura", 15, "bold"))
Title.pack(anchor="center", pady="20px")

length = Label(root, text="Length of Your Password:", fg="darkgreen", bg="skyblue", font=("ubuntu", 12))
length.place(x="20px", y="70px")

solidboss = IntVar()
Selector = Combobox(root, textvariable=solidboss, state="readonly")
Selector['values'] = list(all_no.keys())
Selector.current(7)
Selector.place(x="220px", y="72px")

generate_btn = Button(root, text="Generate Password", bg="black", fg="white", font=("ubuntu", 15), cursor="hand2", command=password_generate)
generate_btn.pack(anchor="center", pady="50px")

result_label = Label(root, text="Generated Password:", bg="skyblue", fg="darkgreen", font=("ubuntu", 12))
result_label.place(x="20px", y="160px")

password = StringVar()
password_final = Entry(root, textvariable=password, state="readonly", fg="black", font=("ubuntu", 15))
password_final.place(x="180px", y="160px")

strength_label = Label(root, text="Strength:", bg="skyblue", fg="darkgreen", font=("ubuntu", 12))
strength_label.place(x="20px", y="200px")

copy_btn = Button(root, text="Copy to Clipboard", bg="blue", fg="white", font=("ubuntu", 12), cursor="hand2", command=copy_to_clipboard)
copy_btn.place(x="50px", y="240px")

clear_btn = Button(root, text="Clear", bg="red", fg="white", font=("ubuntu", 12), cursor="hand2", command=clear_password)
clear_btn.place(x="250px", y="240px")

# Bind events for button hover effect
def on_enter(e):
    generate_btn['bg'] = "grey"
    generate_btn['fg'] = "white"

def on_leave(e):
    generate_btn['bg'] = "black"
    generate_btn['fg'] = "white"   

generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

# Run the main loop
root.mainloop()
