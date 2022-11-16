import tkinter as tk
from tkinter import E, W

# Initialization
window = tk.Tk()

# Title
window.title("This is my app")


# Labels
label_f = tk.Label(
    master=window,
    text="Fahrenheit: ",
    height=3,
    width=15,
)
label_c = tk.Label(
    master=window,
    text="Celsius",
)
label_result = tk.Label(
    master=window,
    text="Result will be shown here...",
)


# Entries
entry_f = tk.Entry(
    master=window,
    width=40,
)


def temp_calc():
    try:
        label_result['text'] = (int(entry_f.get())-32) * (5/9)
    except ValueError:
        label_result['text'] = "You should enter a number!"


# Buttons
button_calc = tk.Button(
    master=window,
    text="Calc",
    width=8,
    command=temp_calc,
)


# Show Widgets
label_f.grid(row=0, column=0)
entry_f.grid(row=0, column=1)
button_calc.grid(row=0, column=2, padx=(20, 10))
label_c.grid(row=1, column=0, pady=(2, 10))
label_result.grid(row=1, column=1, pady=(2, 10))


# Run
window.mainloop()
