import tkinter as tk


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Error: division by zero!")
                return
            result = num1 / num2
        else:
            result = 0
        result_label.config(text=f"Result: {result} ")
    except ValueError:
        result_label.config(text="Please enter a numeric value")


root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.iconbitmap(default="fish.ico")

input_frame = tk.Frame(root)
input_frame.pack(pady=100)

tk.Label(input_frame, text="Enter the first number:").grid(row=0, column=0)
entry1 = tk.Entry(input_frame)
entry1.grid(row=0, column=1)

tk.Label(input_frame, text="Enter the second number:").grid(row=1, column=0)
entry2 = tk.Entry(input_frame)
entry2.grid(row=1, column=1)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

tk.Button(
    buttons_frame,
    text="+ Add",
    command=lambda: calculate("+"),
    width=8).grid(
        row=0,
        column=0,
    padx=2)
tk.Button(
    buttons_frame,
    text="- Subtract",
    command=lambda: calculate("-"),
    width=8).grid(
        row=0,
        column=1,
    padx=2)
tk.Button(
    buttons_frame,
    text="* Multiply",
    command=lambda: calculate("*"),
    width=8).grid(
        row=0,
        column=2,
    padx=2)
tk.Button(
    buttons_frame,
    text="/ Divide",
    command=lambda: calculate("/"),
    width=8).grid(
        row=0,
        column=3,
    padx=2)

result_label = tk.Label(root, text="Result: ")
result_label.pack()
root.mainloop()
