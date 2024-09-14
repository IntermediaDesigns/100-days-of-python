import tkinter as tk


def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, str(current) + str(value))


def clear():
    display.delete(0, tk.END)


def operator_click(op):
    global first_number, operator
    current = display.get()
    if current:
        first_number = int(current)
        operator = op
        display.insert(tk.END, op)


def calculate():
    current = display.get()
    if not current or operator not in current:
        return

    parts = current.split(operator)
    if len(parts) != 2:
        return

    first_number = int(parts[0])
    second_number = int(parts[1])

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operator"

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    display.delete(0, tk.END)
    display.insert(tk.END, str(result))


window = tk.Tk()
window.title("Simple GUI Calculator")
window.geometry("350x300")

display = tk.Entry(window, width=25, justify="right", font=("Arial", 14))
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    '1', '2', '3', '/', '4', '5', '6', '*', '7', '8', '9', '-', '0', '.', '=',
    '+'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        cmd = calculate
    elif button in '+-*/':
        cmd = lambda x=button: operator_click(x)
    else:
        cmd = lambda x=button: button_click(x)

    tk.Button(window, text=button, width=5, height=2,
              command=cmd).grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(window, text="C", width=5, height=2, command=clear).grid(row=row,
                                                                   column=col,
                                                                   padx=2,
                                                                   pady=2)

window.mainloop()
