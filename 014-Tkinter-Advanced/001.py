import math
import operator
import tkinter as tk
from tkinter import ttk

OPERATIONS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


class Calculator:
    def __init__(self):
        self.memory = 0.0
        self.all_clear()

    def all_clear(self):
        self.display = "0"
        self.accumulator = None
        self.pending = None
        self.new_entry = True

    def clear_entry(self):
        self.display = "0"
        self.new_entry = True

    def value(self):
        return float(self.display)

    def show(self, number):
        self.display = str(int(number)) if float(number).is_integer() else repr(round(number, 10))
        self.new_entry = True

    def digit(self, d):
        if self.display == "Error":
            self.all_clear()
        if self.new_entry or self.display == "0":
            self.display = d
        else:
            self.display += d
        self.new_entry = False

    def point(self):
        if self.new_entry:
            self.display, self.new_entry = "0", False
        if "." not in self.display:
            self.display += "."

    def safe(self, action):
        try:
            action()
        except (ValueError, ZeroDivisionError, OverflowError):
            self.all_clear()
            self.display = "Error"

    def operation(self, op):
        self.safe(lambda: self._operation(op))

    def _operation(self, op):
        if self.pending and not self.new_entry:
            self._equals()
        self.accumulator, self.pending, self.new_entry = self.value(), op, True

    def equals(self):
        self.safe(self._equals)

    def _equals(self):
        if self.pending:
            self.show(OPERATIONS[self.pending](self.accumulator, self.value()))
            self.accumulator, self.pending = None, None

    def negate(self):
        if self.display not in ("0", "Error"):
            self.display = self.display[1:] if self.display.startswith("-") else "-" + self.display

    def sqrt(self):
        self.safe(lambda: self.show(math.sqrt(self.value())))

    def factorial(self):
        def run():
            number = self.value()
            if not number.is_integer() or number > 170:
                raise ValueError
            self.show(math.factorial(int(number)))
        self.safe(run)

    def memory_clear(self):
        self.memory = 0.0

    def memory_plus(self):
        self.safe(lambda: setattr(self, "memory", self.memory + self.value()))
        self.new_entry = True

    def memory_minus(self):
        self.safe(lambda: setattr(self, "memory", self.memory - self.value()))
        self.new_entry = True

    def memory_recall(self):
        self.show(self.memory)


def press(calc, keys):
    actions = {"+": None, "-": None, "*": None, "/": None, "=": calc.equals, ".": calc.point,
               "±": calc.negate, "√": calc.sqrt, "!": calc.factorial, "CE": calc.clear_entry,
               "AC": calc.all_clear, "mc": calc.memory_clear, "m+": calc.memory_plus,
               "m-": calc.memory_minus, "mr": calc.memory_recall}
    for key in keys:
        if key.isdigit():
            calc.digit(key)
        elif key in OPERATIONS:
            calc.operation(key)
        else:
            actions[key]()
    return calc.display


assert press(Calculator(), ["1", "2", "+", "3", "="]) == "15"
assert press(Calculator(), ["2", "+", "3", "*", "4", "="]) == "20"  # chained left to right, like a pocket calculator
assert press(Calculator(), ["9", "√"]) == "3"
assert press(Calculator(), ["5", "!"]) == "120"
assert press(Calculator(), ["1", "/", "0", "="]) == "Error"
assert press(Calculator(), ["5", "±"]) == "-5"
assert press(Calculator(), ["1", ".", "5", "*", "2", "="]) == "3"
assert press(Calculator(), ["5", "m+", "3", "m-", "AC", "mr"]) == "2"
assert press(Calculator(), ["5", "+", "7", "CE", "3", "="]) == "8"

BUTTONS = [
    ["mc", "m+", "m-", "mr"],
    ["AC", "CE", "√", "!"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["±", "0", ".", "+"],
    ["="],
]

if __name__ == "__main__":
    calc = Calculator()
    root = tk.Tk()
    root.title("Calculator")
    display = tk.StringVar(value=calc.display)
    ttk.Label(root, textvariable=display, anchor="e", font=("Helvetica", 22), relief="sunken") \
        .grid(row=0, column=0, columnspan=4, sticky="we", padx=5, pady=5)

    def click(key):
        press(calc, [key])
        display.set(calc.display)

    for r, row in enumerate(BUTTONS, start=1):
        for c, key in enumerate(row):
            ttk.Button(root, text=key, command=lambda k=key: click(k)) \
                .grid(row=r, column=c, columnspan=4 if len(row) == 1 else 1, sticky="we", padx=2, pady=2)
    root.mainloop()
