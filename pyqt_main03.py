# pyqt 연습 (240911)
'''
https://www.youtube.com/watch?v=O58FGYYBV7U&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=2
pydesigner 로 만든 것을 파이썬 파일로 바꾸기
$ pyuic5 -x window1.ui -o window1.py

'''

import PyQt5.QtWidgets as qtw   # 이렇게 import 해서 사용 가능
import PyQt5.QtGui as qtg

# Create A label
my_label = qtw.Qlabel("Hello World!")

# button 에 함수 입력 하기. 이렇게도 가능함
my_button = qtw.QPushButton("Press Me!", clicked=lambda: press_it())

def press_it():
    my_label.setText(f'Hello {my_entry.text()}') # or currentText(), currentIndex(), currentDate()

# combobox
my_combo = qtw.QComboBox(self, editable=True, insertPolicy=qtw.QComboBox.InertAtTop)

my_combo.addItem("Pepperoni", "Something")
my_combo.addItem("Cheese", 2)
my_combo.addItem("Mushroom", qtw.QWidget)
my_combo.addItems(["One","Two","Three"])    # list 로 넣을 수 있음
my_combo.insertItem(2, "Third Thing")   # 인덱스를 정해서 넣을 수 있음

# spin box, 
my_spin = qtw.QSpinBox(self,    # QDoubleSpinBox 도 있음
                       value=10,
                       maximum=100,
                       minimum=0,
                       singleStep=20,
                       prefix="#",
                       suffix=" Order")
                    

# font size
my_label.setFont(qtg.QFont('Helvetica', 24))

# text box
my_text = qtw.QTextEdit(self,
                        plainText="This is real text",
                        html="<h1>big header text!</h1>",
                        acceptRichText=True,    # 글자에 색 입힐 수 있음
                        lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                        lineWrapColumnOrWidth=50,
                        placeholderText="Hello World!",
                        readOnly=False,)

my_label.setText(f'You typed {my_text.toPalinText()}')
my_text.setPlainText("you pressed ")

# lec #5
form_layout = qtw.QFormLayout()
self.setLayout(form_layout)
label_1 = qtw.QLabel("ths is a cool label")
f_name = qtw.QLineEdit(self)
l_name = tqw.QLineEdit(self)
form_layout.addRow(label_1)
form_layout.addRow("First Name", f_name)
form_layout.addRow("Last Name", l_name)
form_layout.addRow(qtw.QPushButton("Press it!!", clicked=lambda:press_it()))

# lec #6
# pip install PyQt5Designer
# $ pyuic5 -x hello_world.ui -o hello_world.poy

# lec #8

# ("Press it!!", clicked=lambda:press_it("C")) # 이렇게 넘김

def press_it(self, pressed):    # 입력을 받았을 때 어떤 입력을 추가로 받았는지를 pressed 로 전달함
    if pressed == "C":
        self.outputLabel.setText("0")
    else:
        if self.outputLabel.text() == "0":
            self.outputLabel.setText()
        self.outputLabel.setText(f'{self.outputLabel.text(){pressed}}')

answer = eval(screen)   # 수식 계산

# lec #10
# Fugue Icons 추가 가능, p.yusukekamiyamane.com

# lec #12
# tab close -> property, tabsClosable 'check' 
tabs = self.tabWidget
tabs.tabCloseRequested.connect(lambda index: tabs.removeTab(index))

# lec #13
# add item to list. lineedit, pushbutton, listwidget 이 있음
def add_it(self):
    # grap the item from the list box
    item = self.additem_lineEdit.text()
    # add item to list
    self.mylist_listWidget.addItem(item) 
    # clear the item box
    self.additem_lineEdit.setText("")

def clear_it(self):
    self.mylist_listWidget.clear()

def delete_it(self):
    # grap the selected row or current row
    clicked = self.mylist_listWidget.currentRow()
    # self.additem_lineEdit.setText(str(clicked)) # clicked 는 int 로 들어감
    # delete selected row
    self.mylist_listWidget.takeItem(clicked)

# lec #14
def save_it(self):
    # create blank dictionary to hold todo items
    items = []
    # loop through the listWidget and pull out each item
    for index in range(self.mylist_listWidget.count()):
        items.append(self.mylist_listWidget.item(index))
    for item in items:
        print(item.text())

# lec #15
import sqlite3

conn = sqlite3.connect('mylist.db')
c = conn.cursor()
c.execute("""CREATE TABLE if not exists todo_list(
          list_item text) 
          """)
