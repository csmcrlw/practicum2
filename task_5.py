import tkinter as tk


class MovingButtonApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x600")
        self.master.title("Движущаяся кнопка")
        self.master.resizable(False, False)

        self.button_size = 20
        self.x = 300
        self.y = 200

        self.button = tk.Button(master, text=self.get_button_text(), command=self.move_button)
        self.button.focus_set()
        self.button.pack()

        master.bind("<KeyPress>", self.on_key_press)

    def get_button_text(self):
        return f"x={self.x}, y={self.y}, size={self.button_size}"

    def move_button(self):
        self.button.place(x=self.x, y=self.y, width=self.button_size*10, height=self.button_size)

    def on_key_press(self, event):
        if event.char == "w":
            self.y -= 10
        elif event.char == "s":
            self.y += 10
        elif event.char == "a":
            self.x -= 10
        elif event.char == "d":
            self.x += 10
        elif event.char == "i":
            self.button_size = min(200, self.button_size + 5)
        elif event.char == "k":
            self.button_size = max(20, self.button_size - 5)

        self.x = max(0, min(self.x, self.master.winfo_width() - self.button_size))
        self.y = max(0, min(self.y, self.master.winfo_height() - self.button_size))

        self.button.config(text=self.get_button_text())
        self.move_button()


if __name__ == "__main__":
    root = tk.Tk()
    app = MovingButtonApp(root)
    root.mainloop()
