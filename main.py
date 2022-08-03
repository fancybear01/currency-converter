import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from converter import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_Ui()

    def init_Ui(self):
        self.setWindowTitle("Currency converter")
        self.setWindowIcon(QIcon('D:\photoshop\для ps\exchanging.png'))

        self.ui.inpu_currency.setPlaceholderText('Из валюты:')
        self.ui.input_ammount.setPlaceholderText('Сколько:')
        self.ui.output_currency.setPlaceholderText('В валюту:')
        self.ui.output_ammount.setPlaceholderText('Я получу:')
        self.ui.pushButton.clicked.connect(self.conv)
    def conv(self):
        c = CurrencyConverter()
        input_currency = self.ui.inpu_currency.text()
        output_currency = self.ui.output_currency.text()
        input_ammount = int(self.ui.input_ammount.text())

        output_ammount = round(c.convert(input_ammount, '%s' % (input_currency), '%s' % (output_currency)), 2)

        self.ui.output_ammount.setText(str(output_ammount))

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
