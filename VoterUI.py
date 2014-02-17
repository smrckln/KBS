import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Voter(QtWidgets.QWidget):

    def __init__(self):
        super(Voter, self).__init__()

        self.initUI()

    def initUI(self):
        grid = QtWidgets.QGridLayout()

        
        
        self.setFixedSize(550, 550)
        self.setWindowTitle('KBS Vote')
        self.center()

        vBtn = QtWidgets.QPushButton('Vote', self)
        cBtn = QtWidgets.QPushButton('Clear', self)

        vBtn.move(self.width()-150, self.height()-50)
        cBtn.move(self.width()-75, self.height()-50)

        #vBtn.clicked.connect(voteClick)
        #cBtn.clicked.connect(clearClick)

        self.show()

    #def clearClick():

    #def voteClick():
        

 

    def center(self):
        
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def main():

    app = QtWidgets.QApplication(sys.argv)

    voter = Voter()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
