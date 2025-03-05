import tkinter as tk
from funcs import get_result

def fetch_result():
    current_field = root.focus_get()
    if current_field == num_field:
        res = get_result(num_field.get())
        res_field.delete(0, tk.END)
        res_field.insert(tk.END, res)
        
        
root = tk.Tk()
root.title("Calculator")


num_field = tk.Entry(root, width = 15, font=("Courier", 10))
num_field.grid(row = 0, column=0, padx = 5, pady = 5)

equal_label = tk.Button(root, text="=", font=("Courier", 10), command=fetch_result)
equal_label.grid(row = 0, column=1, padx = 2, pady = 2)

res_field = tk.Entry(root, width = 15, font=("Courier", 10))
res_field.grid(row = 0, column=2, padx = 5, pady = 5)



if __name__ == "__main__":
    root.mainloop()