# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EnterNameUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(803, 599)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(210, 190, 391, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.namelabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.namelabel.setFont(font)
        self.namelabel.setObjectName("namelabel")
        self.horizontalLayout.addWidget(self.namelabel)
        self.namefield = QtWidgets.QPlainTextEdit(self.widget)
        self.namefield.setObjectName("namefield")
        self.horizontalLayout.addWidget(self.namefield)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scorlabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.scorlabel.setFont(font)
        self.scorlabel.setObjectName("scorlabel")
        self.verticalLayout.addWidget(self.scorlabel)
        self.submitBtn = QtWidgets.QPushButton(self.widget)
        self.submitBtn.setObjectName("sybmitBtn")
        self.verticalLayout.addWidget(self.submitBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.namelabel.setText(_translate("Form", "Enter name"))
        self.scorlabel.setText(_translate("Form", "Your score:"))
        self.submitBtn.setText(_translate("Form", "Submit"))