conn.commit()
conn.close()

c.execute("SELECT * FROM todo_list")
records = c.fetchall()

for record in records:
    self.mylist_listWidgetsaddItem(str(record))

for item in items:
    c.execute("INSERT INTO todo_list VALUES (:item)",
              {
                  'item': item.text(),
              })

# pop up box
msg = qtw.QMessageBox()
msg.setWindowTitle("Saved to database!!")
msg.setText("your todo list has been saved!")
msg.setIcon(qtw.QMessageBox.Information)
x = msg.exec_() # 계속 실행해놓는거는 이렇게

# lec #16

# lec #17

self.statusbar.setFont(qtw.QFont('Helvetica'))
self.statusbar.showMessage("Ready...")

def push_1(self):
    self.statusbar.showMessage("I pressed button 1")

# lec #18
def select(self):
    if self.radioButton.isChecked():
        self.label.setText("Pepperoni")
# set defalut radio button to checked
self.radioButton.setChecked(True)

# lec #19
# set button states
self.radioButton.toggled.connect(lambda:self.btnstate(self.radioButton))    # btnstate 함수에 어떤 버튼이 선택되었는지를 넘겨줌. 받을 때 인수 필요

def btnstate(self, b):
    if b.isChecked():
        self.label.setText(b.text())

# lec #20
# state, 0=not checked, 2=checked

# lec #21
self.red_checkBox.stateChanged.connect(lambda:self.check())
self.blue_checkBox.toggled.connect(lambda:self.check())

# lec #22
self.dial = qtw.QtWidgets.QDial(self.qtw.QWidget())
self.dial.valueChanged.connect()
self.dial.setRange(100,200)
# set notches
self.dial.setNotchesVisible(False)
self.dial.setStyleSheet('background-color: #377235')

# lec #23 combo box
def clicker(self):
    self.label.setText(f'you picked: {self.comboBox.currentText()}')
# add items to combo box. addItem 으로 아이템 입력
self.comboBox.addItem("Pepperoni")
self.comboBox.addItem("Mushroom")
# list 로 아이템 추가하기
my_topping = ["Ham", "Pineapple"]
self.comboBox.addItem(my_toppings)
# 콤보박스를 선택했을 때 버튼이 눌렀을 때 와 같은 동작 시키기
self.comboBox.activated.connect(self.clicker()) # activated 매서드를 사용해서 실행

# lec #24, open a second window

# lec #25, pass data between window

# lec #26, hide first window from second window
def open_window(self):
    # open second window
    self.window = QtWidgets.QMainWindow()
    self.ui = Ui_SecondWindow()
    self.ui.setUi(self.window)
    self.window.show()
    MainWindow.hide() # 이렇게 하면 숨겨짐
#$ 윈도우 간에 서로 import 해서 서로의 함수를 사용할 수 있도록 설정
main_w.hide()
main_w.show() 로 사용

# lec #27, how to load pyqt5 designer ui files
class UI(QMainwWindow):
    def __init__(self):
        super(UI, self).__init__()
        # load the ui file
        uic.loadUi("loadui.ui", self)
        # define our widgets
        self.label = self.findChild(QLabel, "label") # 이렇게 ui 파일에서 사용하는 위젯을 찾아서 가져옴
        # show the app
        self.show()

# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

#$ ui 파일을 지정해서 불러올 수 있으며, widget 을 재정의 해서 사용함. 

# lec #28/#53, dependent comboboxes
    # add items to the combobox
    self.combo1.addItem("Male", ["John","Wes"])
    self.combo1.addItem("Female", ["April","Steph"])
    # click the first dropdown
    self.combo1.activated.connect(self.clicker)

def clicker(self, index):
    self.combo2.clear()
    self.combo2.addItems(self.combo1.itemData(index))

# lec #29, file dialog boxes with QFileDialog
fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Python Files (*.py)")     # 3번째 항목인 "" 는 파일을 여는 기본 경로를 변경할 때 사용한다
if fname:
    self.label.setText(str(fname)) # fname[0] 에는 불러온 파일 이름이 들어가고, fname[1] 에는 설정된 파일 유형이 들어간다

# lec #30, build an image viewer
# open the Iamge
self.pixmap = QPixmap(fname[0]) 
self.label.setPixmap(self.pixmap) # 이미지를 나타낼 label 에서 alignment 는 중간으로 해주는게 좋음

