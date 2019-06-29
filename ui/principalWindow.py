# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:/Users/BENYOUNES_Achraf/Desktop/Python/Tutorial_PySide2/python_notes_manager_example/notes-taking-manager/ui\principalWindow.ui',
# licensing of 'c:/Users/BENYOUNES_Achraf/Desktop/Python/Tutorial_PySide2/python_notes_manager_example/notes-taking-manager/ui\principalWindow.ui' applies.
#
# Created: Sat Jun 29 16:55:36 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_principalWindow(object):
    def setupUi(self, principalWindow):
        principalWindow.setObjectName("principalWindow")
        principalWindow.resize(508, 435)
        self.gridLayout = QtWidgets.QGridLayout(principalWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_createNote = QtWidgets.QPushButton(principalWindow)
        self.btn_createNote.setObjectName("btn_createNote")
        self.gridLayout.addWidget(self.btn_createNote, 0, 0, 1, 1)
        self.btn_delNote = QtWidgets.QPushButton(principalWindow)
        self.btn_delNote.setObjectName("btn_delNote")
        self.gridLayout.addWidget(self.btn_delNote, 0, 1, 1, 1)
        self.lw_listNotes = QtWidgets.QListWidget(principalWindow)
        self.lw_listNotes.setObjectName("lw_listNotes")
        self.gridLayout.addWidget(self.lw_listNotes, 1, 0, 2, 2)
        self.te_NoteContent = QtWidgets.QTextEdit(principalWindow)
        self.te_NoteContent.setObjectName("te_NoteContent")
        self.gridLayout.addWidget(self.te_NoteContent, 1, 2, 1, 1)
        self.btn_updateNote = QtWidgets.QPushButton(principalWindow)
        self.btn_updateNote.setObjectName("btn_updateNote")
        self.gridLayout.addWidget(self.btn_updateNote, 2, 2, 1, 1)

        self.retranslateUi(principalWindow)
        QtCore.QMetaObject.connectSlotsByName(principalWindow)

    def retranslateUi(self, principalWindow):
        principalWindow.setWindowTitle(QtWidgets.QApplication.translate("principalWindow", "Notes Creator", None, -1))
        self.btn_createNote.setText(QtWidgets.QApplication.translate("principalWindow", "Create note", None, -1))
        self.btn_delNote.setText(QtWidgets.QApplication.translate("principalWindow", "Delete note", None, -1))
        self.btn_updateNote.setText(QtWidgets.QApplication.translate("principalWindow", "Update note", None, -1))

