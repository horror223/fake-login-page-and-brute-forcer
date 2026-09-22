import tkinter as tk
from tkinter import messagebox
from auth import verify_login


root = tk.Tk()

root.title("Steak Employee Panel")
root.geometry("400x300")
root.maxsize(400, 300)
root.minsize(400, 300)
root.configure(background="white")

title_label = tk.Label(
    root,
    text="Steak Employee Panel",
    bg="white",
    font=("Arial", 16, "bold")
)

title_label.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

messagebox.showinfo(
    "Welcome",
    "Please login to your employee panel"
)

emp_label = tk.Label(
    root,
    text="Employee Login:",
    bg="white"
)

emp_label.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

user_entry = tk.Entry(
    root,
    width=30
)

user_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)

password_label = tk.Label(
    root,
    text="Password:",
    bg="white"
)

password_label.grid(
    row=2,
    column=0,
    padx=10,
    pady=10
)

password_entry = tk.Entry(
    root,
    width=30,
    show="*"
)

password_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=10
)

def check_login():
    if verify_login(user_entry.get(), password_entry.get()):
        messagebox.showinfo(
            "login successful",
            "welcome to the employee panel"
        )
    else:
        messagebox.showerror(
            "login failed",
            "invalid credentials"
        )

        

login_button = tk.Button(
    root,
    text="Login",
    command=check_login
)


login_button.grid(
    row=3,
    column=0,
    columnspan=2,
    padx=10,
    pady=10
)

if __name__ == "__main__":
    root.mainloop()