# lec #31, build a tic tac toe game
# click the button
self.button1.clicked.connect(lambda: self.clicker(self.button1))
def clicker(self, b):
    if self.counter % 2 == 0:
        mark = "X"
    else:
        mark = "O"

    b.setText("X")
    b.setEnabled(False) # 버튼을 누르면 표시를 남기고 비활성화 시키기
def reset(self): # 일괄 적용시에는 리스트를 만들어서 진행
    button_list = [
        self.button1,
        self.button9,]
    for b in button_list:
        b.setText("")
        b.setEanbled(True)
    
# change the button colors to red
a.setStyelSheet('QPushButton {color: red;}')

# lec #33, change background color with menu
# add menu triggers
self.actionBlack.tiriggered.connect(lambda: self.change("black"))

def change(self.color):
    self.setStyleSheet(f"background-color: {color};")

# lec #34, how to use the calender widget
self.calender.selectionChanged.connect(self.grab_date)
def grab_date(self):
    dateSelected = self.calender.selectedDate()
    self.label.setText(str(dateSelected.toPyDate()))

# lec #35, create an LCD Clock
self.timer = QTimer()
self.timer.timeout.connect(self.lcd_number)
self.timer.start(1000)
self.lcd_number()
self.show()

def lcd_number(self):
    time = datetime.now()
    formatted_time = time.strftime("%I:%M:%S %p")
    self.lcd.setDigitCount(12)
    self.lcd.setSegmentTStype(QLCDNumber.Flat)
    self.lcd.display(formatted_time)

# lec #36, multiple windows inside your app, 240929
self.mdi = self.findCHild(QMdiArea, "mdiArea")
# click button
self.button.clicked.connect(self.add_window)

def add_window(self):
    UI.count = UI.count + 1
    # create sub windows
    sub = QMdiSubWindow()
    # do stuff in the sub windows
    sub.setWidget(QTextEdit())
    # set the titlebar or the sub window
    sub.setWindowTitle("Subby window " + str(UI.cont))
    # add the sub window into our MDI widget
    self.mdi.addSubWindow(sub)
    # show the new sub window
    sub.show()
    # position the su bwindows
    self.mdi.titleSubwindows()
    self.mdi.cascadeSubWindows()

# lec #37, hover and focus effects for forms and buttons
#$ editStyleSheet

# lec #38, language translation app
#$ pip install googletrans
#$ pip install textblob
# add language to the combo boxes
self.language = googletrans.LANGUAGES
#$ combo box 에 나타낼 값 설정
self.language_list = list(self.languages.values())
self.combo_1.addItesm(self.language_list)
self.combo_1.setCurrentText("english")

def translate(self):
    try:
        # get original language key
        for key, value in self.languages.items():
            if( value == self.combo_1.currentText()):
                from_language_key = key
        # get translated language key
        for key, value in self.languages.items():
            if (value == self.combo_2.currentText()):
                to_language_key = key
    except Exception as e:
        QMessageBox.about(self, "Translator", str(e))

    # turn original text into a textblob
    words = textblob.TextBlob(self.text_1.toPlainText())
    # translate words!
    words = words.tranlate(from_lang=from_language_key, to=to_language_key)
    # output to text_2
    self.text_2.setText(str(words))

# lec #38, how to add text to speech, 
#$ pip install pyttsx3
#$ pip install pywin32
# initialize the speech engine
engine = pyttsx3.init()
# pass words to speak
engine.say(words)

# lec 40, horizontal slider
self.slider = self.findChild(QSlider, "horizontalSlider")
self.label.setAlignment(QtCore.Qt.AlignCenter)
self.slider.setMinimum(0)
self.slider.setMaximum(50)
self.slider.setValue(0)
self.slider.setTickPosition(QSlider.TicksBelow)
self.slider.setIckInterval(5)
self.slider.setSingleStop(5)
self.slider.valueChanged.connect(self.slide_it)


def slide_it(self, value):
    self.label.setText(str(value))

# lec #41, vertical slider

# lec #42, add text to images with pillow,
# 이미지 넣기. label 을 추가 -> text 에 pixmap 으로 이미지 파일 추가

# lec #44, bind text box text to label
# hit enter button
self.edit.editingFinished.connect(self.hitEnter)
# on click
self.edit.textChanged.connect(self.changeText)
def hitEnter(self):
    self.label.setText(self.edit.text())
def changeText(self):
    self.label.setText()

