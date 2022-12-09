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

    # Total push button, calculates total of all selected menu items
    # Counts for quantity requested in spin box
    def total(self):
        try:
            bill = float(0)
            if self.checkBurger.isChecked():
                qty = self.spinBoxBur.value()
                amount = 6.0 * qty
                bill += amount
            if self.checkChsBurger.isChecked():
                qty = self.spinBoxCBur.value()
                amount = 6.5 * qty
                bill += amount
            if self.checkChkSand.isChecked():
                qty = self.spinBoxCSnd.value()
                amount = 5.5 * qty
                bill += amount
            if self.checkSChkSand.isChecked():
                qty = self.spinBoxSCSnd.value()
                amount = 5.5 * qty
                bill += amount
            if self.checkCSalad.isChecked():
                qty = self.spinBoxCSalad.value()
                amount = 5.0 * qty
                bill += amount
            if self.checkGSalad.isChecked():
                qty = self.spinBoxGSalad.value()
                amount = 5.0 * qty
                bill += amount
            if self.checkSWSalad.isChecked():
                qty = self.spinBoxSWSalad.value()
                amount = 5.5 * qty
                bill += amount
            if self.checkFries.isChecked():
                qty = self.spinBoxFries.value()
                amount = 1.25 * qty
                bill += amount
            if self.checkCFries.isChecked():
                qty = self.spinBoxCFries.value()
                amount = 1.75 * qty
                bill += amount
            if self.checkSideSalad.isChecked():
                qty = self.spinBoxSideSalad.value()
                amount = 2.0 * qty
                bill += amount
            if self.checkChips.isChecked():
                qty = self.spinBoxChips.value()
                amount = 1.75 * qty
                bill += amount
            if self.checkSmlSoda.isChecked():
                qty = self.spinBoxSml.value()
                amount = 1.0 * qty
                bill += amount
            if self.checkMedSoda.isChecked():
                qty = self.spinBoxMed.value()
                amount = 1.5 * qty
                bill += amount
            if self.checkLrgSoda.isChecked():
                qty = self.spinBoxLrg.value()
                amount = 2.0 * qty
                bill += amount
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

    # Clears all selected items to 'submit' a new order.
    def clear(self):
        self.radioButton10.setChecked(True)
        self.labelTotal.setText('Bill Summary:')
        self.checkBurger.setChecked(False)
        self.checkChsBurger.setChecked(False)
        self.checkChkSand.setChecked(False)
        self.checkSChkSand.setChecked(False)
        self.checkCSalad.setChecked(False)
        self.checkGSalad.setChecked(False)
        self.checkSWSalad.setChecked(False)
        self.checkFries.setChecked(False)
        self.checkCFries.setChecked(False)
        self.checkSideSalad.setChecked(False)
        self.checkChips.setChecked(False)
        self.checkSmlSoda.setChecked(False)
        self.checkMedSoda.setChecked(False)
        self.checkLrgSoda.setChecked(False)
        self.checkWater.setChecked(False)
        self.spinBoxBur.setValue(1)
        self.spinBoxCBur.setValue(1)
        self.spinBoxCSnd.setValue(1)
        self.spinBoxSCSnd.setValue(1)
        self.spinBoxCSalad.setValue(1)
        self.spinBoxGSalad.setValue(1)
        self.spinBoxSWSalad.setValue(1)
        self.spinBoxFries.setValue(1)
        self.spinBoxCFries.setValue(1)
        self.spinBoxSideSalad.setValue(1)
        self.spinBoxChips.setValue(1)
        self.spinBoxSml.setValue(1)
        self.spinBoxMed.setValue(1)
        self.spinBoxLrg.setValue(1)
        self.spinBoxWater.setValue(1)


