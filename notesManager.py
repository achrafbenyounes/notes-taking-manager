import os
from glob import glob

CUR_DIR = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(CUR_DIR, 'data')
path_note = None

def getNoteContent(note_name):
    note_path = os.path.join(DATA_FOLDER, note_name + '.txt')
    with open(note_path, 'r') as f:
        note_content = f.read()
    return note_content

def createNote(noteName, content = ''):
    path_note = getNotePath(DATA_FOLDER, noteName, '.txt')
    with open(path_note, 'w') as f:
        f.write(content)
    if os.path.isfile(path_note):
        print(f"The note {noteName} is well writen")

def deleteNote(noteName):
    path_note = getNotePath(DATA_FOLDER, noteName, '.txt')
    if os.path.isfile(path_note):
        os.remove(path_note)
        print(f"The note {noteName} is removed")
    else:
        print(f"The note {noteName} does not exist")

def retrieveAllNotes():
    notes = glob(DATA_FOLDER + '/*.txt')
    # We'll use comprehension list to retrive only the name of the note 
    return [os.path.splitext(os.path.split(n)[-1])[0] for n in notes]

def getNotePath(folderNote, noteName, noteExtension):
    return os.path.join(folderNote, noteName + noteExtension)

