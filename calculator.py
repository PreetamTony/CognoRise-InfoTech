import tkinter as tk
import math

class ScientificCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('←', 1, 4), ('C', 1, 5),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^', 5, 3),
            ('sqrt', 6, 0), ('log', 6, 1), ('ln', 6, 2), ('pi', 6, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

    def on_button_click(self, value):
        current_display = self.display.get()

        if value == '=':
            try:
                result = eval(current_display)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")

        elif value == 'C':
            self.display.delete(0, tk.END)

        elif value == '←':
            self.display.delete(len(current_display)-1, tk.END)

        elif value == 'sin':
            self.display.insert(tk.END, 'sin(')

        elif value == 'cos':
            self.display.insert(tk.END, 'cos(')

        elif value == 'tan':
            self.display.insert(tk.END, 'tan(')

        elif value == '^':
            self.display.insert(tk.END, '**')

        elif value == 'sqrt':
            self.display.insert(tk.END, 'math.sqrt(')

        elif value == 'log':
            self.display.insert(tk.END, 'math.log10(')

        elif value == 'ln':
            self.display.insert(tk.END, 'math.log(')

        elif value == 'pi':
            self.display.insert(tk.END, 'math.pi')

        else:
            self.display.insert(tk.END, value)

root = tk.Tk()
app = ScientificCalculatorApp(root)
root.mainloop()

