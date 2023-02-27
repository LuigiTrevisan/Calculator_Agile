import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator Agile")

        self.display = tk.Entry(master, width=25, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 1
        col = 0

        for button in buttons:
            command = lambda x=button: self.handle_click(x)
            tk.Button(master, text=button, width=5, command=command).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def handle_click(self, key):
        if key == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif key == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()