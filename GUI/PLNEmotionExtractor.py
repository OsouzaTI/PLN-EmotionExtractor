from tkinter import *
from tkinter import ttk

from Extractor import HtmlDownloader

class PLNEmotionExtractor():
    
    def __init__(self, title : str = "PLNEmotionExtractor") -> None:

        # HtmlDownloader
        self.html_downloader = HtmlDownloader()


        self.root = Tk()
        self.root.title(title)
        self.root.geometry('320x240')

        # main frame
        f_main = ttk.Frame(self.root, relief=RAISED, border=1, padding=10)
        f_main.pack(side=LEFT, expand=True, fill=BOTH)
        
        c_teste = ttk.Frame(f_main, padding=10)

        lb0 = ttk.Label(c_teste, text="Url")
        lb0.pack(side=LEFT, padx=10)

        self.e0 = ttk.Entry(c_teste)
        self.e0.pack(side=LEFT, padx=10)

        c_teste.pack()

        bt_extract = ttk.Button(f_main, text="Extract", command=self.test)
        bt_extract.pack()


        # outro lado do root
        f_palavras = ttk.Frame(self.root, relief=RAISED, border=1, padding=10)
        f_palavras.pack(side=LEFT, expand=True, fill=BOTH)

        self.l_lista_palavras = Listbox(f_palavras)
        self.l_lista_palavras.pack(fill=BOTH, expand=True)

    def add_lista_palavras(self, index : int, palavra : str):
        self.l_lista_palavras.insert(index, palavra)

    def test(self) -> None:
        
        # definindo a url
        self.html_downloader.set_url(self.e0.get())
        # carregando html
        self.html_downloader.load()
        # recuperando o objeto parser
        parser = self.html_downloader.get_bs4()        
        links = map(lambda a: self.add_lista_palavras(a[0], a[1].get('href')),  enumerate(parser.find_all('a')))
        print(list(links))

    

    def run(self) -> None:
        self.root.mainloop()