from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import random


class Ui_Dialog(object):
    board = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    turn = 0
    turns = 0
    status = 0
    buttons = []

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 218, 75, 61))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 108, 75, 61))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(250, 338, 75, 61))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 218, 75, 61))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(400, 338, 75, 61))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")

        self.resetButton = QtWidgets.QPushButton(Dialog)
        self.resetButton.setGeometry(QtCore.QRect(400, 40, 75, 30))
        self.resetButton.setText("reset")
        self.resetButton.setObjectName("reset_button")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 108, 75, 61))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 108, 75, 61))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 218, 75, 61))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 38, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 340, 75, 61))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")

        self.buttons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9]

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(partial(self.playTurn, 0))
        self.pushButton_2.clicked.connect(partial(self.playTurn, 1))
        self.pushButton_3.clicked.connect(partial(self.playTurn, 2))
        self.pushButton_4.clicked.connect(partial(self.playTurn, 3))
        self.pushButton_5.clicked.connect(partial(self.playTurn, 4))
        self.pushButton_6.clicked.connect(partial(self.playTurn, 5))
        self.pushButton_7.clicked.connect(partial(self.playTurn, 6))
        self.pushButton_8.clicked.connect(partial(self.playTurn, 7))
        self.pushButton_9.clicked.connect(partial(self.playTurn, 8))
        self.resetButton.clicked.connect(self.reset)

    def playTurn(self, boardnum):

        if self.status != 1:

            if self.board[boardnum] == 1 or self.board[boardnum] == 0:
                # redo turn!
                pass
            else:
                self.board[boardnum] = 0
                self.buttons[boardnum].setStyleSheet("background-color: blue")
                self.turns += 1
                self.checkWin(0)
            self.comTurn()

    def comTurn(self):
        if self.status != 1:
            self.turns += 1
            if self.turns >= 9:
                self.lineEdit_2.setText("Cats Game!")
                self.status = 1
            else:

                randpick = random.randint(0, 8)
                while self.board[randpick] == 0 or self.board[randpick] == 1:
                    randpick = random.randint(0, 8)

                self.buttons[randpick].setStyleSheet("background-color: red")
                self.board[randpick] = 1
                self.checkWin(1)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.lineEdit_2.setText(_translate("Dialog", "status"))

    def checkWin(self, player):
        if (self.board[0] == self.board[1] == self.board[2]) or \
                (self.board[3] == self.board[4] == self.board[5]) or \
                (self.board[6] == self.board[7] == self.board[8]) or \
                (self.board[0] == self.board[3] == self.board[6]) or \
                (self.board[1] == self.board[4] == self.board[7]) or \
                (self.board[2] == self.board[5] == self.board[8]) or \
                (self.board[0] == self.board[4] == self.board[8]) or \
                (self.board[2] == self.board[4] == self.board[6]) or \
                (self.board[0] == self.board[1] == self.board[2]):

            if player == 0:
                self.lineEdit_2.setText("Player wins!")
            else:
                self.lineEdit_2.setText("COM wins!")
            self.status = 1
        if self.turns > 9:
            self.lineEdit_2.setText("Cats Game!")
            self.status = 1

    def reset(self):

        self.board = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        self.turn = 0
        self.turns = 0
        self.status = 0
        for i in range(0, 9):
            self.buttons[i].setStyleSheet("background-color: none")

        self.lineEdit_2.setText(" ")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
