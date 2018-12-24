import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import json
from PyQt5.QtCore import Qt
from build_script import design

root_game = []
otvet = []



class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.addComment)
        self.pushButton2.clicked.connect(self.gen)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.del_list)
        self.lcdNumber.display(0)
        self.show()

    def addComment(self):
        otvet.append({"text": self.lineEdit_2.text(), "schena": int(self.spinBox.text())})
        nomer = 1
        self.listWidget.clear()
        for item in otvet:
            self.listWidget.addItem(str(nomer) + ' ' + item['text'] + ' -----> ' + str(item['schena']))
            nomer += 1

    def gen(self):
        self.spinBox.clear()
        self.lineEdit_2.clear()
        self.listWidget.clear()
        root_game.append({"text": self.textEdit.toPlainText(), "otvet": otvet.copy(), "Hard": int(self.lineEdit_4.text()),"hangre": int(self.lineEdit_3.text()), "root": int(self.spinBox_2.text())})
        self.lcdNumber.display(len(root_game))
        for x in otvet:
            del otvet[0]
        if len(otvet) != 0:
            del otvet[0]

    def del_list(self):
        if len(otvet) != 0:
            del otvet[len(otvet)-1]
        nomer = 1
        self.listWidget.clear()
        for item in otvet:
            self.listWidget.addItem(str(nomer) + ' ' + item['text'] + ' -----> ' + str(item['schena']))
            nomer += 1


    def save(self):
        with open('root.json', 'w') as outfile:
            json.dump(root_game, outfile)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.addComment()
        el


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()
