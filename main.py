from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QFormLayout
import json

app = QApplication([])

notes = {
    'Ласкаво просимо!': {
        'текст' : 'вавфівавіафвіавіавіавіавіаваа',
        'тег' : ['Добро', 'Інструкція']
    }
}

with open('notes_data.json', 'w') as file:
    json.dump(notes, file)


notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel('Список заміток')

button_note_create = QPushButton('Створити замітку')
button_note_delete = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введіть тег...')
field_text = QTextEdit()

button_tag_add = QPushButton('Додати тег')
button_tag_del = QPushButton('Відкрипити тег')
button_tag_search = QPushButton('Шукати по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегів')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_delete)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItem(notes[key]['теги'])

list_notes.itemClicked.connect(show_note) 

with open('notes_data.json', 'r') as file:
    notes = json.load(file)
    list_notes.addItem(notes)   

notes_win.show()

app.exec_()