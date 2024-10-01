import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QAction, QMenu, qApp
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import *

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())

# 버튼에 설정 가능한 것
btn = QPushButton('button name', self)
btn.resize(btn.sizeHint())
btn.setToolTip("툴팁임 <b>진하게도 가능하지</b>")
btn.mvoe(20,30) # 이동도 가능함

self.setGeometry(100,100,200,300) # 크기 조절 가능
self.setWindowTitle("제목 넣기도 가능")
self.show()

##

QCoreApplication # 이벤트 처리 담당
btn.clicked.connect(QCoreApplication.instance().quit) # 버튼 클릭 시 프로그램 종료
self.resize(500,500) # resize 만 해도 가운데 뜸
 
def closeEvent(self, QCloseEvent): # overriding 함
    ans = QMessageBox.question(self, "종료 확인", "종료할꺼야?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) # 마지막은 기본 값 위치 설정, 값을 받을 수 있음
    if ans == QMessageBox.Yes:
        QCloseEvent.accept()
    else:
        QCloseEvent.ignore()

# statusbar 만들기
self.statusBar()
self.statusBar().showMessage("안녕하세요")

# menu 만들기
menu = self.menuBar()
menu_file = menu.addMenu('File')
menu_edit = menu.addMenu('Edit')
menu_view = menu.addMenu('View')



file_new = QMenu('New', self)
new_txt = QAction('텍스트 파일', self)
new_py = QAction('파이썬 파일', self)
view_stat = QAction('상태표시줄', self, checkable=True) # 체커블 추가
view_stat.setCheckable(True)

file_exit = QAction('Exit', self)
file_exit.setShortcut('Ctrl+Q')
file_exit.setStatusTip('누르면 프로그램 종료됨')

file_exit.triggered.connect(QCoreApplication.instance().quit)
view_stat.triggered.connect(self.tglStat)

file_new.addAction(new_txt)
file_new.addAction(new_py)

menu_file.addMenu(file_new)
menu_file.addAction(file_exit)
menu_view.addAction(view_stat)

# 04강. https://www.youtube.com/watch?v=OIe77wIGZXY&list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo&index=4

def tglStat(self, state):
    if state:
        self.statusBar().show()
    else:
        self.statusBar().hide()

# 우클릭 만들기. 재정의 함
def contextMenuEvent(self, QContextMenuEvent):
    cm = QMenu(self)

    quit = cm.addAction("Quit")

    action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
    if action == quit:
        qApp.quit()  # connect 에 넣으려면 () 괄호를 빼야 함

# Layout

hbox = QHBoxLayout()
hbox.addStretch(1) # 다른 위젯이 차지하고 있지 않은 영역은 쭉쭉 늘려줌
hbox.addWidget(okButton)
hbox.addWidget(cancelButton)

# 계산기 모양으로 버튼 배치
grid = QGridLayout()
grid.setSpacing(10) # 개체들 사이사이에 공간을 주겠다
self.setLayout(grid)

positions = [(i,j) for i in range(5) for j in range(4)]
grid.addWidget(button, *position) # 이럴 경우에 postion 이 tuple 이면 쪼개서 넘어감. (1,3) -> 1,3

QLabel, QLineEdit, QTextEdit
grid.addWidget(review, 3,0)
grid.addWidget(reviewEdit, 3,1,5,1)

# event, signal
lcd = QLCDNumber(self)
sld = QSlider(Qt.Horizontal, self)

sld.valueChanged.connect(lcd.display) # dispaly 메서드는 미리 정의됨

## 키 누를 때 반응
def keyPressEvent(self, e): # e 는 값을 눌렀을 때 전달되는 키. 이벤트를 다시 정의하는 것. 틀 잡아놓은 것을 활용
    if e.key() == Qt.Key_Escape: # 정의된 상수랑 비교. e.key() 로 숫자화 된거 받음
        self.close() # 이게 제일 간단한 것

## 키 누르는 위치를 따라감
grid.addWidget(self.label, 0, 0, QtAlignTop)
self.setMouseTracking(True) # 마우스 위치를 계속 확인하겠다. CPU 소모함

def mouseMoveEvent(self,e):
    x = e.x()
    y = e.y()
    text = "x:{0}, y:{1}".format(x,y)
    self.label.setText(text)

##
btn1.clicked.connect(self.buttonClicked)

def buttonClicked(self):
    sender = self.sender() # sender() 는 함수를 호출한 객체를 소환함
    self.statusBar().showMessage(sender.text() + ' was pressed')

## mouse event 확인. emit() -> connect() -> signal() -> action!
class Communicate(QObject):
    closeApp = pyqtSignal() # pyqtSignal 을 사용하기 위해 QObject 를 상속함

self.c = Communicate()
self.c.closeApp.connect(self.close)

def mousePressEvent(self, event):
    self.c.closeApp.emit()

# dialog, 대화상자
self.btn.clicked.connect(self.showDialog)
def shwoDialog(self):
    text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name')
    if ok:
        self.le.setText(str(text)) # string 으로 바꾸기 위해 str 사용함

## frame 에 color 넣기
col = QColor(0,0,0)
self.frm = QFrame(self)
self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
self.frm.setGeometry(100,200,150, 250)
def showDialog(self):
    col = QColorDialog.getColor()
    if col.isValid():
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

## font 수정하기
btn = QPushButton('Dialog', self)
bt.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed) # 뭔가를 고정한다는 의미
def showDialog(self):
    font, ok = QFontDialog.getFont()
    if ok:
        self.lbl.setFont(font)

