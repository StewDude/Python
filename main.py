#def main():
#    app = QtGui.QApplication(sys.argv)
#    window = Window()
#    window.show()
#    sys.exit(app.exec_())
#
#if __name__ == "__main__": main()

#from PyQt5.QtWidgets import QTreeView, QFileSystemModel, QApplication
#
#class Main(QTreeView):
#    def __init__(self):
#        QTreeView.__init__(self)
#        model = QFileSystemModel()
#        model.setRootPath("\\DS3615xs_1")
#        self.setModel(model)
#        self.doubleClicked.connect(self.test)

#    def test(self, signal):
#        file_path=self.model().filePath(signal)
#        print(file_path)

#if __name__ == "__main__":
#    import sys
#    app = QApplication(sys.argv)
#    w = Main()
#    w.show()
#    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 file system view - pythonspot.com"
        self.left = 100
        self.top = 300
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.model = QFileSystemModel()
        self.model.setRootPath("C:\\")
        self.tree = QTreeView()
        self.tree.setModel(self.model)

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())