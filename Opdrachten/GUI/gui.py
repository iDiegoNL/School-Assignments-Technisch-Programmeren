import tkinter as tk
from tkinter import ttk


class ViewHallo(tk.Frame):
    def __init__(self, parent, **kw):
        super.__init__(parent)
        super().__init__(**kw)


class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)


if __name__ == 'main':
    app = MyApplication()
    app.mainloop()