# checkbox
cb = QCheckBox('show title', self)
cb.toggle()
cb.stateChanged.connect(self.changeTitle)
def changTitle(self, state): # state 관련 메서드라 state 를 받을 수 있도록 던져주나 봄
    if state == Qt.Checked:
        self.setWindowTitle('QCheckBox')
    else:
        self.setWindowTitle('.')

## btn 으로 color 적용 설정
redb.clicked.connect(self.setColor)
def setColor(self, pressed): # clicked 라서 click 여부를 던져주나봄. pressed 가 받음
    source = self.sender() # 부른 애를 할당함
    if pressed:
        val = 255
    else:
        val = 0
    if source.text() == "Red":
        self.col.setRed(val)
    elif source.text() == "Green":
        self.col.setGreen(val)
    else:
        self.col.setBlue(val)
    self.square.setStyleSheet("QFram { background-color : %s }" % self.col.name())

## progress bar 활용 
self.pbar = QProgressBar(self)
self.btn = QPushButton('Start', self)
self.btn.clicked.connect(self.doAction)
self.timer = QBasicTimer()
self.step = 0

def timerEvent(self, e):
    if self.step >= 100:
        self.timer.stop()
        self.btn.setText('Finished')
        return
    self.step = self.setp+1
    self.pbar.setValue(self.step)

def doAction(self):
    if self.timer.isActive():
        self.timer.stop()
        self.btn.setText('Start')
    else:
        self.timer.start(100,self) # 100/1000 초라서 0.1초를 나타냄
        self.btn.setText('Stop')

# image 넣기
pixmap = QPixmap('Gun.png')
lbl = QLabel(self)
lbl.setPixmap(pixmap)

## 글자 친거 넣거
self.lbl = QLabel(self)
qle = QLineEdit(self)
qle.textChanged[str].connect(self.onChanged)
def onChanged(self, text):
    self.lbl.setText(text)
    self.lbl.adjustSize()

## combobox
self.lbl = QLabel('Ubuntu', self)
combo = QComboBox(self)
combo.addItem("Ubuntu")
combo.addItem("Normal")
combo.activated[str].connect(self.onActivated)
def onActivated(self,text):
    self.lbl.setText(text)
    self.lbl.adjustSize()

## drag & drop - 어렵다 다시 이해해보자 https://www.youtube.com/watch?v=1fdGUSmcdv0&list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo&index=10
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100,65)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        e.accept() # accept 는 설정해줘야 함

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
    def mouseMoveEvent(self,e): # mouseMoveEvent
        if e.buttons() != Qt.RightButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec_(Qt.MoveAction)
    def mousePressEvent(self,e): # mousePressEvent
        super().mousePressEvent(e)
        if e.button() == Qt.LeftButton:
            print('press')

# painter #skip

# tablewidget
self.btn.clicked.connect(on_cl)

def on_cl(): # 요건 버튼 클릭 시 실행. 함수임!
    fp = open("out.txt","wb")
    for r in range(ex.size):
        for c in range(ex.size):
            pickle.dump(ex.table.item(r,c).text(), fp)
    fp.close()

