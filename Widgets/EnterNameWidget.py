from PyQt5.QtWidgets import QWidget
from UI.EnterNameUI import Ui_Form
from PyQt5.QtCore import pyqtSignal
import sqlite3

class EnterNameWidget(QWidget, Ui_Form):
    
    submit = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.submitBtn.clicked.connect(self.proccess)
        with open("Widgets/score.txt", "r") as file:
            self.score = file.read().strip(" \t\n")
            file.close()
            self.scorlabel.setText(f"Your score: {self.score}")


    def proccess(self):
        if self.namefield.toPlainText() != "":
            con = sqlite3.connect("Widgets/pyqt_data.db")
            cursor = con.cursor()

            person_name = self.namefield.toPlainText().strip(" \t\n")

            cursor.execute(f"""INSERT INTO Scores VALUES (?, ?)""", (person_name, self.score))
            con.commit()
            con.close()
            self.submit.emit()
            

    def reload(self):
        with open("Widgets/score.txt", "r") as file:
            self.score = file.read().strip(" \t\n")
            file.close()
        self.scorlabel.setText(f"Your score: {self.score}")




