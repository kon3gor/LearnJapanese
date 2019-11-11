from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from Widgets.MainWigdet import MainWidget
from Widgets.LearningWidget import LearnWidget
from Widgets.SettingsWidget import SettingsWidget
from Widgets.ScoreTableWidget import ScoreTableWidget
from Widgets.EnterNameWidget import EnterNameWidget


class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.resize(807, 584)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.learning_widget = LearnWidget(self)
        self.main_widget = MainWidget(self)
        self.settings_widget = SettingsWidget(self)
        self.scoretable_widget = ScoreTableWidget(self)
        self.entername_widget = EnterNameWidget(self)

        self.central_widget.addWidget(self.main_widget)
        self.central_widget.addWidget(self.learning_widget)
        self.central_widget.addWidget(self.settings_widget)
        self.central_widget.addWidget(self.scoretable_widget)
        self.central_widget.addWidget(self.entername_widget)

        self.central_widget.setCurrentWidget(self.main_widget)

        self.main_widget.learning.connect(self.reload_leraning)
        self.main_widget.settings.connect(lambda: 
                                         self.central_widget.setCurrentWidget(self.settings_widget))
        self.main_widget.score_table.connect(self.reload_table)
        self.learning_widget.finish.connect(self.reload_entername)
        self.entername_widget.submit.connect(self.reload_main)
        self.settings_widget.back.connect(self.reload_main)
        self.scoretable_widget.back.connect(self.reload_main)
        

    def reload_entername(self):
        self.central_widget.setCurrentWidget(self.entername_widget)
        self.entername_widget.reload()


    def reload_leraning(self):
        self.central_widget.setCurrentWidget(self.learning_widget)
        self.learning_widget.reload()

    
    def reload_table(self):
        self.central_widget.setCurrentWidget(self.scoretable_widget)
        self.scoretable_widget.reload()

    
    def reload_main(self):
        self.central_widget.setCurrentWidget(self.main_widget)
        self.main_widget.reload()
