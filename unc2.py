from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("Calculator")

pole = Entry(root, width=45, borderwidth=3)
pole.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def btn_add(number):
    current = pole.get()
    pole.delete(0, END)
    pole.insert(0, str(current) + str(number))

def btn_clear():
    pole.delete(0, END)

def btn_pl():
    first_n = pole.get()
    global f_n
    global math
    math = "addition"
    f_n = float(first_n)
    pole.delete(0, END)

def btn_equal():
    second_n = pole.get()
    pole.delete(0, END)
    if math == "addition":
        pole.insert(0, f_n + float(second_n))
    if math == "substraction":
        pole.insert(0, f_n - float(second_n))
    if math == "multiplication":
        pole.insert(0, f_n * float(second_n))
    if math == "division":
        if float(second_n) != 0:
            pole.insert(0, f_n / float(second_n))
        else:
            pole.insert(0, "Error")
    if math == "module":
        pole.insert(0, f_n % float(second_n))

def btn_min():
    first_n = pole.get()
    global f_n
    global math
    math = "substraction"
    f_n = float(first_n)
    pole.delete(0, END)

def btn_mult():
    first_n = pole.get()
    global f_n
    global math
    math = "multiplication"
    f_n = float(first_n)
    pole.delete(0, END)

def btn_div():
    first_n = pole.get()
    global f_n
    global math
    math = "division"
    f_n = float(first_n)
    pole.delete(0, END)

def btn_mod():
    first_n = pole.get()
    global f_n
    global math
    math = "module"
    f_n = float(first_n)
    pole.delete(0, END)

def btn_dot():
    current = pole.get()
    if '.' not in current:
        pole.insert(END, '.')

btn_1 = ttk.Button(root, text="1", command=lambda: btn_add(1))
btn_2 = ttk.Button(root, text="2", command=lambda: btn_add(2))
btn_3 = ttk.Button(root, text="3", command=lambda: btn_add(3))
btn_4 = ttk.Button(root, text="4", command=lambda: btn_add(4))
btn_5 = ttk.Button(root, text="5", command=lambda: btn_add(5))
btn_6 = ttk.Button(root, text="6", command=lambda: btn_add(6))
btn_7 = ttk.Button(root, text="7", command=lambda: btn_add(7))
btn_8 = ttk.Button(root, text="8", command=lambda: btn_add(8))
btn_9 = ttk.Button(root, text="9", command=lambda: btn_add(9))
btn_0 = ttk.Button(root, text="0", command=lambda: btn_add(0))
btn_c = ttk.Button(root, text="C", command=btn_clear)
btn_plus = ttk.Button(root, text="+", command=btn_pl)
btn_eq = ttk.Button(root, text="=", command=btn_equal)
btn_dot = ttk.Button(root, text=".", command=btn_dot)

btn_min = ttk.Button(root, text="-", command=btn_min)
btn_mult = ttk.Button(root, text="*", command=btn_mult)
btn_div = ttk.Button(root, text="div", command=btn_div)
btn_mod = ttk.Button(root, text="mod", command=btn_mod)

btn_1.grid(row=2, column=0, pady=5)
btn_2.grid(row=2, column=1)
btn_3.grid(row=2, column=2)
btn_4.grid(row=3, column=0, pady=5)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_7.grid(row=4, column=0, pady=5)
btn_8.grid(row=4, column=1)
btn_9.grid(row=4, column=2)
btn_0.grid(row=5, column=0, pady=5)

btn_c.grid(row=6, column=2)
btn_plus.grid(row=5, column=1)
btn_eq.grid(row=6, column=1)

btn_min.grid(row=5, column=2)
btn_mult.grid(row=6, column=0, pady=5)
btn_div.grid(row=1, column=0, pady=20)

btn_mod.grid(row=1, column=1)
btn_dot.grid(row=1, column=2)

root.mainloop()