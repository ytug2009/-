#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import*

app=QApplication([])
ap=QWidget()
RadioGroupBox2=QGroupBox('результат теста:')
RadioGroupBox=QGroupBox('варианты ответов')
RadioGroupBox2.hide()
ap.setWindowTitle('appp')
button=QPushButton('ответить')
qvestion=QLabel('что?')
qvestion1=QLabel('верно')
qvestion2=QLabel('не верно')
rbtn1=QRadioButton('да')
rbtn2=QRadioButton('нет')
rbtn3=QRadioButton('то')
rbtn4=QRadioButton('ничего')
layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

def showresult():
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    button.setText('следующий')

def showqestions():
    RadioGroupBox2.hide()
    RadioGroupBox.show()
    button.setText('ответить')   

def starttext():
    if 'ответить'==button.text():
        showresult()
    else:
        showqestions()

answers=[rbtn1,rbtn2,rbtn3,rbtn4]
def ask(qvestion0,rbtn1,rbtn2,rbtn3,rbtn4):
    shuffle(answers)
    answers[0].setText(rbtn1)
    answers[1].setText(rbtn2)
    answers[2].setText(rbtn3)
    answers[3].setText(rbtn4)
    qvestion.setText(qvestion0)
    qvestion2.setText(rbtn1)
    showqestions()

def showcorrect(result):
    qvestion1.setText(result)
    showresult()


def checkanswer():
    if answers[0].isChecked():
        showcorrect('prawilno')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            showcorrect('neprawilno')

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
layout1=QHBoxLayout()
layout2=QHBoxLayout()
layout3=QHBoxLayout()
layout4=QVBoxLayout()
layoutw=QVBoxLayout()
layoutw.addWidget(qvestion1)
layoutw.addWidget(qvestion2)

RadioGroupBox.setLayout(layout_ans1)
RadioGroupBox.show()
RadioGroupBox2.setLayout(layoutw)
RadioGroupBox2.hide()

layout1.addWidget(qvestion,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout2.addWidget(RadioGroupBox,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout2.addWidget(RadioGroupBox2,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout3.addWidget(button,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout4.addLayout(layout1)
layout4.addLayout(layout2)
layout4.addLayout(layout3)
ap.setLayout(layout4)
ask('что?',('да'),'нет','то','ничего')
button.clicked.connect(checkanswer)
ap.show()
app.exec()
