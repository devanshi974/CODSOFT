from tkinter import *
import random
import string

root = Tk()
root.geometry("600x300")
root.title("Password Generator")

pass_str = StringVar()
pass_output = Label(root, textvariable=pass_str)
pass_output.pack()

pwd_len = IntVar()
pwd_len.set(0)

def get_pass():                                    
    length = pwd_len.get()
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars)for i in range(length))
    pass_str.set(password)

Label(root, text = "TO  GENERATE  PASSWORD", font="calibri 18 bold").pack()
Label(root, text = "Enter Length of Password", font="calibri 13").pack(pady=9)
Entry(root, textvariable=pwd_len).pack(pady=2)
Button(root, text="Generate Password", font="calibri 13", command=get_pass).pack(pady=15)
Entry(root, textvariable=pass_str).pack(pady=2)

root.mainloop()