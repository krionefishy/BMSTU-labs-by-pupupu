import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import *
import logging
logging.basicConfig(level=logging.INFO)
import json
import math
############################ Конфиг
root = tk.Tk()
root.title("Калькулятор функций")
root.configure(bg="black")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

st = ttk.Style()
st.configure("Rounded.TButton",
             padding = 10,
             relief = "raised",
             background = "Orange",
             foreground="white",
             font=("Arial", 12), 
             borderwidth=0,
             focuscolor="none",
             bordercolor="none")
#############################

def show_plot(roots = [], start = None, end = None, func = None, flag = True):
    if not hasattr(show_plot, "figure"):
        show_plot.figure = plt.Figure(figsize=(5, 4), dpi=200)
        show_plot.ax = show_plot.figure.add_subplot(111)
        show_plot.canvas = FigureCanvasTkAgg(show_plot.figure, master=plot_frame)
        show_plot.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        show_plot.ax.set_xlabel("x")
        show_plot.ax.set_ylabel("f(x)")
        show_plot.ax.axhline(0, color='black', linewidth=0.5, linestyle='--') 
        show_plot.ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
        show_plot.ax.grid(True)

    show_plot.ax.clear()
    show_plot.ax.set_xlabel("x")
    show_plot.ax.set_ylabel("f(x)")
    show_plot.ax.axhline(0, color='black', linewidth=1, linestyle='--')  
    show_plot.ax.axvline(0, color='black', linewidth=1, linestyle='--') 
    show_plot.ax.grid(True)
    if not flag:
        show_plot.ax.set_title("Некорректные данные")
    else:
        show_plot.ax.set_title("График функции")
    


    if not flag:
        show_plot.canvas.draw()
        return
    

    if start is not None and end is not None and func is not None:
        dots = np.linspace(start, end, 1000)  

        func_results = []
        valid_dots = []
        for x in dots:
            try:
                y = func(x)
                func_results.append(y)
                valid_dots.append(x)
            except (ValueError, ZeroDivisionError) as e:
                logging.error(f"invalid x was found: {e}")
                continue

        
        show_plot.ax.plot(valid_dots, func_results, label="f(x)")
        show_plot.ax.legend()

    for i in roots:
        show_plot.ax.plot(i, 0, "ro", label = "корни")
    
    show_plot.ax.relim()
    show_plot.ax.autoscale_view()
    show_plot.canvas.draw()



def clear_table():
    logging.log(logging.INFO, "clear table button was recieved")
    for row in table.get_children():
        table.delete(row)


def calculate_and_show():
    a = start_field.get()
    b = end_field.get()
    h = step_field.get()
    nmax = n_field.get()
    eps = eps_field.get()
    func = get_func(func_field.get())
    if func is None:
        return
    
    if (
        check_if_valid(a) and \
        check_if_valid(b) and \
        check_if_valid(h) and \
        check_if_valid(nmax) and \
        check_if_valid(eps) and \
        float(eps) > 0 and \
        float(a) < float(b) and \
        float(h) > 0
    ):
        a = float(a)
        b = float(b)
        h = float(h)
        nmax = int(nmax)
        eps = float(eps)
    else:
        return 
    
    logging.log(logging.INFO, f'recieved result button action: {json.dumps({"a": a, "b": b, "h": h, "n": nmax, "eps": eps})}')
    
    
    clear_table()


    roots = []
    current = a
    flag = True
    while current < b:
        current_next = current + h 
        if current_next > b:
            current_next = b


        root, amount_of_iterations, rc = hord_method(func, current, current_next, nmax, eps)
        if rc == 3:
            flag = False
            break
            
        if root is not None:    
            logging.log(logging.INFO, f'got function result: {json.dumps({"root": root, "iter": amount_of_iterations, "err_code": rc})}')
            roots.append(root)
            table.insert("", "end", values=(
                len(roots),
                f"[{current:.4g};{current_next:.4g}]",
                f"{root:2f}",
                f"{func(root):2f}",
                f"{amount_of_iterations}",
                f"{rc}"
            ))
        
        current = current_next
    show_plot(roots, start=a, end=b, func=func, flag = flag)



def clear_all_fields():
    logging.log(logging.INFO, "recieved clear all fields button")
    func_field.delete(0, tk.END)
    start_field.delete(0, tk.END)
    end_field.delete(0, tk.END)
    step_field.delete(0, tk.END)
    eps_field.delete(0, tk.END)
    n_field.delete(0, tk.END)







input_plot_frame = tk.Frame(root, bg="black", background="black")
input_plot_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

fields_frame = tk.Frame(input_plot_frame, bg="black")
fields_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


tk.Label(fields_frame, text="функция f(x)", width=15, height=5).grid(row=0, column=0, padx=10, pady=5, sticky="w")
func_field = tk.Entry(fields_frame)
func_field.grid(row=0, column=1, padx=10, pady=5)

tk.Label(fields_frame, text="Начало отрезка", width=15, height=5).grid(row=1, column=0, padx=10, pady=5, sticky="w")
start_field = tk.Entry(fields_frame)
start_field.grid(row=1, column=1, padx=10, pady=5)

tk.Label(fields_frame, text="Конец отрезка", width=15, height=5).grid(row=2, column=0, padx=10, pady=5, sticky="w")
end_field = tk.Entry(fields_frame)
end_field.grid(row=2, column=1, padx=10, pady=5)

tk.Label(fields_frame, text="Шаг", width=15, height=5).grid(row=3, column=0, padx=10, pady=5, sticky="w")
step_field = tk.Entry(fields_frame)
step_field.grid(row=3, column=1, padx=10, pady=5)

tk.Label(fields_frame, text="Точность", width=15, height=5).grid(row=4, column=0, padx=10, pady=5, sticky="w")
eps_field = tk.Entry(fields_frame)
eps_field.grid(row=4, column=1, padx=10, pady=5)

tk.Label(fields_frame, text="N разбиений", width=15, height=5).grid(row=5, column=0, padx=10, pady=5, sticky="w")
n_field = tk.Entry(fields_frame)
n_field.grid(row=5, column=1, padx=10, pady=5)


result_button = ttk.Button(fields_frame, text="=", command=calculate_and_show, style = "Rounded.TButton")
result_button.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")

clear_fields_button = ttk.Button(fields_frame, text="Очистить все", command=clear_all_fields, style = "Rounded.TButton")
clear_fields_button.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

clear_table_button = ttk.Button(fields_frame, text="Очистить таблицу", command=clear_table, style="Rounded.TButton")
clear_table_button.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")


plot_frame = tk.Frame(input_plot_frame, bg="black")
plot_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


table_frame = tk.Frame(root, bg="black")
table_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


columns = ("№ корня", "[x_i; x_i+1]", "x'", "f(x')", "Итерации", "Код ошибки")
table = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
table.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    show_plot()
    root.mainloop()
    logging.log(logging.INFO, "calc app is running")


