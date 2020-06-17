from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox,QBoxLayout,QDial,QGridLayout,QLineEdit,QToolBar

class Message(QWidget) :
    def __init__(self,message):








if __name__ == '__main__' :
    app=QApplication([])
    window=Message('message')
    window.show()
    app.exec_()
