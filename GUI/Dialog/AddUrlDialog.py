from PyQt5 import QtWidgets, QtGui, uic

class AddUrlDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Adicionar Item")

        # Layout principal do diálogo
        layout = QtWidgets.QVBoxLayout(self)

        # Layout para o formulário
        form_layout = QtWidgets.QFormLayout()
        layout.addLayout(form_layout)

        # QLineEdit para digitar o item
        self.line_edit = QtWidgets.QLineEdit()
        form_layout.addRow("Item:", self.line_edit)

        # QDialogButtonBox com botões "Adicionar" e "Cancelar"
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def get_item(self):
        return self.line_edit.text()