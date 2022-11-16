import tkinter as tk
from tkinter import E, W

# Initialization
window = tk.Tk()

# Title
window.title("This is my app")


# Labels
lbl_fahrenheit = tk.Label(
    master=window,
    text="Fahrenheit: ",
    height=3,
    width=15,
)
lbl_celsius = tk.Label(
    master=window,
    text="Celsius",
)
lbl_result = tk.Label(
    master=window,
    text="Result will be shown here...",
)


# Entries
ent_fahrenheit = tk.Entry(
    master=window,
    width=40,
)


def temp_calc(*args):
    try:
        if ent_fahrenheit.get() == "":
            lbl_result['text'] = "Input is empty..."
        else:
            lbl_result['text'] = (int(ent_fahrenheit.get())-32) * (5/9)
    except ValueError:
        lbl_result['text'] = "You should enter a number!"


# Buttons
btn_calc = tk.Button(
    master=window,
    text="Calc",
    width=8,
    command=temp_calc,
)

window.bind("<Return>", temp_calc)


# Show Widgets
lbl_fahrenheit.grid(row=0, column=0)
ent_fahrenheit.grid(row=0, column=1)
btn_calc.grid(row=0, column=2, padx=(20, 10))
lbl_celsius.grid(row=1, column=0, pady=(2, 10))
lbl_result.grid(row=1, column=1, pady=(2, 10))


# Run
window.mainloop()
