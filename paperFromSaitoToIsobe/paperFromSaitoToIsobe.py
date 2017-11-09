import sys
from numpy import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep

paperList = [4, 7, 9, 10, 14, 15, 22, 27, 29, 33, 34, 35, 42, 44, 45, 47, 48, 51, 56, 63, 65, 67, 68, 69, 72, 75, 79, 80, 81, 82]
result = random.choice(paperList, 2, replace = False)

class Button(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        ## Labelオブジェクト
        explanationLabel = QLabel('saitoからisobeに移す論文を２編選ぶよ!!!')
        paper1Label = QLabel('論文１')
        paper2Label = QLabel('論文２')
        
        ## LineEditオブジェクト
        self.paper1Qle = QLineEdit(self)
        self.paper2Qle = QLineEdit(self)
        self.paper1Qle.setText("抽選No.")
        self.paper2Qle.setText("抽選No.")

        ## プログレスバー
        self.pbar = QProgressBar(self)
        self.timer = QBasicTimer()
        self.step = 0
        
        ## ボタン
        lotButton = QPushButton('抽選開始!!')
        lotButton.resize(lotButton.sizeHint())
        lotButton.clicked.connect(self.lotButtonClicked)

        ## レイアウト
        grid = QVBoxLayout()
        paperLayout = QHBoxLayout()
        paper1Layout = QVBoxLayout()
        paper2Layout = QVBoxLayout()
        paper1Layout.addWidget(paper1Label)
        paper1Layout.addWidget(self.paper1Qle)
        paper2Layout.addWidget(paper2Label)
        paper2Layout.addWidget(self.paper2Qle)
        paperLayout.addLayout(paper1Layout)
        paperLayout.addLayout(paper2Layout)
        grid.addWidget(explanationLabel)
        grid.addWidget(self.pbar)
        grid.addLayout(paperLayout)
        grid.addWidget(lotButton)

        self.setLayout(grid)
        self.setWindowTitle('Paper Lot')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.paper1Qle.setText("抽選No." + str(result[0]))
            self.paper2Qle.setText("抽選No." + str(result[1]))
            return
        
        self.step += 1
        self.pbar.setValue(self.step)

    def lotButtonClicked(self):
        sender = self.sender()
        self.timer.start(100, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    btn = Button()
    sys.exit(app.exec_())