from PyQt5.QtWidgets import *
from areaInput import Ui_MainWindow
from rashawn_thompson import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.hide_fields()

        self.submitButton.clicked.connect(lambda: self.submit())
        self.shapeSelect.currentTextChanged.connect(lambda: self.changed())

    def hide_fields(self) -> None:
        """
        This method hides all the input fields and corresponding labels for initialization
        """
        self.baseLabel.hide()
        self.baseInput.hide()
        self.heightInput.hide()
        self.heightLabel.hide()

    def check_base(self, base: str) -> bool:
        """
        This method checks if the value passed into it through parameter base is
        valid and outputs text giving a hint on why the value was not valid
        :param base: string value that is checked for validity
        :return: boolean value that allows the submit button functionality to work properly
        """
        if base.isdigit() and base != '0':
            return True
        elif base == '':
            self.resultBox.setPlainText('Enter a Value')
            return False
        else:
            self.resultBox.setPlainText('Use Valid Number!')
            return False

    def check_height(self, height: str) -> bool:
        """
        This method checks if the value passed into it through parameter height is
        valid and outputs text giving a hint on why the value was not valid
        :param height: string value that is checked for validity
        :return: boolean value that allows the submit button functionality to work properly
        """
        if height.isdigit() and height != '0':
            return True
        elif height == '':
            self.resultBox.setPlainText('Enter a Value')
            return False
        else:
            self.resultBox.setPlainText('Use Valid Number!')
            return False

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
        height = self.heightInput.text()

        if shape == 'Select':
            self.resultBox.setText('Select your shape!')

        elif shape == 'Square' and self.check_base(base):
            base = float(base)
            self.resultBox.setPlainText(f'{square(base):.2f}')
            self.reset_fields()

        elif shape == 'Circle' and self.check_base(base):
            base = float(base)
            self.resultBox.setPlainText(f'{circle(base):.2f}')
            self.reset_fields()

        elif shape == 'Rectangle' and (self.check_base(base) and self.check_height(height)):
            base = float(base)
            height = float(height)
            self.resultBox.setPlainText(f'{rectangle(base, height):.2f}')
            self.reset_fields()

        elif shape == 'Triangle' and (self.check_base(base) and self.check_height(height)):
            base = float(base)
            height = float(height)
            self.resultBox.setPlainText(f'{triangle(base, height):.2f}')
            self.reset_fields()

        else:
            pass

    def changed(self):
        if self.shapeSelect.currentText() == 'Circle' or self.shapeSelect.currentText() == 'Square':
            self.baseLabel.show()
            self.baseInput.show()
            self.heightLabel.hide()
            self.heightInput.hide()

        elif self.shapeSelect.currentText() == 'Rectangle' or self.shapeSelect.currentText() == 'Triangle':
            self.baseLabel.show()
            self.baseInput.show()
            self.heightLabel.show()
            self.heightInput.show()

        else:
            self.hide_fields()
