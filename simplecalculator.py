import tkinter as tk



cal = ""

def add_to_cal(symbol):
    global cal
    if symbol == "(" and cal and cal[-1].isdigit():
        cal += "*"
        if symbol == ")" and cal.count("(") <= cal.count(")"):
            return
    cal += str(symbol)
    text.delete(1.0, "end")
    print(f"Current Calculation: {cal}")
    text.insert(1.0, cal)

def eva_cal():
     global cal
     try:
         cal = str(eval(cal))
         text.delete(1.0, "end")
         print(f"Current Answer: {cal}")
         text.insert(1.0, cal)
         text
     except Exception as e:
         print(f"Unable To Calculate: {e}")
         clear_field()
         text.insert(1.0, "Error")


def clear_field():
    global cal
    print("Cleared!")
    cal = ""
    text.delete(1.0, "end"),


root = tk.Tk()
root.geometry("320x275")
root.title("Best Calculator Ever")

text = tk.Text(root, height=2, width=16, font=("Arial", 24))
text.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_cal(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_cal(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_cal(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_cal(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_cal(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_cal(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_cal(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_cal(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_cal(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_cal(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_cal("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_cal("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_cal("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_cal("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)
btn_op = tk.Button(root, text="(", command=lambda: add_to_cal("("), width=5, font=("Arial", 14))
btn_op.grid(row=5, column=1)
btn_cl = tk.Button(root, text=")", command=lambda: add_to_cal(")"), width=5, font=("Arial", 14))
btn_cl.grid(row=5, column=3)
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_eq = tk.Button(root, text="=", command=eva_cal, width=11, font=("Arial", 14))
btn_eq.grid(row=6, column=3, columnspan=2)
root.mainloop()