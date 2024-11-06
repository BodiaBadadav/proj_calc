import tkinter as tk
from logic import CalculatorLogic

class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.logic = CalculatorLogic(self)

        # Поле отображения
        self.display = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Настройка кнопок
        buttons = [
            '1', '2', '3', '/',
            '4', '5', '6', '*',
            '7', '8', '9', '-',
            'C', '0', '=', '+'
        ]

        for c in range(4): root.columnconfigure(index=c, weight=1)
        for r in range(5): root.rowconfigure(index=r, weight=1)

        row, col = 1, 0
        for button in buttons:
            action = lambda x=button: self.handle_click(x)
            tk.Button(root, text=button, command=action, font=("Arial", 18), width=4, height=2).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def handle_click(self, value):
        if value == "=":
            self.logic.calculate()
        elif value == "C":
            self.logic.clear()
        else:
            self.logic.add_to_display(value)
