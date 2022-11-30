from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushTotal.clicked.connect(lambda: self.total())
        self.pushClear.clicked.connect(lambda: self.clear())

    def total(self):
        try:
            bill = float(0)
            if self.checkBurger.isChecked():
                bill += 6.0
            if self.checkChsBurger.isChecked():
                bill += 6.5
            if self.checkChkSand.isChecked():
                bill += 5.5
            if self.checkSChkSand.isChecked():
                bill += 5.5
            if self.checkCSalad.isChecked():
                bill += 5.0
            if self.checkGSalad.isChecked():
                bill += 5.0
            if self.checkSWSalad.isChecked():
                bill += 5.5
            if self.checkFries.isChecked():
                bill += 1.25
            if self.checkCFries.isChecked():
                bill += 1.75
            if self.checkSideSalad.isChecked():
                bill += 2.0
            if self.checkChips.isChecked():
                bill += 1.75
            if self.checkSmlSoda.isChecked():
                bill += 1.0
            if self.checkMedSoda.isChecked():
                bill += 1.5
            if self.checkLrgSoda.isChecked():
                bill += 2.
            checked = [self.buttonGroup.buttons()[x].isChecked() for x in range(len(self.buttonGroup.buttons()))].index(
                True)
            if checked == 0:
                tip_amount = .1
            elif checked == 1:
                tip_amount = .15
            elif checked == 2:
                tip_amount = .2
            tax = bill * .1
            tip = ((tax + bill) * tip_amount)
            total_amount = bill + tax + tip
            self.labelTotal.setText(
                'Bill Summary:\n'
                '\n'
                f'Order total:  ${bill:.2f}\n'
                f'Tax:          ${tax:.2f}\n'
                f'Tip:          ${tip:.2f}\n'
                f'Total Amount: ${total_amount:.2f}')
        except ValueError:
            self.labelTotal.setText('At least one menu item needs to be selected.')

    def clear(self):
        self.radioButton10.setChecked(True)
        self.labelTotal.setText('Bill Summary:')

