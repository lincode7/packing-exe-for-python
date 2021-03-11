# -*- coding: utf-8 -*-
import os, sys

# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI_packing import Ui_MainWindow


class MySignal(QObject):
    visable = pyqtSignal(object, bool)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        cwd = os.getcwd()
        img = r'resources\img\packing.ico'
        font = r'resources\font\*.ttf'
        self.setWindowIcon(QIcon(os.path.join(cwd, img)))
        QFontDatabase.addApplicationFont(os.path.join(cwd, font))

        self.ms = MySignal()
        self.signal_action()
        self.setui()

        self.py = []
        self.ico = r''
        self.resrc = []
        self.outpath = r''

    def packing(self):
        self.packbutton.setEnabled(False)

        # runtimehook = os.path.join(os.getcwd(), 'Filter.ui')
        # pyinstaller -F -w temp.py -n name -i 1.ico --add-data "test.json;data" --add-data "python.README;data" --clean
        if self.py:
            pack = 'pyinstaller'
            if self.checkBox_F.isChecked():  # 是否生成单文件
                pack += ' -F'
            if self.checkBox_w.isChecked():  # 是否关闭控制台
                pack += ' -w'

            pack += ' ' + self.python.toPlainText()

            if self.checkBox_n.isChecked():  # 是否重命名
                if self.nameEdit.text():
                    pack += ' -n ' + self.nameEdit.text()
            if self.checkBox_i.isChecked():  # 是否添加图标
                if self.icon.toPlainText():
                    pack += ' -i ' + self.icon.toPlainText()
                else:
                    print('no icon')
                    msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'no icon!')
                    msg_box.exec_()
            if self.resources.toPlainText():  # 是否打包资源文件
                pack += r' –add-data "' + self.resources.toPlainText() + r':' + 'resources' + r'"'

            pack += ' --clean'  # 在每次编译生成exe时，清除之前的编译文件
            print(pack)
            # os.system(pack)
        else:
            print('no python filie!')
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'no python filie!')
            msg_box.exec_()
        self.buttonpack.setEnabled(True)

    def buildpath(self):
        self.pathbutton.setEnabled(False)
        path = self.pathEdit.text()
        if path:
            QFileDialog.getExistingDirectory(self, "请选择文件夹路径", path)
        else:
            QFileDialog.getExistingDirectory(self, "请选择文件夹路径", ".")
        self.pathbutton.setEnabled(True)

    def setui(self):
        self.ms.visable.emit(self.nameEdit, False)

    def signal_action(self):
        # print(1)
        self.python.textChanged.connect(self.setpy)
        self.icon.textChanged.connect(self.setico)
        self.resources.textChanged.connect(self.setsource)
        self.pathbutton.clicked.connect(self.buildpath)
        self.clearbutton.clicked.connect(self.clear)
        self.packbutton.clicked.connect(self.packing)
        self.checkBox_n.clicked.connect(self.check_n)
        self.ms.visable.connect(self.setshow)

    def setpy(self):
        # 获取py文件路径，可以多个
        path = self.python.toPlainText()
        if 'file:///' in path: # 删除拖放文件的前缀
            path = path.lstrip('file:///')
            self.python.setText(path + '\r\n')
            if self.py == []:  # 第1个py文件入列
                self.py.append(path)
            elif '\r\n' in path:  # 第2个开始的py文件加入列表
                path = path.split('\r\n')
                for i in path:
                    if i not in self.py:
                        self.py.append(i)
            print(self.py)
            print(0)

        if self.outpath == '': # 从第一个py文件确定默认打包路径
            p, f = os.path.split(self.py)
            self.outpath = os.path.join(p, 'build')
            self.pathEdit.setText(self.outpath)


    def setico(self):
        path = self.icon.toPlainText()
        if 'file:///' in path:
            self.ico = path.lstrip('file:///')
            self.icon.setText(self.ico)



    def setsource(self):
        self.resrc = self.resources.toPlainText()
        if 'file:///' in self.resrc:
            self.resrc = self.resrc.lstrip('file:///')
            self.resources.setText(self.resrc + '\r\n')


    def clear(self):
        self.py = []
        self.ico = r''
        self.resrc = []
        self.outpath = r''
        self.python.clear()
        self.icon.clear()
        self.resources.clear()
        self.pathEdit.clear()
        self.nameEdit.clear()
        self.ms.visable.emit(self.nameEdit, False)
        self.checkBox_n.setChecked(False)


    def check_n(self):
        if self.checkBox_n.isChecked():
            self.ms.visable.emit(self.nameEdit, True)
        else:
            self.ms.visable.emit(self.nameEdit, False)


    def setshow(self, ui, flag):
        if isinstance(ui, list):
            for one in ui:
                one.setVisible(flag)
        else:
            ui.setVisible(flag)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.show()
    sys.exit(app.exec_())
