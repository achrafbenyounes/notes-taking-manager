from PySide2 import QtWidgets, QtGui, QtCore
from ui.principalWindow import Ui_principalWindow

class NoteCreation(QtWidgets.QWidget, Ui_principalWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

app = QtWidgets.QApplication([])
note_creation = NoteCreation()
app.exec_()