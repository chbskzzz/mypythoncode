# scraping
from bs4 import BeautifulSoup as bs, element

self.btn1.clicked.connect(self.catSel)

def catSel(self):
    sefl.curCat = self.sender().text() # 어떤 버튼을 눌렀는지는 sender() 를 보면 알 수 있다. sender() 의 text 를 확인
    self.ulrSet()

self.lst.claer() # 리스트 초기화는 .clear() 로 한다
li[1].string # string 으로 변환

#
# pip install pyside2
# pip install pyinstaller

# 기본 포맷
import sys
from PySide2.QtWidgets import QApplication, QWidget

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()

app = QApplication([])
form = Form()
form.show()
sys.exit(app.exec_())

# align
self.ln = QLineEdit()
self.ln.setAlignment(Qt.AlignRight)
self.ln.setStyleSheet("font-size: 24px;" "font-weight: bold;")

## 버튼은 크기 조절이 안되게 되어 있기 때문에 정책을 수정해야 한다
i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

## 어떤 버튼이 눌러졌는지 확인하기 위해서는 self.sender() 를 확인해야 함

# 시그널은 신호. 객체의 상태가 변하게 되면 시그널이 발생 함. 시그널과 슬롯을 연결하면 슬롯에 있는 함수가 실행 됨

# 미리 초기 함수에 넣어주면 됨
super(btn, self).__init__()
self.setText(caption)
self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
self.setFixedSize(100,100)
self.setStyleSheet(".." "..")

# 슬롯을 통해서는 인자값을 넘길 수 없음. 인자를 넘기고 싶으면 '람다 함수' 를 사용해야 함
self.btnLambda.pressed.connect(lambda: self.test_lambda(self.btnReset.text()))
def test_lambda(self, i):
    self.clkCnt()
    print("입력: {}".format(i))