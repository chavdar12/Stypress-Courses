import tkinter as tk
from tkinter import ttk


def bmi(weight, height):
    return weight / height ** 2


def category(value):
    if value < 18.5:
        return "Underweight"
    if value < 25:
        return "Normal weight"
    if value < 30:
        return "Overweight"
    return "Obesity"


assert round(bmi(70, 1.75), 1) == 22.9 and category(22.9) == "Normal weight"
assert category(17) == "Underweight" and category(27) == "Overweight" and category(31) == "Obesity"


def calculate():
    try:
        height, weight = float(height_entry.get()), float(weight_entry.get())
        if height <= 0 or weight <= 0:
            raise ValueError
    except ValueError:
        result.set("Enter positive numbers")
        return
    value = bmi(weight, height)
    result.set(f"BMI: {value:.1f} ({category(value)})")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("BMI Calculator")
    ttk.Label(root, text="Height (m):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    height_entry = ttk.Entry(root)
    height_entry.grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    weight_entry = ttk.Entry(root)
    weight_entry.grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(root, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2, pady=5)
    result = tk.StringVar()
    ttk.Label(root, textvariable=result).grid(row=3, column=0, columnspan=2, pady=5)
    root.mainloop()
