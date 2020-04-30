import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
    QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QPushButton)

class Example(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 150, 300, 450)
        self.loginscreen()       

    def loginscreen(self):    
        mainlbl = QLabel(u'<H1>Auth</H1>', self)
        mainlbl.move(120,10)

        loginlbl = QLabel(u'<H3>Login</H3>', self)
        loginlbl.move(30, 100)

        passwordlbl = QLabel(u'<H3>Password</H3>', self)
        passwordlbl.move(30, 125)

        login_edit = QLineEdit(self)
        login_edit.move(150, 105)
        login_edit.resize(100,20)

        password_edit = QLineEdit(self)
        password_edit.move(150,130)
        password_edit.resize(100,20)
        password_edit.setEchoMode(QLineEdit.Password)

        login_button = QPushButton('Login', self)
        login_button.move(100, 300)
        self.show()
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
