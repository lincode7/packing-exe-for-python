# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 433)
        MainWindow.setMinimumSize(QtCore.QSize(400, 0))
        MainWindow.setWindowOpacity(0.95)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(180, 180, 180)\n"
"}\n"
".QPushButton{\n"
"    border-radius: 5px;\n"
"    font: 20pt \"Dirnaith\";\n"
"    color: white;\n"
"    background-color: rgb(102, 102, 102);\n"
"}\n"
".QPushButton:hover { \n"
"    color: black;\n"
"    background-color: rgb(124, 208, 190);\n"
"}\n"
".QPushButton:pressed { \n"
"    color: black;\n"
"    background-color: rgb(152, 255, 233);\n"
"}\n"
".QLineEdit{\n"
"    font: 14pt \"Consolas\";\n"
"    border-color: rgb(80, 156, 255);\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
".QLineEdit:focus {\n"
"    padding: 1px;\n"
"    border: 3px solid rgb(239, 176, 74);\n"
"}\n"
".QTextEdit{\n"
"    border-radius: 5px;\n"
"    font: 14pt \"Consolas\";\n"
"    color: black;\n"
"    background-color: rgb(231, 231, 231);\n"
"}\n"
".QTextEdit:focus {\n"
"    padding: 1px;\n"
"    border: 3px solid rgb(132, 132, 132);\n"
"    color: black;\n"
"}\n"
".QLabel{\n"
"    font: 14pt \"Dirnaith\";\n"
"    background-color: transparent;\n"
"}\n"
".QCheckBox{\n"
"    border-radius: 5px;\n"
"    font: 14pt \"Consolas\";\n"
"    color: rgb(231, 228, 142);\n"
"    background-color: rgb(106, 106, 106);\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(512, 512))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.python = QtWidgets.QTextEdit(self.centralwidget)
        self.python.setAcceptDrops(True)
        self.python.setObjectName("python")
        self.verticalLayout_3.addWidget(self.python)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.moreselection = QtWidgets.QFrame(self.centralwidget)
        self.moreselection.setObjectName("moreselection")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.moreselection)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.moreselection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.icon = QtWidgets.QTextEdit(self.moreselection)
        self.icon.setAcceptDrops(True)
        self.icon.setObjectName("icon")
        self.verticalLayout_2.addWidget(self.icon)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.line_3 = QtWidgets.QFrame(self.moreselection)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.moreselection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.resources = QtWidgets.QTextEdit(self.moreselection)
        self.resources.setAcceptDrops(True)
        self.resources.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.resources.setObjectName("resources")
        self.verticalLayout.addWidget(self.resources)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_6.addWidget(self.moreselection)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.morefilebutton = QtWidgets.QPushButton(self.centralwidget)
        self.morefilebutton.setStyleSheet("font: 12pt;")
        self.morefilebutton.setObjectName("morefilebutton")
        self.horizontalLayout_5.addWidget(self.morefilebutton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pathEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathEdit.setInputMask("")
        self.pathEdit.setText("")
        self.pathEdit.setObjectName("pathEdit")
        self.horizontalLayout_3.addWidget(self.pathEdit)
        self.pathbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pathbutton.setStyleSheet("font: 16pt \"5Zlash\";")
        self.pathbutton.setObjectName("pathbutton")
        self.horizontalLayout_3.addWidget(self.pathbutton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_F = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_F.setChecked(False)
        self.checkBox_F.setObjectName("checkBox_F")
        self.horizontalLayout_2.addWidget(self.checkBox_F)
        self.checkBox_w = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_w.setChecked(True)
        self.checkBox_w.setObjectName("checkBox_w")
        self.horizontalLayout_2.addWidget(self.checkBox_w)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_n = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_n.setChecked(False)
        self.checkBox_n.setTristate(False)
        self.checkBox_n.setObjectName("checkBox_n")
        self.verticalLayout_5.addWidget(self.checkBox_n)
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout_5.addWidget(self.nameEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.clearbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearbutton.sizePolicy().hasHeightForWidth())
        self.clearbutton.setSizePolicy(sizePolicy)
        self.clearbutton.setObjectName("clearbutton")
        self.horizontalLayout.addWidget(self.clearbutton)
        self.packbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packbutton.sizePolicy().hasHeightForWidth())
        self.packbutton.setSizePolicy(sizePolicy)
        self.packbutton.setObjectName("packbutton")
        self.horizontalLayout.addWidget(self.packbutton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Packing For Py"))
        self.label.setText(_translate("MainWindow", "Python file"))
        self.python.setPlaceholderText(_translate("MainWindow", "此处放置python文件"))
        self.label_2.setText(_translate("MainWindow", "icon file"))
        self.icon.setPlaceholderText(_translate("MainWindow", "此处放置图标文件，非必要"))
        self.label_4.setText(_translate("MainWindow", "Resources file"))
        self.resources.setToolTip(_translate("MainWindow", "<html><head/><body><p>通过.ui文件导入的程序需要将ui文件放在这，或者是其他需要放在同目录下的额外文件</p></body></html>"))
        self.resources.setPlaceholderText(_translate("MainWindow", "此处放置额外资源文件，支持图片和data数据（xml，csv，json等）"))
        self.morefilebutton.setText(_translate("MainWindow", "more"))
        self.label_3.setText(_translate("MainWindow", "Output Path"))
        self.pathEdit.setPlaceholderText(_translate("MainWindow", "输出路径"))
        self.pathbutton.setText(_translate("MainWindow", "···"))
        self.checkBox_F.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt;\">只在dist中生产一个demo.exe文件</span></pre><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt;\">取消则是-D默认参数，生成exe加依赖文件</span></pre></body></html>"))
        self.checkBox_F.setText(_translate("MainWindow", "-F"))
        self.checkBox_w.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Apple Color Emoji\',\'Segoe UI Emoji\',\'Segoe UI Symbol\',\'Segoe UI\',\'PingFang SC\',\'Hiragino Sans GB\',\'Microsoft YaHei\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:9pt; color:#404040; background-color:rgba(179,179,179,0.14902);\">只对windows有效，不使用控制台，黑框。</span></p></body></html>"))
        self.checkBox_w.setText(_translate("MainWindow", "-w"))
        self.checkBox_n.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">改变exe名字，默认与主py程序同名。</span></p></body></html>"))
        self.checkBox_n.setText(_translate("MainWindow", "-n"))
        self.nameEdit.setPlaceholderText(_translate("MainWindow", "更新文件名"))
        self.clearbutton.setText(_translate("MainWindow", "clear"))
        self.packbutton.setText(_translate("MainWindow", "GO"))
