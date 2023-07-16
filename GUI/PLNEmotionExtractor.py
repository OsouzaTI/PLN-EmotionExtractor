from PyQt5 import QtWidgets, QtGui, QtCore, uic
from tkinter import filedialog

from Extractor import HtmlDownloader
from .Dialog import AddUrlDialog

from langdetect import detect

import re
import PyPDF2

class PLNEmotionExtractor(QtWidgets.QMainWindow):
    
    def __init__(self, title : str = "PLNEmotionExtractor") -> None:
        super().__init__()
    
        # parametros usados
        self.url_selected = -1
        self.urls   = []
        self.words  = []

        # HtmlDownloader
        self.html_downloader = HtmlDownloader()

        # carregando janela
        uic.loadUi('GUI\QtDesigner\main.ui', self)
        self.setWindowTitle(title)

        # Inicializando Botoes
        self.ui_init_extract()
        self.ui_init_add_url()
        self.ui_init_remove_url()
        
        # Inicializando componentes
        self.ui_init_list_url()

        # Atualizando componentes
        self.ui_update_list_words()
        

    def ui_init_extract(self):
        bt_extract : QtWidgets.QPushButton = self.findChild(QtWidgets.QPushButton, 'bt_extract')
        bt_extract.clicked.connect(self.extract_from_url)

    def ui_init_add_url(self):
        bt_add_url : QtWidgets.QPushButton = self.findChild(QtWidgets.QPushButton, 'bt_add_url')
        bt_add_url.clicked.connect(self.handler_add_url_dialog)

    def ui_init_remove_url(self):
        bt_remove_url : QtWidgets.QPushButton = self.findChild(QtWidgets.QPushButton, 'bt_remove_url')
        bt_remove_url.clicked.connect(self.handler_remove_url)

    def ui_update_list_words(self):
        self.words.sort()
        lt_words : QtWidgets.QListView = self.findChild(QtWidgets.QListView, 'lt_words')

        # Create a QStandardItemModel
        model = QtGui.QStandardItemModel()
        for word in self.words:
            model.appendRow(QtGui.QStandardItem(word))

        lt_words.setModel(model)

    def ui_init_list_url(self):
        lt_urls : QtWidgets.QListView = self.findChild(QtWidgets.QListView, 'lt_urls')
        lt_urls.clicked.connect(self.handle_url_selection)

    def ui_update_list_url(self):
        lt_urls : QtWidgets.QListView = self.findChild(QtWidgets.QListView, 'lt_urls')

        # Create a QStandardItemModel
        model = QtGui.QStandardItemModel()
        for url in self.urls:
            model.appendRow(QtGui.QStandardItem(url))

        lt_urls.setModel(model)

    def ui_handler_text_url_changed(self, text):
        self.url = text

    #----------------------------------------------------------------#
    def extract_from_url(self) -> None:
        self.words.clear()
        for url in self.urls:

            # definindo a url
            self.html_downloader.set_url(url)
            # carregando html
            self.html_downloader.load()
            # recuperando o objeto parser
            parser = self.html_downloader.get_bs4()    

            for a in enumerate(parser.select('p')):
                palavras = re.findall(r'\b(?![\d_])\w{6,10}\b', a[1].text)
                for palavra in palavras:
                    # Só adicionamos se a palavra for em portugues (PT-BR)
                    if detect(palavra) == 'pt':
                        self.words.append(palavra)

        self.ui_update_list_words()

    def handler_add_url_dialog(self):
        dialog = AddUrlDialog(self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            item = dialog.get_item()
            self.urls.append(item)
            self.ui_update_list_url()

    def handle_url_selection(self, index : QtCore.QModelIndex):
        lt_urls : QtWidgets.QListView = self.findChild(QtWidgets.QListView, 'lt_urls')
        # model = lt_urls.model()
        # model.data(index, QtCore.Qt.DisplayRole)
        self.url_selected = index.row()
        print("Item selecionado:", self.url_selected)

    def handler_remove_url(self):
        if self.url_selected >= 0:
            del self.urls[self.url_selected]
            self.ui_update_list_url()
            # resetando o indice selecionado
            self.url_selected = -1
        else:
            self.show_message_error(message='Nenhuma url selecionada!')

    #-------------------------------------------------------------------------#

    def show_message_error(self, message = 'Error!'):
        # Exibir uma caixa de diálogo de mensagem de erro
        QtWidgets.QMessageBox.critical(None, "Erro", message)

    def show_message_success(self, message = 'Success!'):
        # Exibir uma caixa de diálogo de mensagem de erro
        QtWidgets.QMessageBox.information(None, "Success", message)