# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subForm_1(QtWidgets.QWidget, object):
    def setupUi(self, subForm_1):
        subForm_1.setObjectName("subForm_1")
        subForm_1.resize(731, 536)
        self.gridLayout_2 = QtWidgets.QGridLayout(subForm_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(subForm_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(subForm_1)
        self.frame.setMinimumSize(QtCore.QSize(691, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(subForm_1)
        self.textBrowser.setMinimumSize(QtCore.QSize(701, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 2, 0, 1, 1)

        self.retranslateUi(subForm_1)
        QtCore.QMetaObject.connectSlotsByName(subForm_1)

    def retranslateUi(self, subForm_1):
        _translate = QtCore.QCoreApplication.translate
        subForm_1.setWindowTitle(_translate("subForm_1", "Form"))
        self.label.setText(_translate("subForm_1", "爬虫选项"))
        self.label_2.setText(_translate("subForm_1", "保存路径："))
        self.pushButton.setText(_translate("subForm_1", "开始爬取"))
        self.pushButton_2.setText(_translate("subForm_1", "选择路径"))
        self.pushButton_3.setText(_translate("subForm_1", "停止爬取"))
