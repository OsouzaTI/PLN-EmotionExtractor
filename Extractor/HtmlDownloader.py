import requests
from bs4 import BeautifulSoup

class HtmlDownloader():

    def __init__(self) -> None:
        self.url    = None
        self.html   = None
        self.bs4    = None

    def set_url(self, url : str) -> None:
        self.url = url

    def get_url(self) -> str:
        self.url
    
    def get_bs4(self) -> BeautifulSoup:
        return self.bs4

    def load(self) -> None:
        try:
            self.html   = requests.get(self.url)            
            self.bs4    =  BeautifulSoup(self.html.text, 'html.parser')
        except Exception as e:
            print(f'Erro encontrado {e}')