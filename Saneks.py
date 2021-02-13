from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout
from random import randint

def show_winner():
    question_text.setText('АФИГЕТЬ ПРОСТО АФИГЕТЬ!ЭТО ОН!!!ЛОВИ ВОРЮГУ!!!!!')
    button.setText('ХАХАХАХА Я ПШУТИЛ!ОН  ВЫИГРАЛ!ОН НЕ ВОРЮГА!')
    a = randint(1,1000)
    a = str(a)
    winner.setText(a)


app = QApplication([])
window = QWidget()

window.resize(600,400)

question_text = QLabel('ЗДАРОВА РЕБЯТКИ')
winner = QLabel('КАК ВЫ ДУМАЕТЕ КТО ПОБЕДИЛ?')
button = QPushButton('УЗНАЙТЕ ЭТО!')

general_line = QVBoxLayout()

general_line.addWidget(question_text,alignment = Qt.AlignCenter)
general_line.addWidget(winner,alignment = Qt.AlignCenter)
general_line.addWidget(button,alignment = Qt.AlignCenter)

window.setLayout(general_line)

button.clicked.connect(show_winner)

window.show()
app.exec_()