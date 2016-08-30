#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Simple Hello World
"""

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = tk.Button(self)
        self.button1["text"] = "Click here to do action 1"
        self.button1["command"] = self.action1
        self.button1.pack(side="top")

        self.button2 = tk.Button(self)
        self.button2["text"] = "Action 2 here"
        self.button2["command"] = self.action2
        self.button2.pack()

        self.output_label = tk.Label(self)
        self.output_label["text"] = "Program will communicate here !"
        self.output_label.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

    def action1(self):
        print("action 1")

    def action2(self):
        self.output_label["text"] = "Ahah, t'a cliqué sur le bouton 2, je le sais"


root = tk.Tk()
app = Application(master=root)
app.mainloop()



