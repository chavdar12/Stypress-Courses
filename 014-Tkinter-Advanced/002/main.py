import tkinter as tk
from pathlib import Path

from gui import CollectionApp
from manager import CollectionManager
from storage import TextFileStorage

if __name__ == "__main__":
    root = tk.Tk()
    CollectionApp(root, CollectionManager(TextFileStorage(Path(__file__).with_name("collection.txt"))))
    root.mainloop()
