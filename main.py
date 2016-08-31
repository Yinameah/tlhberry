#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
Simple Hello World
"""

import tkinter as tk
import os
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.ping_button = tk.Button(self)
        self.ping_button["text"] = "Ping pour réveiller le tlhberry si la connection est compliquée"
        self.ping_button["command"] = self.ping_action
        self.ping_button.pack(side="top")

        self.connect_button = tk.Button(self)
        self.connect_button["text"] = "Action 2 here"
        self.connect_button["command"] = self.connect_action
        self.connect_button.pack()

        self.output_var = tk.StringVar()
        tk.Label(root, textvariable=self.output_var).pack(side="left")
        self.output_var.set("Program will communicate here")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

    def ping_action(self):
        # Ça marche pas le changement avant, je sais pas pourquoi
        self.output_var.set("Dring dring ...")
        # On pourrait boucler mais c'est trop long
        #for ping in range(100,150):
        address = "172.18.4.141"  # + str(ping)
        res = subprocess.call(['ping', '-c', '3', address])
        if res == 0:
            self.output_var.set("ping to " + address + " OK")
        elif res == 2:
            self.output_var.set("pas de réponse de " + address)
        else:
            self.output_var.set("ÉCHEC du ping")

    def connect_action(self):
        self.output_label["text"] = "Ahah, t'a cliqué sur le bouton 2, je le sais"


root = tk.Tk()
app = Application(master=root)
app.mainloop()



