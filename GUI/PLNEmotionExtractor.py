from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from Extractor import HtmlDownloader
from langdetect import detect

import re
import PyPDF2

class PLNEmotionExtractor():
    
    def __init__(self, title : str = "PLNEmotionExtractor") -> None:

        # HtmlDownloader
        self.html_downloader = HtmlDownloader()


        self.root = Tk()
        self.root.title(title)
        self.root.geometry('640x480')
        self.root.resizable(False, False)

        # main frame
        f_main = ttk.Frame(self.root, padding=10)
        f_main.pack(fill=BOTH)
        
        # Container do campo botao
        c_teste = ttk.Frame(f_main)
        c_teste.pack(fill=X, expand=True,)

        lb0 = ttk.Label(c_teste, text="URI", font=("TkDefaultFont", 10, "bold"))
        lb0.pack(side=LEFT, padx=10)

        self.e0 = ttk.Entry(c_teste)
        self.e0.pack(side=LEFT, fill=X, expand=True,  padx=10)

        bt_extract = ttk.Button(c_teste, text="File (PDF)", command=self.selecionar_arquivo)
        bt_extract.pack()
        
        bt_extract = ttk.Button(c_teste, text="Extract", command=self.test)
        bt_extract.pack()


        # outro lado do root
        f_palavras = ttk.Frame(self.root, padding=10)
        f_palavras.pack(expand=True, fill=BOTH)

        # Lista
        self.l_lista_palavras = Listbox(f_palavras)
        self.l_lista_palavras.pack(expand=True, fill=BOTH)

    def selecionar_arquivo(self):
        # Abrir diálogo para selecionar arquivo
        arquivo = filedialog.askopenfilename()
        # limpa o campo
        self.e0.delete(0, 'end')
        self.e0.insert(0, arquivo)

    def extrair_texto_pdf(self, path : str) -> str:
        # Abrir o arquivo PDF em modo de leitura binária
        with open(path, 'rb') as arquivo_pdf:
            # Criar um objeto PDFReader
            pdf_reader = PyPDF2.PdfReader(arquivo_pdf)

            # Extrair o texto de cada página
            texto_completo = ''
            for pagina in pdf_reader.pages:
                texto_completo += pagina.extract_text()
            
            return texto_completo

    def add_lista_palavras(self, index : int, palavra : str):
        self.l_lista_palavras.insert(index, palavra)

    def test(self) -> None:

        if '.pdf' in  self.e0.get():
            pdf_texto = self.extrair_texto_pdf(self.e0.get())
            palavras = re.findall(r'\b(?![\d_])\w{6,10}\b', pdf_texto)
            for (ind, palavra) in enumerate(palavras):
                # Só adicionamos se a palavra for em portugues (PT-BR)
                if detect(palavra) == 'pt':
                    self.add_lista_palavras(ind, palavra)
        else:

            # limpando a lista
            self.l_lista_palavras.delete(0, 'end')
            # definindo a url
            self.html_downloader.set_url(self.e0.get())
            # carregando html
            self.html_downloader.load()
            # recuperando o objeto parser
            parser = self.html_downloader.get_bs4()    

            for a in enumerate(parser.select('p')):
                palavras = re.findall(r'\b(?![\d_])\w{6,10}\b', a[1].text)
                for palavra in palavras:
                    # Só adicionamos se a palavra for em portugues (PT-BR)
                    if detect(palavra) == 'pt':
                        self.add_lista_palavras(a[0], palavra)

    def run(self) -> None:
        self.root.mainloop()