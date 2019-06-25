# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import time


class Ui_Dialog(object):
    board = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    turn = 0
    status = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 38, 71, 20))
        self.lineEdit.setObjectName("lineEdit")
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(partial(self.playTurn, self.turn, self.pushButton, 0))
        self.pushButton_2.clicked.connect(partial(self.playTurn, self.turn, self.pushButton_2, 1))
        self.pushButton_3.clicked.connect(partial(self.playTurn, self.turn, self.pushButton_3, 2))
        self.pushButton_4.clicked.connect(partial(self.playTurn, self.turn, self.pushButton_4, 3))
        self.pushButton_5.clicked.connect(partial(self.playTurn, self.turn, self.pushButton_5, 4))
        self.pushButton_6.clicked.connect(partial(self.playTurn, self.turn, self.pushButton_6, 5))
        self.pushButton_7.clicked.connect(partial(self.playTurn, self.turn, self.pushButton_7, 6))
        self.pushButton_8.clicked.connect(partial(self.playTurn, self.turn, self.pushButton_8, 7))
        self.pushButton_9.clicked.connect(partial(self.playTurn, self.turn, self.pushButton_9, 8))
        self.resetButton.clicked.connect(self.reset)

    def playTurn(self, turn, button, boardnum):
        if self.status != 1:
            if self.turn == 1:
                # self.comTurn()
                print("com plays")
                button.setStyleSheet("background-color: red")
                self.turn = 0
                self.lineEdit.setText("turn: " + str(self.turn))
                self.board[boardnum] = 1
                self.checkWin()
            else:
                if self.board[boardnum] == 1 or self.board[boardnum] == 0:
                    print("already placed!")
                else:
                    self.board[boardnum] = turn
                    button.setStyleSheet("background-color: blue")
                    self.turn = 1
                    self.lineEdit.setText("turn: " + str(self.turn))
                    self.checkWin()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setText(_translate("Dialog", "Turn: 0"))
        self.lineEdit_2.setText(_translate("Dialog", "status"))

    def checkWin(self):
        if (self.board[0] == self.board[1] == self.board[2]) or \
                (self.board[3] == self.board[4] == self.board[5]) or \
                (self.board[6] == self.board[7] == self.board[8]) or \
                (self.board[0] == self.board[3] == self.board[6]) or \
                (self.board[1] == self.board[4] == self.board[7]) or \
                (self.board[2] == self.board[5] == self.board[8]) or \
                (self.board[0] == self.board[4] == self.board[8]) or \
                (self.board[2] == self.board[4] == self.board[6]) or \
                (self.board[0] == self.board[1] == self.board[2]):
            self.lineEdit_2.setText(str(self.turn) + " wins!")
            self.status = 1
        count = 0
        for i in self.board:
            if i == 1 or i == 0:
                count += 1
        if count == 9:
            self.status = 1
            self.lineEdit_2.setText("Cats game!")



    def reset(self):

        self.board = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        self.turn = 0
        self.status = 0
        self.pushButton.setStyleSheet("background-color: none")
        self.pushButton_2.setStyleSheet("background-color: none")
        self.pushButton_3.setStyleSheet("background-color: none")
        self.pushButton_4.setStyleSheet("background-color: none")
        self.pushButton_5.setStyleSheet("background-color: none")
        self.pushButton_6.setStyleSheet("background-color: none")
        self.pushButton_7.setStyleSheet("background-color: none")
        self.pushButton_8.setStyleSheet("background-color: none")
        self.pushButton_9.setStyleSheet("background-color: none")
        self.lineEdit_2.setText(" ")
        self.lineEdit.setText("turn: 0")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
