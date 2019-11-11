from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget
from UI.MainWidgetUI import Ui_Form
from PyQt5.QtCore import pyqtSignal
import sqlite3


class MainWidget(QWidget, Ui_Form):

    learning = pyqtSignal()
    settings = pyqtSignal()
    score_table = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.learnBtn.clicked.connect(self.learning.emit)
        self.settingsBtn.clicked.connect(self.settings.emit)
        self.scoreBtn.clicked.connect(self.score_table.emit)
        self.reload()

    
    def reload(self):
        con = sqlite3.connect("Widgets/pyqt_data.db")
        cursor = con.cursor()

        max_score = cursor.execute("""select max(score) from Scores""").fetchone()
        self.bestscore_2.setText(str(max_score[0]))
        con.close()
        