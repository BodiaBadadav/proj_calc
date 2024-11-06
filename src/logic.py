class CalculatorLogic:
    def __init__(self, ui):
        self.ui = ui

    def add_to_display(self, value):
        current = self.ui.display.get()
        self.ui.display.delete(0, 'end')
        self.ui.display.insert('end', current + str(value))

    def calculate(self):
        try:
            result = eval(self.ui.display.get())
            self.ui.display.delete(0, 'end')
            self.ui.display.insert('end', str(result))
        except Exception:
            self.ui.display.delete(0, 'end')
            self.ui.display.insert('end', "Ошибка")

    def clear(self):
        self.ui.display.delete(0, 'end')
