from Affichage_Principal import *
from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout,QDial,QGridLayout,QLineEdit


class fenetre(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.wid=Widget_Matplotlib('V_HULL.STL')
        self.layout=QHBoxLayout()
        self.box=QVBoxLayout()
        self.layout.addWidget(self.box,self.wid)
        self.setLayout(self.layout)
if __name__ == '__main__' :
    app=QApplication([])
    window=fenetre()
    window.show()
    app.exec_()

