import tkinter as tk

# Создаем основное окно приложения
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

# Поле для отображения
display = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Функции для обработки нажатий
def click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(value))

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Ошибка")

def clear():
    display.delete(0, tk.END)

# Кнопки калькулятора
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 1, 0
for button in buttons:
    action = lambda x=button: click(x) if x != "=" else calculate() if x == "=" else clear()
    tk.Button(root, text=button, command=action, font=("Arial", 18), width=4, height=2).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Запуск основного цикла
root.mainloop()
