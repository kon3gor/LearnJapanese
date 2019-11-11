import sys
from PyQt5.QtWidgets import QApplication
from Widgets.Application import App


app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())
