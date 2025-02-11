import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(0, "end")
    text_result.insert(0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(0, "end")
        text_result.insert(0, calculation)
    except:
        clear_field()
        text_result.insert(0, "Error")
    pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(0, "end")
    pass

root = tk.Tk()
root.geometry("475x275")
root.title("Simple Calculator")
text_result = tk.Entry(master=root, borderwidth=10, background="white", font=("Arial", 24))
text_result.grid(row=0, columnspan=6, padx=35)


# Row 1

btn_clear = tk.Button(root, text="clear", command=clear_field, width=15, font=("Arial", 14))
btn_clear.grid(row=1, column=1, columnspan=3, sticky=tk.NSEW)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=1, column=4, sticky=tk.NSEW)

# Row 2

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1, sticky=tk.NSEW)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2, sticky=tk.NSEW)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3, sticky=tk.NSEW)

btn_sub = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_sub.grid(row=2, column=4, sticky=tk.NSEW)

# Row 3

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1, sticky=tk.NSEW)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2, sticky=tk.NSEW)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3, sticky=tk.NSEW)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=3, column=4, sticky=tk.NSEW)

# Row 4

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1, sticky=tk.NSEW)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2, sticky=tk.NSEW)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3, sticky=tk.NSEW)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=4, column=4, sticky=tk.NSEW)

# Row 5

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=1, sticky=tk.NSEW)

btn_sum = tk.Button(root, text="=", command=evaluate_calculation, width=15, font=("Arial", 14))
btn_sum.grid(row=5, column=2, columnspan=3, sticky=tk.NSEW)


# MacBook Errors
# https://discussions.apple.com/thread/255761734?sortBy=rank
# 2024-12-15 17:03:49.686 Python[8484:12873852] +[IMKClient subclass]: chose IMKClient_Modern
# 2024-12-15 17:03:49.686 Python[8484:12873852] +[IMKInputSession subclass]: chose IMKInputSession_Modern

root.mainloop()