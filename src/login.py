


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()
        self.setup_ui()

    def setup_ui(self):
        # Configurar el campo de contraseña para mostrar asteriscos
        self.ui.lineEdit_contrasea.setEchoMode(QtWidgets.QLineEdit.Password)

    def setup_connections(self):
        self.ui.Button_ingresar.clicked.connect(self.check_login)

    def check_login(self):
        username = self.ui.lineEdit_usuario.text()
        password = self.ui.lineEdit_contrasea.text()

        if username == "admin" and password == "admin":
            self.hide()
            from opciones import OpcionesWindow
            self.opciones_window = OpcionesWindow()
            self.opciones_window.show()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def clear_fields(self):
        self.ui.lineEdit_usuario.clear()
        self.ui.lineEdit_contrasea.clear()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 443)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(76, 76, 230, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 641))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fdc32721859471281b27dc52fed6c7ee.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.WELCOME = QtWidgets.QLabel(self.centralwidget)
        self.WELCOME.setGeometry(QtCore.QRect(90, 30, 401, 101))
        self.WELCOME.setStyleSheet("font: 75 28pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.WELCOME.setScaledContents(True)
        self.WELCOME.setObjectName("WELCOME")
        self.lb_fondo = QtWidgets.QLabel(self.centralwidget)
        self.lb_fondo.setGeometry(QtCore.QRect(250, 160, 61, 51))
        self.lb_fondo.setStyleSheet("\n"
"\n"
"border-radius: 30px; /* Cambia 10px por el radio deseado */")
        self.lb_fondo.setText("")
        self.lb_fondo.setPixmap(QtGui.QPixmap("102649.png"))
        self.lb_fondo.setScaledContents(True)
        self.lb_fondo.setObjectName("lb_fondo")
        self.lb_fondo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_fondo_2.setGeometry(QtCore.QRect(100, 240, 371, 121))
        self.lb_fondo_2.setStyleSheet("\n"
"\n"
"border-radius: 30px; /* Cambia 10px por el radio deseado */")
        self.lb_fondo_2.setText("")
        self.lb_fondo_2.setPixmap(QtGui.QPixmap("src/1233706_6b7ea.jpg"))
        self.lb_fondo_2.setScaledContents(False)
        self.lb_fondo_2.setObjectName("lb_fondo_2")
        self.lbl_iniceses = QtWidgets.QLabel(self.centralwidget)
        self.lbl_iniceses.setGeometry(QtCore.QRect(200, 210, 151, 21))
        self.lbl_iniceses.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lbl_iniceses.setObjectName("lbl_iniceses")
        self.lbl_contrasea = QtWidgets.QLabel(self.centralwidget)
        self.lbl_contrasea.setGeometry(QtCore.QRect(120, 310, 111, 21))
        self.lbl_contrasea.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lbl_contrasea.setObjectName("lbl_contrasea")
        self.lbl_usuario = QtWidgets.QLabel(self.centralwidget)
        self.lbl_usuario.setGeometry(QtCore.QRect(150, 260, 91, 21))
        self.lbl_usuario.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lbl_usuario.setObjectName("lbl_usuario")
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setGeometry(QtCore.QRect(240, 250, 191, 41))
        self.lineEdit_usuario.setStyleSheet("background-color: rgb(176, 176, 176);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.lineEdit_contrasea = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_contrasea.setGeometry(QtCore.QRect(240, 300, 191, 41))
        self.lineEdit_contrasea.setStyleSheet("background-color: rgb(176, 176, 176);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.lineEdit_contrasea.setObjectName("lineEdit_contrasea")
        self.Button_ingresar = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ingresar.setGeometry(QtCore.QRect(200, 370, 151, 51))
        self.Button_ingresar.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"background-color: rgb(60, 180, 180);")
        self.Button_ingresar.setObjectName("Button_ingresar")
        self.WELCOME_2 = QtWidgets.QLabel(self.centralwidget)
        self.WELCOME_2.setGeometry(QtCore.QRect(150, 90, 261, 101))
        self.WELCOME_2.setStyleSheet("font: 75 28pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.WELCOME_2.setScaledContents(True)
        self.WELCOME_2.setObjectName("WELCOME_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.WELCOME.setText(_translate("MainWindow", "HELLO & WELCOME"))
        self.lbl_iniceses.setText(_translate("MainWindow", "INICIE SESION"))
        self.lbl_contrasea.setText(_translate("MainWindow", "Contraseña:"))
        self.lbl_usuario.setText(_translate("MainWindow", "Usuario:"))
        self.Button_ingresar.setText(_translate("MainWindow", "INGRESAR"))
        self.WELCOME_2.setText(_translate("MainWindow", "PASSKEEPER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
