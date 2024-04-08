import tkinter as tk


class ChessBoard:
    def __init__(self, master, rows, columns, cell_size):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self._current_color = 'white'

        self.canvas = tk.Canvas(self.master, width=self.rows*self.cell_size, height=self.columns*self.cell_size)
        self.canvas.pack()
        self.draw_board()

    def change_color(self):
        self._current_color = 'black' if self._current_color == 'white' else 'white'

    def draw_board(self):
        for row in range(self.rows):
            for col in range(self.columns):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = col * self.cell_size + self.cell_size, row * self.cell_size + self.cell_size
                self.canvas.create_rectangle((x1, y1), (x2, y2), fill=self._current_color)
                self.change_color()
            self.change_color()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Шахматная доска")
    board = ChessBoard(root, 8, 8, 50)
    root.mainloop()
