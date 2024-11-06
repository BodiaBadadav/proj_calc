from ui import CalculatorUI
import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.ui = CalculatorUI(root)

    def run(self):
        self.ui.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    app.run()
