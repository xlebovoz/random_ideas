from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from random import randint
from PyQt5.QtGui import QFont
from ideas_ru import i_ru
from ideas_en import i_en

W = 900
H = 700
main_font = 16
language = 'ru'

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('RANDOM ideas')

style_sheet = '''QWidget {
    background-color: #d3d9eb;
}

#spinButton {
    background-color: #2786c5;
    color: black;
    border: none;
    border-radius: 10%;
    font-size: 26px;
}
#spinButton:hover {
    background-color: #2c8fd1;
}

#lan {
    background-color: #2786c5;
    color: black;
    border: none;
    border-radius: 10%;
}
'''

app.setStyleSheet(style_sheet)

ideas_list = []
current_index = None
initial_text = 'Идеи'

def load_ideas():
    global ideas_list
    if language == 'ru':
        ideas_list = i_ru
    else:
        ideas_list = i_en

load_ideas()

main_win.setFixedSize(W, H)

text = QLabel(initial_text)
font1 = QFont()
font1.setPointSize(main_font)
text.setFont(font1)
btn_change = QPushButton('Обновить')
btn_change.setFixedSize(200, 100)
btn_change.setObjectName("spinButton")
btn_lan = QPushButton('RU')
btn_lan.setFixedSize(50, 50)
btn_lan.setObjectName('lan')

text.setAlignment(Qt.AlignCenter)
text.setWordWrap(True)
text.setFixedWidth(800)

def change():
    global current_index
    if ideas_list:
        current_index = randint(0, len(ideas_list) - 1)
        text.setText(ideas_list[current_index])
    else:
        text.setText("Нет идей в файле.")

def change_lan():
    global language, current_index
    current_text = text.text()
    if current_text != initial_text and ideas_list:
        try:
            current_index = ideas_list.index(current_text)
        except ValueError:
            current_index = None

    cur_text_button = btn_lan.text()
    if cur_text_button == 'RU':
        btn_lan.setText('EN')
        btn_change.setText('SPIN')
        language = 'en'
    elif cur_text_button == 'EN':
        btn_lan.setText('RU')
        btn_change.setText('Обновить')
        language = 'ru'

    load_ideas()

    if current_index is not None and 0 <= current_index < len(ideas_list):
        text.setText(ideas_list[current_index])
    else:
        if ideas_list:
            index = randint(0, len(ideas_list) - 1)
            text.setText(ideas_list[index])
            current_index = index
        else:
            text.setText("Нет идей в файле.")
            current_index = None

main_layout = QVBoxLayout()
lan_layout = QHBoxLayout()
idea_layout = QHBoxLayout()
btn_layout = QHBoxLayout()

main_layout.addLayout(lan_layout)
main_layout.addLayout(idea_layout)
main_layout.addLayout(btn_layout)

idea_layout.addWidget(text, alignment=Qt.AlignCenter)

lan_layout.addWidget(btn_lan)
lan_layout.addStretch()
btn_layout.addWidget(btn_change)

main_win.setLayout(main_layout)

btn_change.clicked.connect(change)
btn_lan.clicked.connect(change_lan)

main_win.show()

app.exec()