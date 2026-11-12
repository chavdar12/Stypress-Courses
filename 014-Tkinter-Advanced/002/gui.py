import tkinter as tk
from tkinter import messagebox, ttk

from manager import CATEGORIES, FIELDS

ALL = "All"


class CollectionApp:
    def __init__(self, root, manager):
        self.manager = manager
        root.title("Collection Manager")

        top = ttk.Frame(root, padding=5)
        top.pack(fill="x")
        ttk.Label(top, text="Show:").pack(side="left")
        self.filter = ttk.Combobox(top, values=(ALL, *CATEGORIES), state="readonly", width=8)
        self.filter.set(ALL)
        self.filter.bind("<<ComboboxSelected>>", lambda e: self.refresh())
        self.filter.pack(side="left", padx=5)
        self.query = tk.StringVar()
        self.query.trace_add("write", lambda *a: self.refresh())
        ttk.Label(top, text="Search:").pack(side="left", padx=(10, 0))
        ttk.Entry(top, textvariable=self.query).pack(side="left", fill="x", expand=True, padx=5)

        self.table = ttk.Treeview(root, columns=FIELDS, show="headings", height=12)
        for field in FIELDS:
            self.table.heading(field, text=field.title())
        self.table.pack(fill="both", expand=True, padx=5)
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        form = ttk.Frame(root, padding=5)
        form.pack(fill="x")
        self.inputs = {}
        for column, field in enumerate(FIELDS):
            ttk.Label(form, text=field.title()).grid(row=0, column=column, sticky="w")
            widget = ttk.Combobox(form, values=CATEGORIES, state="readonly", width=8) \
                if field == "category" else ttk.Entry(form)
            widget.grid(row=1, column=column, padx=2, sticky="we")
            self.inputs[field] = widget
        self.inputs["category"].set(CATEGORIES[0])

        buttons = ttk.Frame(root, padding=5)
        buttons.pack(fill="x")
        for text, command in (("Add", self.add), ("Update", self.update), ("Delete", self.delete), ("Clear", self.clear)):
            ttk.Button(buttons, text=text, command=command).pack(side="left", padx=2)
        self.refresh()

    def form_data(self):
        return {field: widget.get() for field, widget in self.inputs.items()}

    def selected_id(self):
        selection = self.table.selection()
        if not selection:
            messagebox.showinfo("Collection", "Select an item first")
            return None
        return int(selection[0])

    def run(self, action):
        try:
            action()
        except (ValueError, KeyError) as error:
            messagebox.showerror("Collection", str(error))
        self.refresh()

    def add(self):
        self.run(lambda: self.manager.create(self.form_data()))

    def update(self):
        item_id = self.selected_id()
        if item_id is not None:
            self.run(lambda: self.manager.update(item_id, self.form_data()))

    def delete(self):
        item_id = self.selected_id()
        if item_id is not None and messagebox.askyesno("Collection", "Delete the selected item?"):
            self.run(lambda: self.manager.delete(item_id))
            self.clear()

    def clear(self):
        for field, widget in self.inputs.items():
            if field != "category":
                widget.delete(0, "end")
        self.table.selection_remove(self.table.selection())

    def on_select(self, event):
        selection = self.table.selection()
        if not selection:
            return
        item = self.manager.get(int(selection[0]))
        for field, widget in self.inputs.items():
            if field == "category":
                widget.set(item[field])
            else:
                widget.delete(0, "end")
                widget.insert(0, item[field])

    def refresh(self):
        category = None if self.filter.get() == ALL else self.filter.get()
        self.table.delete(*self.table.get_children())
        for item in self.manager.search(self.query.get(), category):
            self.table.insert("", "end", iid=str(item["id"]), values=[item[f] for f in FIELDS])