def createTable(self): # 이건 init 할 때 미리 부르는 거임. 메서드임!
    self.table = QTableWidget()
    self.table.setRowCount(self.size)
    self.table.setColumnCount(self.size)
    self.setHorizontalHeaderLabels(("이름","국어","영어","수학"))
    try:
        fp = open("out.txt","rb")
        for r in range(self.size):
            for c in range(self.size):
                self.table.setItem(r,c,QTableWidgetItem(str(pickle.load(fp))))
        fp.close()
    except:
        for r in range(self.size):
            for c in range(self.size):
                self.tabel.setItem(r,c,QTableWidgetItem(""))

# gray scale, open file
## 값을 넣으면 버튼이 생성
self.btn.clicked.connect(self.createBtn)
def createBtn(self):
    self.cnt = int(self.txt.text())
    for i in range(self.cnt):
        self.btnList.append(QPushButton(str(i+1) + "번째 버튼", self))
        self.btnList[i].resize(QSize(80,25))
        self.btnList[i].move(10,self.btnTop + (i*25))
        self.btnList[i].show() # 이게 중요함. show 를 해야 버튼을 보여줌

# 이미지 반사
# 타임벨


# treeview
self.tree = QTreeView(self)
self.tree.setRootIsDecorated(False)     # 기본으로 설정해 주는 것
self.tree.setAlternatingRowColors(True) # 기본으로 설정해 주는 것
self.tree.resize(330,200) 

self.tcontent = QStandardItemModel(0, 3, self) # 행은 그때그떄 지정 가능하지만, 컬럼은 미리 지정해준다
self.tcontent.setHeaderData(0, Qt.Horizontal, "번호") # 헤더 정보를 입력한다
self.tcontent.setHeaderData(1, Qt.Horizontal, "이름")
self.tcontent.setHeaderData(2, Qt.Horizontal, "주소")

self.tcontent.insertRows(self.tcontent.rowCount(), 1))
self.tcontent.setData(self.tcontent.index(0,0), self.tcontent.rowCount())
self.tcontent.setData(self.tcontent.index(0,1), "가나다")
self.tcontent.setData(self.tcontent.index(0,2), "라마바")

self.tree.setModel(self.tcontent)
self.tree.setColumnWidth(0,40)
self.tree.setColumnWidth(1,80)
                         
## db data
def enterEvent(self, QEvent):
    self.cmd = "select * from test"
    self.cur.execute(self.cmd)
    self.conn.commit()
    res = self.cur.fetchall()

## msg box
if None :
    try:
        pass
    except:
        QMessageBox.information(self, "에러", "재입력", QMessageBox.Yes, QMessageBox.Yes)


self.cmd = "insert into test (`no`,`name`,`add`) values({},'{}','{}')".format()
self.tree.currentIndex()

self.btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expandin) # 크기를 자동으로 맞춤

# 슬롯은 시그널을 보낸 객체를 알 수 있다

# 도형 그리기
class Rectangle(QGraphicsRectItem):
    def __init__():
        super().__init__()
        self.setBrush(QColor())
        self.setPen(QColor())
        self.setFlag(QGraphicsItem.ItemIsMovable, True)


## 도형을 보여주기 위해서는 씬을 만든 다음에 씬에 넣어서 보여주면 된다
class View(QGraphicsView):
    def __init__(self):
        super(View, self).__init__()
        self.scene = QGraphicsScene()
        self.setSceneRect(0,0,400,400)

        self.rect = Rectangle(5,5,5,5)
        self.scene.addItem(self.rect)

        self.setScene(self.scene)
                      
## 슬라이더 설정
self.sld = QSlider(Qt.Horizontal, self)
self.sld.setRange(-180,180)
self.sld.valueChanged.connect(self.changeValue)

# grid 는 QWidget 에만 설정 가능 
w = QWidget()
w.setLayout(self.gird)
self.setCentralWidget(w)

##
text, res = QInputDialog.getText(self, "제목", "할 일", QLineEdit.Normal, fname) # QLineEdit 은 기본값이라서 넣어 둠

## 파일 다루기
os.unlink(fname) # 파일 삭제
shutil.rmtree(fname) # 폴더 삭제