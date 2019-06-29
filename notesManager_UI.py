from PySide2 import QtWidgets, QtGui, QtCore
from ui.principalWindow import Ui_principalWindow
import notesManager as nm

class NoteCreation(QtWidgets.QWidget, Ui_principalWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retrieveAllNotes()
        self.setupConnections()
        self.show()

    def setupConnections(self):
        self.btn_createNote.clicked.connect(self.createNote)
        self.btn_delNote.clicked.connect(self.deleteNote)
        self.btn_updateNote.clicked.connect(self.updateNote)
        self.lw_listNotes.itemClicked.connect(self.showNote)


    def createNote(self):
        print("Note created ...")
    
    def deleteNote(self):
        print("Note deleted ...")
    
    def showNote(self):
        print("Note visualized ...")
    
    def updateNote(self):
        print("Note is updated ...")
    
    def retrieveAllNotes(self):
        notes = nm.retrieveAllNotes()
        self.lw_listNotes.addItems(notes)

app = QtWidgets.QApplication([])
note_creation = NoteCreation()
app.exec_()