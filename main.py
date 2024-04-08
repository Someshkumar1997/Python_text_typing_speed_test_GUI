import tkinter as tk
import time
import threading
import random

class TypeSpeedGUI:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Typing Speed Application")
        self.root.geometry = ("800x600")

        self.texts = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text= random(self.texts), font= ("Your choice", 18))
        self.sample_label.grid(row= 0, column= 0, columnspan= 2, padx= 5, pady= 10)

        self.input_entry = tk.Entry(self.frame, width=40, font= ("Your choice", 24))
        self.input_entry.grid(row= 1, column= 0, columnspan= 2, padx= 5, pady= 10)
        self.input_entry.bind("<KeyPress>", self.start)

        self.speed_label = tk.Label(self.frame, text= "Speed: \n0.00 WPS\n0.00 WPM", font= ("Your choice", 18))
        self.speed_label.grid(row= 2, column= 0, columnspan= 2, padx= 5, pady= 10)

        self.reset_button = tk.Button(self.frame, text= "Reset", command= self.reset)
        self.reset_button.grid(row= 3, column= 0, columnspan= 2, padx= 5, pady= 10)

        self.frame.pack(expand= True)

        self.counter = 0
        self.started = False

        self.root.mainloop()

    def start(self, event):
        if not self.started:
            if not event.keycode in [16, 17, 18]:
                self.started = True
                t = threading.Thread(target= self.time_thread)
                t.start()

        if not self.sample_label.cget('text') == self.input_entry.get():
            self.input_entry.config(fg= "red")
        else:
            self.input_entry.config(fg= "black")
        
        if self.input_entry.get() == self.sample_label.cget('text')[:-1]:
            self.started = False
            self.input_entry.config(fg= "green")



    def time_thread(self):
        while self.started:
            time.sleep(0.1)
            self.counter += 0.1
            wps = len(self.input_entry.get() / self.counter)
            wpm = wps * 60
            self.speed_label.config(text= f"Speed: \n{wps:.2f} CPS\n{wpm:.2f} CPM")





    def reset(self):
        pass

TypeSpeedGUI()










