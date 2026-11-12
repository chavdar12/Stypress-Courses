import random
import tkinter as tk
from tkinter import ttk

WORDS = ["python", "tkinter", "dictionary", "function", "variable", "exception", "iterator", "database"]
MAX_MISTAKES = 6


class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = set()
        self.mistakes = 0

    def guess(self, letter):
        if letter in self.guessed or self.is_over():
            return
        self.guessed.add(letter)
        if letter not in self.word:
            self.mistakes += 1

    def masked(self):
        return " ".join(ch if ch in self.guessed else "_" for ch in self.word)

    def is_won(self):
        return set(self.word) <= self.guessed

    def is_over(self):
        return self.is_won() or self.mistakes >= MAX_MISTAKES


game = Hangman("abc")
for letter in "axb":
    game.guess(letter)
assert game.masked() == "a b _" and game.mistakes == 1 and not game.is_over()
game.guess("c")
assert game.is_won()


class App:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=200, height=220, bg="white")
        self.canvas.pack(pady=5)
        self.word_label = ttk.Label(root, font=("Courier", 20))
        self.word_label.pack()
        self.status = ttk.Label(root)
        self.status.pack(pady=5)
        letters = ttk.Frame(root)
        letters.pack(padx=5, pady=5)
        self.buttons = {}
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            button = ttk.Button(letters, text=letter, width=3, command=lambda l=letter: self.guess(l))
            button.grid(row=i // 9, column=i % 9)
            self.buttons[letter] = button
        ttk.Button(root, text="New game", command=self.new_game).pack(pady=5)
        root.bind("<Key>", lambda event: self.guess(event.char.lower()))
        self.new_game()

    def new_game(self):
        self.game = Hangman(random.choice(WORDS))
        for button in self.buttons.values():
            button.state(["!disabled"])
        self.refresh()

    def guess(self, letter):
        if letter in self.buttons:
            self.game.guess(letter)
            self.buttons[letter].state(["disabled"])
            self.refresh()

    def refresh(self):
        self.word_label.config(text=self.game.masked())
        self.draw()
        if self.game.is_won():
            self.status.config(text="You win!")
        elif self.game.is_over():
            self.status.config(text=f"You lose! The word was '{self.game.word}'")
        else:
            self.status.config(text=f"Mistakes: {self.game.mistakes}/{MAX_MISTAKES}")

    def draw(self):
        c = self.canvas
        c.delete("all")
        c.create_line(20, 210, 180, 210)
        c.create_line(50, 210, 50, 20, 130, 20, 130, 45)
        parts = [
            lambda: c.create_oval(115, 45, 145, 75),
            lambda: c.create_line(130, 75, 130, 140),
            lambda: c.create_line(130, 90, 105, 115),
            lambda: c.create_line(130, 90, 155, 115),
            lambda: c.create_line(130, 140, 110, 180),
            lambda: c.create_line(130, 140, 150, 180),
        ]
        for part in parts[:self.game.mistakes]:
            part()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hangman")
    App(root)
    root.mainloop()
