from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 751)
        MainWindow.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 270))
        self.frame.setStyleSheet("background-color: rgb(255, 253, 208);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 30, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(34, 34, 46);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 181, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../photoshop/для ps/exchanging.png"))
        self.label_2.setObjectName("label_2")
        self.inpu_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.inpu_currency.setGeometry(QtCore.QRect(50, 300, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        self.inpu_currency.setFont(font)
        self.inpu_currency.setStyleSheet("background-color: rgb(120, 120, 120);\n"
"color: rgb(255, 253, 208);\n"
"border: 2px solid #fffdd0;\n"
"border-radius: 30;")
        self.inpu_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.inpu_currency.setObjectName("inpu_currency")
        self.input_ammount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ammount.setGeometry(QtCore.QRect(50, 390, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        self.input_ammount.setFont(font)
        self.input_ammount.setStyleSheet("background-color: rgb(120, 120, 120);\n"
"color: rgb(255, 253, 208);\n"
"border: 2px solid #fffdd0;\n"
"border-radius: 30;")
        self.input_ammount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_ammount.setObjectName("input_ammount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(50, 480, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: rgb(120, 120, 120);\n"
"color: rgb(255, 253, 208);\n"
"border: 2px solid #fffdd0;\n"
"border-radius: 30;")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_ammount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_ammount.setGeometry(QtCore.QRect(50, 570, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        self.output_ammount.setFont(font)
        self.output_ammount.setStyleSheet("background-color: rgb(120, 120, 120);\n"
"color: rgb(255, 253, 208);\n"
"border: 2px solid #fffdd0;\n"
"border-radius: 30;")
        self.output_ammount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_ammount.setObjectName("output_ammount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 660, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {color: 2222e;\n"
"background-color:  rgb(255, 253, 208);\n"
"border-radius: 30;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: 2222e;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "КОНВЕРТЕР ВАЛЮТ"))
        self.pushButton.setText(_translate("MainWindow", "КОНВЕРТИРУЙ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


"""
grey : rgb(57, 57, 57);
green : rgb(60, 223, 115);


"""