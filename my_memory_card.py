#создай приложение для запоминания информации
#подключение модулей
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QPushButton, QGroupBox, QButtonGroup
from random import shuffle, randint
#создание класса QuestionW
class Questionw():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#создание окна

app = QApplication([])

#параметры окна приложения
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(500,500)
#виджеты
answer = QLabel('Какой национальности не существует?')
question = QPushButton('Ответить')

radiogroupbutton = QGroupBox('Варианты ответов')
questiongroupone = QRadioButton('Энцы')
questiongrouptwo = QRadioButton('Смурфы')
questiongroupthree = QRadioButton('Чулымцы')
questiongroupfour = QRadioButton('Алеуты')

buttongroup = QButtonGroup()
buttongroup.addButton(questiongroupone)
buttongroup.addButton(questiongrouptwo)
buttongroup.addButton(questiongroupthree)
buttongroup.addButton(questiongroupfour)

#создание лэйаутов

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
main_line = QVBoxLayout()

 
layout2.addWidget(questiongroupone)
layout2.addWidget(questiongrouptwo)
layout3.addWidget(questiongroupthree)
layout3.addWidget(questiongroupfour)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

radiogroupbutton.setLayout(layout1)

layoutH1.addWidget(answer)
layoutH2.addWidget(radiogroupbutton)
layoutH3.addWidget(question)
main_line.addLayout(layoutH1)
main_line.addLayout(layoutH2)
main_line.addLayout(layoutH3)

#скрывание вариантов ответов/1.2 часть дня

otvet = QLabel('Правильно/Неправильно')
p_otvet = QLabel('Правильный ответ')

layout4 = QVBoxLayout()
layout4.addWidget(otvet)
layout4.addWidget(p_otvet)

tworadiongroup = QGroupBox('Результат:')
tworadiongroup.setLayout(layout4)
layoutH2.addWidget(tworadiongroup)
tworadiongroup.hide()

#функция show_result, show_question, start_test
def show_result():
    radiogroupbutton.hide()
    tworadiongroup.show()
    question.setText('Следующий вопрос')

def show_question():
    tworadiongroup.hide()
    radiogroupbutton.show()
    question.setText('Ответить')
    buttongroup.setExclusive(False)
    questiongroupone.setChecked(False)
    questiongrouptwo.setChecked(False)
    questiongroupthree.setChecked(False)
    questiongroupfour.setChecked(False)
    buttongroup.setExclusive(True)







#задаём вопрос и обрабатываем ответ/2.2 часть
answers = [questiongroupone, questiongrouptwo, questiongroupthree, questiongroupfour]
def ask(q: Questionw):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    answer.setText(q.question)
    p_otvet.setText(q.right_answer)
    show_question()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика')
        print('Всего вопросов:', main_win.total)
        print('Правильных ответов:', main_win.score )
        print('Рейтинг:', main_win.score/main_win.total*100, '%')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно!')
        print('Рейтинг:', main_win.score/main_win.total*100, '%')

def show_correct(res):
    otvet.setText(res)
    show_result()


def next_question():
    main_win.total += 1
    cur_quest = randint(0, len(spisok)-1)
    q = spisok[cur_quest]
    ask(q)


def click_on():

    if 'Ответить' == question.text():
        check_answer()
    else:
        next_question()


spisok = list()
#ask('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский')
q = Questionw('Выбери перевод слова "переменная"', 'variable', 'variant', 'variaton', 'changing')
q2 = Questionw('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты')
q3 = Questionw('В каком штате есть город Харрикейн?', 'Юта', 'Флорида', 'Огайо', 'Монтана')
q4 = Questionw('Как переводится слово "plain"?' , 'равнина', 'самолёт', 'горы', 'вертолёт')
q5 = Questionw('В каком году были первые олимпийские игры в России?', '1980', '2012', '1993', '2004')
q6 = Questionw('В каком году родился А. С. Пушкин?', '1799', '1743', '1825', '1789')
q7 = Questionw('Что в советские времена означало наличие на товаре знака "звезда в пятиугольнике"?', 'знак качества', 'медаль', 'знак брака', 'экспортный товар')
q8 = Questionw('Кто написал "Муму"?', 'И. С. Тургенев', 'Л. Н. Толстой', 'Ф. М. Достоевский', 'А. П. Чехов')
q9 = Questionw('Кто из лицейских товарищей А. С. Пушкина был его секундантом на дуэли с Дантесом?', 'Данзас', 'Яковлев', 'Пущин', 'Кюхельберкер')
q10 = Questionw('При каком правителе на Руси двуглавый орёл появился на государственной печати?', 'Иван VI Грозный', 'Иван I Калита', 'Иван III', 'Иван II Красный')
q11 = Questionw('В каком году в России был введен григорианский календарь?', '1918', '1572', '1924', '1582')
q12 = Questionw('При каком правителе к России была присоединена территория Финляндии?', 'Александр I', 'Екатерина II', 'Пётр I', 'Павел I')
spisok.append(q)
spisok.append(q2)
spisok.append(q3)
spisok.append(q4)
spisok.append(q5)
spisok.append(q6)
spisok.append(q7)
spisok.append(q8)
spisok.append(q9)
spisok.append(q10)
spisok.append(q11)
spisok.append(q12)



question.clicked.connect(click_on)
main_win.total = 0
main_win.score = 0
next_question()


#отображение окна приложения

main_win.setLayout(main_line)
main_win.show()
app.exec_()

