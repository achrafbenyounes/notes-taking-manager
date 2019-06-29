from PySide2 import QtWidgets, QtGui, QtCore
from ui.principalWindow import Ui_principalWindow
import os
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

    # Make a function to retrieve the selected note and to be used by other methods
    def getSelectedNote(self):
        notes_selected = self.lw_listNotes.selectedItems()
        if not notes_selected:
            return
        note_name = notes_selected[-1].text()
        path_note = os.path.join(nm.DATA_FOLDER, note_name + '.txt')
        return note_name, path_note
    
    def deleteNote(self):
        note_name, path_name = self.getSelectedNote()
        nm.deleteNote(note_name)
        self.retrieveAllNotes()
        self.te_NoteContent.setText('')

    def showNote(self):
        note_name, path_note = self.getSelectedNote()
        note_content = nm.getNoteContent(note_name)
        self.te_NoteContent.setText(note_content)
    
    def updateNote(self):
        note_name, path_note = self.getSelectedNote()
        note_content = self.te_NoteContent.toPlainText()
        nm.createNote(note_name, note_content)
    
    def retrieveAllNotes(self):
        self.lw_listNotes.clear()
        notes = nm.retrieveAllNotes()
        self.lw_listNotes.addItems(notes)
    



app = QtWidgets.QApplication([])
note_creation = NoteCreation()
app.exec_()