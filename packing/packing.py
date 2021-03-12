# -*- coding: utf-8 -*-
import os, sys, traceback

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtCore import QObject, pyqtSignal
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

    def setui(self):
        self.ms.visable.emit(self.nameEdit, False)
        self.ms.visable.emit(self.moreselection, False)
        self.path = ''
        self.py = []
        self.ico = ''
        self.resrc = []
        self.outpath = ''
        self.ms.visable.emit(self.resources, False)
        self.ms.visable.emit(self.label_4, False)
        self.ms.visable.emit(self.line_3, False)

    def signal_action(self):
        self.python.textChanged.connect(self.setpy)
        self.icon.textChanged.connect(self.setico)
        self.resources.textChanged.connect(self.setsource)
        self.morefilebutton.clicked.connect(self.morefile)
        self.pathbutton.clicked.connect(self.buildpath)
        self.clearbutton.clicked.connect(self.clear)
        self.packbutton.clicked.connect(self.packing)
        self.checkBox_n.clicked.connect(self.check_n)
        self.ms.visable.connect(self.setshow)

    def setpy(self):
        # 获取py文件路径，可以多个
        path = self.python.toPlainText()

        if 'file:///' in path:  # 删除拖放文件的前缀
            path = path.replace('file:///', '')
            self.python.setText(path + '\n')

            if '\n' in path:  # 多个文件时删除换行符
                path = path.split('\n')
            if self.py:  # 第2个及更多py
                for i in path:
                    if i not in self.py and i != '':
                        self.py.append(i)
            else:  # 第1个py
                if isinstance(path, str):
                    self.py.append(path)
                    if self.outpath == '':  # 从第一个py文件确定默认打包路径
                        p = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")  # 得到父目录
                        self.outpath = os.path.join(p, 'build')  # 设置build目录
                        self.pathEdit.setText(self.outpath)
                elif isinstance(path, list):
                    self.py = path[:-1]
                    if self.outpath == '':  # 从第一个py文件确定默认打包路径
                        p = os.path.abspath(os.path.dirname(path[0]) + os.path.sep + ".")  # 得到父目录
                        self.outpath = os.path.join(p, 'build')  # 设置build目录,第一个py文件同目录下简历build文件夹存放生成文件
                        self.pathEdit.setText(self.outpath)
            # print('.py:', self.py)

    def setico(self):
        path = self.icon.toPlainText()
        if 'file:///' in path:
            if self.ico:
                self.ico = (path.replace('file:///', '')).replace(self.ico, '')  # 用新的ico替换原来的ico
            else:
                self.ico = path.replace('file:///', '')
            if self.ico.endswith('.ico'):
                self.icon.setText(self.ico)
                # print('.ico:', self.ico)
            else:
                self.icon.clear()
                QMessageBox.warning(self, '警告', '非ico图标文件')

    def setsource(self):
        # 获取py文件路径，可以多个
        path = self.resources.toPlainText()
        if 'file:///' in path:  # 删除拖放文件的前缀
            path = path.replace('file:///', '')
            self.resources.setText(path + '\n')

            if '\n' in path:  # 多个文件时删除换行符
                path = path.split('\n')
            if self.resrc:  # 第2个及更多资源文件
                for i in path:
                    if i not in self.resrc and i != '':
                        self.resrc.append(i)
            else:  # 第1个资源文件
                self.resrc = []
                if isinstance(path, str):
                    self.resrc.append(path)
                elif isinstance(path, list):
                    self.resrc = path[:-1]
            # 资源文件分类，img，font，data，ui
            # print('resrc:', self.resrc)

    def morefile(self):
        self.morefilebutton.setEnabled(False)
        if self.moreselection.isVisible():
            self.ms.visable.emit(self.moreselection, False)
            self.morefilebutton.setText('more')
        else:
            self.ms.visable.emit(self.moreselection, True)
            self.morefilebutton.setText('↑')
        self.morefilebutton.setEnabled(True)

    def buildpath(self):
        self.pathbutton.setEnabled(False)
        path = self.pathEdit.text()
        if path:
            QFileDialog.getExistingDirectory(self, "请选择文件夹路径", path)
        else:
            QFileDialog.getExistingDirectory(self, "请选择文件夹路径", ".")
        self.pathbutton.setEnabled(True)

    def clear(self):
        self.path = ''
        self.py = []
        self.ico = ''
        self.resrc = []
        self.outpath = ''

        self.python.clear()
        self.icon.clear()
        self.resources.clear()
        self.pathEdit.clear()
        self.nameEdit.clear()
        self.ms.visable.emit(self.nameEdit, False)
        self.checkBox_F.setChecked(False)
        self.checkBox_n.setChecked(False)

    def packing(self):
        self.packbutton.setEnabled(False)

        # runtimehook = os.path.join(os.getcwd(), 'Filter.ui')
        # pyinstaller -p E:\program\build -F -w -n name 1.py 2.py 3.py -i 1.ico --add-data "1.json;data" --add-data "2.font" --add-data "3.png" --clean
        if self.py:
            pack = 'pyinstaller'
            if self.checkBox_F.isChecked():  # 是否生成单文件
                pack += ' -F'
            if self.checkBox_w.isChecked():  # 是否关闭控制台
                pack += ' -w'
            if self.checkBox_n.isChecked() and self.nameEdit.text():  # 是否重命名
                pack += r' -n {}'.format(self.nameEdit.text())
            for i in self.py:
                if i != '':
                    pack += r' {}'.format(i)
            if self.ico:  # 是否添加图标
                pack += r' -i {}'.format(self.ico)
            # if self.resrc:  # 是否打包资源文件
            #     for i in self.resrc:
            #         if i.endswith('.ttf'):
            #             pack += r' -–add-data "{};resources\font"'.format(i)
            #         elif i.endswith('.jpg') or i.endswith('.png') or i.endswith('.ico'):
            #             pack += r' -–add-data "{};resources\img"'.format(i)
            #         elif i.endswith('.ui'):
            #             pack += r' -–add-data "{};resources\ui"'.format(i)
            #         else:
            #             pack += r' -–add-data "{};resources\data"'.format(i)

            pack += r' --workpath {}  --distpath {} --specpath {} -y --clean'.format(os.path.join(self.outpath, 'temp'), os.path.join(self.outpath, 'final'),self.outpath)  # 在每次编译生成exe时，清除之前的编译文件
            print(pack)
            os.system(pack)
        else:
            print('no python filie!')
            QMessageBox.warning(self, 'Warning', 'no python filie!')

        self.packbutton.setEnabled(True)

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
    try:
        app = QApplication(sys.argv)
        MW = MainWindow()
        MW.show()
        sys.exit(app.exec_())
    except Exception:
        print(traceback.format_exc())
