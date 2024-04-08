import tkinter as tk


class ArithmeticApp:
    def __init__(self, master):
        self.master = master
        master.title("Арифметические операции")

        self.number = tk.IntVar()
        self.number.set(1)

        self.number_label = tk.Label(master, textvariable=self.number, font=("Arial", 24))
        self.number_label.pack(pady=20)

        self.add_button = tk.Button(master, text="+2", command=self.add_two, font=("Arial", 14))
        self.add_button.pack(side="left", padx=10)

        self.multiply_button = tk.Button(master, text="×3", command=self.multiply_three, font=("Arial", 14))
        self.multiply_button.pack(side="right", padx=10)

    def add_two(self):
        self.number.set(self.number.get() + 2)

    def multiply_three(self):
        self.number.set(self.number.get() * 3)


if __name__ == "__main__":
    root = tk.Tk()
    app = ArithmeticApp(root)
    root.mainloop()
