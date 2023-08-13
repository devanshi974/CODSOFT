from tkinter import *

calculation = ""
def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calc():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "ERROR")
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = Tk()
root.geometry("300x275")
root.title("calculator")

text_result = Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = Button(root, text="(", command=lambda: add_to_calc("("), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = Button(root, text=")", command=lambda: add_to_calc(")"), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = Button(root, text="7", command=lambda: add_to_calc(7), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = Button(root, text="8", command=lambda: add_to_calc(8), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = Button(root, text="9", command=lambda: add_to_calc(9), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = Button(root, text="4", command=lambda: add_to_calc(4), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = Button(root, text="5", command=lambda: add_to_calc(5), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = Button(root, text="6", command=lambda: add_to_calc(6), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = Button(root, text="2", command=lambda: add_to_calc(2), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_11 = Button(root, text="+", command=lambda: add_to_calc("+"), width=5, font=("Arial", 14))
btn_11.grid(row=2, column=4)

btn_12 = Button(root, text="-", command=lambda: add_to_calc("-"), width=5, font=("Arial", 14))
btn_12.grid(row=3, column=4)

btn_13 = Button(root, text="*", command=lambda: add_to_calc("*"), width=5, font=("Arial", 14))
btn_13.grid(row=4, column=4)

btn_14 = Button(root, text="/", command=lambda: add_to_calc("/"), width=5, font=("Arial", 14))
btn_14.grid(row=5, column=4)

btn_15 = Button(root, text="1", command=lambda: add_to_calc(1), width=5, font=("Arial", 14))
btn_15.grid(row=5, column=1)

btn_16 = Button(root, text="3", command=lambda: add_to_calc(3), width=5, font=("Arial", 14))
btn_16.grid(row=5, column=3)

btn_17 = Button(root, text=".", command=lambda: add_to_calc("."), width=5, font=("Arial", 14))
btn_17.grid(row=6, column=1)

btn_18 = Button(root, text="0", command=lambda: add_to_calc("0"), width=5, font=("Arial", 14))
btn_18.grid(row=6, column=2)

btn_19 = Button(root, text="%", command=lambda: add_to_calc("%"), width=5, font=("Arial", 14))
btn_19.grid(row=6, column=3)

btn_20 = Button(root, text="=", command=evaluate_calc, width=5, font=("Arial", 14))
btn_20.grid(row=6, column=4)

root.mainloop()