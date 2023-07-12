from tkinter import *
from tkinter import ttk

class PLNEmotionExtractor():
    
    def __init__(self, title : str = "PLNEmotionExtractor") -> None:
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('320x240')

        # main frame
        f_main = ttk.Frame(self.root, relief=RAISED, border=1)
        f_main.pack(expand=True)
        
        c_teste = ttk.Frame(f_main)

        lb0 = ttk.Label(c_teste, text="Url", padding=10)
        lb0.pack(side=LEFT)

        e0 = ttk.Entry(c_teste)
        e0.pack(side=LEFT, padx=10)

        c_teste.pack()

        bt_extract = ttk.Button(f_main, text="Extract")
        bt_extract.pack()




    def run(self) -> None:
        self.root.mainloop()