from GUI import PLNEmotionExtractor
from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
gui = PLNEmotionExtractor()
gui.show()
app.exec_()