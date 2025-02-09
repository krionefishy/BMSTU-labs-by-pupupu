#Лабораторная работа №1
# Калькулятор вещественных чисел в пятиричной системе счисления
# Подготовил Кошеваров Дмитрий ИУ7-26Б
# Вариант 20

import tkinter as tk
from funcs_and_culcs import *


root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")


def create_button(nob: str, wob: int, hob: int, button_command):
    res = tk.Button(
                root,
                text=nob, 
                width=wob,
                height=hob, 
                command=button_command,
                bg="orange",
                fg="white")
    return res
    

def clear_all_fields():
    num1_button.delete(0, tk.END)
    num2_button.delete(0, tk.END)
    operation_button.delete(0, tk.END)
    res.delete(0, tk.END)

def add_char(char):
    act_button = root.focus_get()
    if act_button in (num1_button, num2_button, operation_button):
        act_button.insert(tk.END, char)

    
def delete_last_char():
    act_button = root.focus_get()
    if act_button in (num1_button, num2_button, operation_button):
        act_button.delete(len(act_button.get()) - 1, tk.END)
        
        
def clear_current_field():
    act_button = root.focus_get()
    if act_button in (num1_button, num2_button, operation_button):
        act_button.delete(0, tk.END)
        
def get_result():
    num1 = num1_button.get()
    num2 = num2_button.get()
    operation = operation_button.get()
    
    num1 = "0" if len(num1) == 0 or num1 == "-" or num1 == "+" else num1 
    num2 = "0" if len(num2) == 0 or num2 == "-" or num2 == "+" else num2 
    if check_if_valid(num1, operation, num2):
        if operation == "-":
            result  = calc_minus(num1, num2)
        if operation == "+":
            result = calc_plus(num1, num2)
    else:
        result = "Invalid operation"

    res.focus()
    res.delete(0, tk.END)
    res.insert(0, result)
    




num1_button = tk.Entry(root, width=13, font=("Courier", 10))
num1_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

operation_button = tk.Entry(root, width=5, font=("Courier", 10))
operation_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

num2_button = tk.Entry(root, width=13, font=("Courier", 10))
num2_button.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

res = tk.Entry(root, width=13, font=("Courier", 10))
res.grid(row = 0, column=3, padx=5, pady=5, sticky="nsew")

keyboard_buttons = ["C", "A", "BK", "0", 
                    "1", "2", "3", "4",
                    "+", "-", ".", "="]


for i in range(4): 
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)
    
current_row = 1
current_col = 0

for i in keyboard_buttons:
    if i == "C":
        create_button(i, 10, 1, clear_all_fields).grid(row=current_row, column=current_col, padx=5, pady=5, sticky="nsew")
    elif i == "A":
        create_button(i, 10, 1,clear_current_field).grid(row=current_row, column=current_col, padx=5, pady=5, sticky="nsew") 
    elif i == "BK":
        create_button(i, 10, 1, delete_last_char).grid(row=current_row, column=current_col, padx=5, pady=5, sticky="nsew")
    elif i == "=":
        create_button(i, 10, 1, get_result).grid(row=current_row, column=current_col, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(
                root, 
                text=i, 
                width=10,
                height=1, 
                command=lambda button = i: add_char(button),
                bg="orange",
                fg="white").grid(row=current_row, column=current_col, padx=5, pady=5, sticky="nsew")
    current_col += 1
    if current_col == 4:
        current_col = 0
        current_row += 1
        
        
        
if __name__ == "__main__":
    root.mainloop()
    