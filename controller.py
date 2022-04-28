from PyQt5.QtWidgets import *
from areaInput import Ui_MainWindow
from rashawn_thompson import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.submitButton.clicked.connect(lambda: self.submit())

    def reset_fields(self) -> None:
        """
        This method resets all the input fields to initial states
        """
        self.shapeSelect.setCurrentIndex(0)
        self.baseInput.clear()
        self.heightInput.clear()

    def submit(self) -> None:
        """
        Determines what shape was selected and uses the corresponding function to calculate the result,
        then prints the result to the appropriate box. After that, it resets all the fields.
        """
        shape = self.shapeSelect.currentText()
        base = self.baseInput.text()
        height = self.baseInput.text()

        # wrong value type/empty value handling
        if base.isdigit():
            base = float(base)
        elif base == '':
            base = 1
        else:
            self.resultBox.setText('Use Number!')

        if height.isdigit():
            height = float(height)
        elif height == '':
            height = 1
        else:
            self.resultBox.setText('Use Number!')

        if shape == 'Select':
            self.resultBox.setText('Select your shape!')
        if shape == 'Square' or shape == 'Circle':
            if shape == 'Square':
                self.resultBox.setPlainText(f'{square(base):.2f}')
                self.reset_fields()
            else:
                self.resultBox.setPlainText(f'{circle(base):.2f}')
                self.reset_fields()
        if shape == 'Rectangle' or shape == 'Triangle':
            if shape == 'Rectangle':
                self.resultBox.setPlainText(f'{rectangle(base, height):.2f}')
                self.reset_fields()
            else:
                self.resultBox.setPlainText(f'{triangle(base, height):.2f}')
                self.reset_fields()
