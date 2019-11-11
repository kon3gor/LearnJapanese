# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(805, 609)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(310, 200, 171, 371))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.katakanaBtn = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.katakanaBtn.setFont(font)
        self.katakanaBtn.setObjectName("katakanaBtn")
        self.verticalLayout.addWidget(self.katakanaBtn)
        self.hiraganaBtn = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hiraganaBtn.setFont(font)
        self.hiraganaBtn.setObjectName("hiraganaBtn")
        self.verticalLayout.addWidget(self.hiraganaBtn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(166, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.baskBtn = QtWidgets.QPushButton(self.widget)
        self.baskBtn.setObjectName("baskBtn")
        self.verticalLayout_2.addWidget(self.baskBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Alphabet"))
        self.katakanaBtn.setText(_translate("Form", "Katakana"))
        self.hiraganaBtn.setText(_translate("Form", "Hiragana"))
        self.baskBtn.setText(_translate("Form", "Back"))