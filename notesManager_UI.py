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
        noteName, ok = QtWidgets.QInputDialog.getText(self, 'Create a note', 'Give your note')
        if not ok:
            return
        nm.createNote(noteName)
        self.retrieveAllNotes()
    
    def deleteNote(self):
        notes_selected = self.lw_listNotes.selectedItems()
        if not notes_selected:
            return
        note_name = notes_selected[-1].text()
        nm.deleteNote(note_name)
        self.retrieveAllNotes()
    def showNote(self):
        print("Note visualized ...")
    
    def updateNote(self):
        print("Note is updated ...")
    
    def retrieveAllNotes(self):
        self.lw_listNotes.clear()
        notes = nm.retrieveAllNotes()
        self.lw_listNotes.addItems(notes)

app = QtWidgets.QApplication([])
note_creation = NoteCreation()
app.exec_()