from PyQt5.QtWidgets import QWidget
from UI.ScoreTableUI import Ui_Form
from PyQt5.QtCore import pyqtSignal
import sqlite3

class ScoreTableWidget(QWidget, Ui_Form):
    
    back = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.baskBtn.clicked.connect(self.back.emit)

        self.scores = [self.score_1, self.score_2, self.score_3, self.score_4,
                       self.score_5, self.score_6, self.score_7, self.score_8]

        self.reload()


    def reload(self):
        con = sqlite3.connect("Widgets/pyqt_data.db")
        cursor = con.cursor()

        data = cursor.execute("""select * from Scores""").fetchall()
        noramlized_data = {}
        for row in data:
            if row[0] in noramlized_data.keys():
                noramlized_data[row[0]] = max(row[1], noramlized_data[row[0]])
            else:
                noramlized_data[row[0]] = int(row[1])

        sorted_data = sorted(noramlized_data.items(), key=lambda x: x[1], reverse=True)
        m = 8
        if len(sorted_data) < 8:
            sorted_data += [("no one", 0)] * (8 - len(sorted_data))
        for i, score in enumerate(self.scores):
            line = sorted_data[i][0] + " " + str(sorted_data[i][1])
            score.setText(line)
            
        con.close()