# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(807, 609)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 60, 581, 511))
        self.layoutWidget.setObjectName("layoutWidget")
        self.widget_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setObjectName("widget_layout")
        self.bestscore_layout = QtWidgets.QVBoxLayout()
        self.bestscore_layout.setObjectName("bestscore_layout")
        self.bestscore_text = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(28)
        self.bestscore_text.setFont(font)
        self.bestscore_text.setAlignment(QtCore.Qt.AlignCenter)
        self.bestscore_text.setObjectName("bestscore_text")
        self.bestscore_layout.addWidget(self.bestscore_text)
        self.bestscore_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(28)
        self.bestscore_2.setFont(font)
        self.bestscore_2.setAlignment(QtCore.Qt.AlignCenter)
        self.bestscore_2.setObjectName("bestscore_2")
        self.bestscore_layout.addWidget(self.bestscore_2)
        self.btn_layout = QtWidgets.QVBoxLayout()
        self.btn_layout.setObjectName("btn_layout")
        self.learnBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.learnBtn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.learnBtn.setFont(font)
        self.learnBtn.setObjectName("learnBtn")
        self.btn_layout.addWidget(self.learnBtn)
        self.scoreBtn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.scoreBtn.setFont(font)
        self.scoreBtn.setObjectName("scoreBtn")
        self.btn_layout.addWidget(self.scoreBtn)
        self.settingsBtn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.settingsBtn.setFont(font)
        self.settingsBtn.setObjectName("settingsBtn")
        self.btn_layout.addWidget(self.settingsBtn)
        self.bestscore_layout.addLayout(self.btn_layout)
        self.widget_layout.addLayout(self.bestscore_layout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bestscore_text.setText(_translate("Form", "BEST SCORE"))
        self.bestscore_2.setText(_translate("Form", "0"))
        self.learnBtn.setText(_translate("Form", "Learn"))
        self.scoreBtn.setText(_translate("Form", "Score table"))
        self.settingsBtn.setText(_translate("Form", "Settings"))

