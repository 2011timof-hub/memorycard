#подключение библиотек
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox,
QRadioButton,QMessageBox,QHBoxLayout,QButtonGroup)

class Question():
    def __init__(self,question,option1True,option2,option3,option4):
        self.question=question
        self.option1True=option1True
        self.option2=option2
        self.option3=option3
        self.option4=option4


qall=[]
qall.append(Question('Государственный язык Бразилии','Португальский','Бразильский','Английский','Французкий'))
qall.append(Question('Какой национальности не существует?','Смурфы','Энцы','Чулымцы','Алеуты'))
qall.append(Question('1+1 = ?','2','1','3','4'))
qall.append(Question('2+1 = ?','3','2','1','4'))
qall.append(Question('5-1 = ?','4','2','3','1'))
qall.append(Question('2+2 = ?','4','2','3','1'))
qall.append(Question('2x2 = ?','4','2','3','1'))
qall.append(Question('1+3 = ?','4','2','3','1'))
qall.append(Question('6-3 = ?','3','2','4','1'))
qall.append(Question('Столица Индии','Дели','Бразилия','Мехико-сити','Токио'))

#создание приложения и главного окна
app=QApplication([])

main_win=QWidget()
main_win.total=0
main_win.score=0
main_win.setWindowTitle('Memory card')
main_win.resize(400,200)


#создание виджетов главного окна
text1=QLabel()
opt1=QRadioButton()
opt2=QRadioButton()
opt3=QRadioButton()
opt4=QRadioButton()

button_group=QButtonGroup()

button=QPushButton('Ответить')

box=QGroupBox('Варианты ответов')
box2=QGroupBox('Результат теста')
box2.hide()
text5=QLabel()
text6=QLabel()


button_group.addButton(opt1)
button_group.addButton(opt2)
button_group.addButton(opt3)
button_group.addButton(opt4)




#привязка элементов к вертикальной линии
v_line=QVBoxLayout()
v2_line=QHBoxLayout()
h_line=QHBoxLayout()
h2_line=QHBoxLayout()
h3_line=QVBoxLayout()
h4_line=QVBoxLayout()
h5_line=QHBoxLayout()

v3_line=QVBoxLayout()

h3_line.setSpacing(15)
h4_line.setSpacing(15)

#расположение виджетов по лэйаутам
h_line.addWidget(text1,alignment=Qt.AlignCenter)

h2_line.addStretch(100)
h2_line.addWidget(box,stretch=500)
h2_line.addWidget(box2,stretch=500)
h2_line.addStretch(100)

h3_line.addWidget(opt1,alignment=Qt.AlignVCenter)
h3_line.addWidget(opt3,alignment=Qt.AlignVCenter)

h4_line.addWidget(opt2,alignment=Qt.AlignVCenter)
h4_line.addWidget(opt4,alignment=Qt.AlignVCenter)

v3_line.addWidget(text5,alignment=Qt.AlignVCenter)
v3_line.addWidget(text6,alignment=Qt.AlignHCenter)

h5_line.addStretch(100)
h5_line.addWidget(button,stretch=200)
h5_line.addStretch(100)

v_line.setSpacing(15)

v_line.addLayout(h_line)
v_line.addLayout(h2_line,stretch=600)



v_line.addLayout(h5_line)

v2_line.addLayout(h3_line)
v2_line.addLayout(h4_line)

box2.setLayout(v3_line)
box.setLayout(v2_line)
main_win.setLayout(v_line)

buttons=[opt1,opt2,opt3,opt4]

def ask(q: Question):
    text6.setText(q.option1True)
    shuffle(buttons)
    text1.setText(q.question)
    buttons[0].setText(q.option1True)
    buttons[1].setText(q.option2)
    buttons[2].setText(q.option3)
    buttons[3].setText(q.option4)
    show_question()

def check_answer():
    if buttons[0].isChecked():
        show_correct('Правильно')
        main_win.score+=1
    else:
        show_correct('Неправильно')
    print('Всего вопросов:',main_win.total)
    print('Правельных вопросов:',main_win.score)
    print('Рейтинг:',int(main_win.score/main_win.total*100),'%')

def show_correct(correct):
    text5.setText(correct)
    show_result()

def show_result():
    box.hide()
    box2.show()
    button.setText('Следущий вопрос')

def show_question():
    button_group.setExclusive(False)
    opt1.setChecked(False)
    opt2.setChecked(False)
    opt3.setChecked(False)
    opt4.setChecked(False)
    button_group.setExclusive(True)
    box2.hide()
    box.show()
    button.setText('Ответить')

def start_test():
    if button.text()=='Ответить':
        check_answer()
    else:
        next_question()

def next_question():
    counter=randint(0, len(qall)-1)
    ask(qall[counter])
    main_win.total+=1
    print('Всего вопросов:',main_win.total)
    print('Правельных вопросов:',main_win.score)

next_question()


button.clicked.connect(start_test)

 
#отображение окна приложения 
main_win.show()
app.exec_()