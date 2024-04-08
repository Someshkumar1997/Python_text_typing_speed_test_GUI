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

        self.sample_label = tk.Label(self.root, text="Sample Text")





