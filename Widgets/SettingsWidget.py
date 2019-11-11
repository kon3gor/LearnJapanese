from PyQt5.QtWidgets import QWidget
from UI.SettingsUI import Ui_Form
from PyQt5.QtCore import pyqtSignal

class SettingsWidget(QWidget, Ui_Form):
    
    back = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.setupUi(self) 
        self.par = parent

        self.baskBtn.clicked.connect(self.check_alph)
        with open("Widgets/alphabet.txt", "r") as file:
            if file.read().strip(" \n\t") == "k":
                self.katakanaBtn.setChecked(True)
            else:
                self.hiraganaBtn.setChecked(True)
    
    def check_alph(self):
        with open("Widgets/alphabet.txt", "w") as file:
            if self.katakanaBtn.isChecked():
                file.write("k")
            else:
                file.write("h")
        self.back.emit()