
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from database import Database




class AgregarWindow(QtWidgets.QMainWindow):
    def __init__(self, password_id=None, password_data=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.password_id = password_id
        self.setup_connections()
        if password_data:
            self.fill_data(password_data)

    def setup_connections(self):
        self.ui.Button_ingresar.clicked.connect(self.add_or_update_password)

    def fill_data(self, data):
        self.ui.lineEdit_usuario.setText(data['usuario'])
        self.ui.lineEdit_contrasea.setText(data['contrasena'])
        self.ui.lineEdit_servicio.setText(data['servicio'])

    def add_or_update_password(self):
        usuario = self.ui.lineEdit_usuario.text()
        contrasena = self.ui.lineEdit_contrasea.text()
        servicio = self.ui.lineEdit_servicio.text()

        if usuario and contrasena and servicio:
            if self.password_id is None:
                # Operación de agregar
                if self.db.add_password(usuario, contrasena, servicio):
                    QMessageBox.information(self, "Éxito", "Contraseña agregada correctamente")
                    self.back_to_options()
                else:
                    QMessageBox.warning(self, "Error", "Error al guardar la contraseña")
            else:
                # Operación de actualización
                if self.db.update_password(self.password_id, usuario, contrasena, servicio):
                    QMessageBox.information(self, "Éxito", "Contraseña actualizada correctamente")
                    self.back_to_options()
                else:
                    QMessageBox.warning(self, "Error", "Error al actualizar la contraseña")
        else:
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos")

    def back_to_options(self):
        self.hide()
        from opciones import OpcionesWindow
        self.opciones_window = OpcionesWindow()
        self.opciones_window.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 381)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(76, 76, 230, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 641))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1c61dc199e4a6354f8cf14540d2b85ca.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.WELCOME = QtWidgets.QLabel(self.centralwidget)
        self.WELCOME.setGeometry(QtCore.QRect(100, 10, 501, 101))
        self.WELCOME.setStyleSheet("font: 75 28pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.WELCOME.setScaledContents(True)
        self.WELCOME.setObjectName("WELCOME")
        self.lb_fondo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_fondo_2.setGeometry(QtCore.QRect(50, 120, 401, 171))
        self.lb_fondo_2.setStyleSheet("\n"
"\n"
"border-radius: 30px; /* Cambia 10px por el radio deseado */")
        self.lb_fondo_2.setText("")
        self.lb_fondo_2.setPixmap(QtGui.QPixmap("1233706_6b7ea.jpg"))
        self.lb_fondo_2.setScaledContents(False)
        self.lb_fondo_2.setObjectName("lb_fondo_2")
        self.lbl_contrasea = QtWidgets.QLabel(self.centralwidget)
        self.lbl_contrasea.setGeometry(QtCore.QRect(60, 190, 111, 21))
        self.lbl_contrasea.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lbl_contrasea.setObjectName("lbl_contrasea")
        self.lbl_usuario = QtWidgets.QLabel(self.centralwidget)
        self.lbl_usuario.setGeometry(QtCore.QRect(80, 140, 91, 21))
        self.lbl_usuario.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lbl_usuario.setObjectName("lbl_usuario")
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setGeometry(QtCore.QRect(170, 130, 191, 41))
        self.lineEdit_usuario.setStyleSheet("background-color: rgb(176, 176, 176);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.lineEdit_contrasea = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_contrasea.setGeometry(QtCore.QRect(170, 180, 191, 41))
        self.lineEdit_contrasea.setStyleSheet("background-color: rgb(176, 176, 176);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.lineEdit_contrasea.setObjectName("lineEdit_contrasea")
        self.Button_ingresar = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ingresar.setGeometry(QtCore.QRect(300, 310, 151, 51))
        self.Button_ingresar.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"background-color: rgb(60, 180, 180);")
        self.Button_ingresar.setObjectName("Button_ingresar")
        self.lbl_servicio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_servicio.setGeometry(QtCore.QRect(70, 240, 81, 21))
        self.lbl_servicio.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lbl_servicio.setObjectName("lbl_servicio")
        self.lineEdit_servicio = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_servicio.setGeometry(QtCore.QRect(170, 230, 191, 41))
        self.lineEdit_servicio.setStyleSheet("background-color: rgb(176, 176, 176);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.lineEdit_servicio.setObjectName("lineEdit_servicio")
        self.lb_fondo_3 = QtWidgets.QLabel(self.centralwidget)
        self.lb_fondo_3.setGeometry(QtCore.QRect(370, 130, 41, 31))
        self.lb_fondo_3.setStyleSheet("\n"
"\n"
"border-radius: 30px; /* Cambia 10px por el radio deseado */")
        self.lb_fondo_3.setText("")
        self.lb_fondo_3.setPixmap(QtGui.QPixmap("src/16363.png"))
        self.lb_fondo_3.setScaledContents(True)
        self.lb_fondo_3.setObjectName("lb_fondo_3")
        self.lb_fondo_4 = QtWidgets.QLabel(self.centralwidget)
        self.lb_fondo_4.setGeometry(QtCore.QRect(360, 170, 61, 41))
        self.lb_fondo_4.setStyleSheet("\n"
"\n"
"border-radius: 30px; /* Cambia 10px por el radio deseado */")
        self.lb_fondo_4.setText("")
        self.lb_fondo_4.setPixmap(QtGui.QPixmap("src/102643.png"))
        self.lb_fondo_4.setScaledContents(True)
        self.lb_fondo_4.setObjectName("lb_fondo_4")
        self.lb_fondo_5 = QtWidgets.QLabel(self.centralwidget)
        self.lb_fondo_5.setGeometry(QtCore.QRect(470, 120, 191, 181))
        self.lb_fondo_5.setStyleSheet("\n"
"\n"
"border-radius: 30px; /* Cambia 10px por el radio deseado */")
        self.lb_fondo_5.setText("")
        self.lb_fondo_5.setPixmap(QtGui.QPixmap("5065361.png"))
        self.lb_fondo_5.setScaledContents(True)
        self.lb_fondo_5.setObjectName("lb_fondo_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.WELCOME.setText(_translate("MainWindow", "AGREGAR CONTRASEÑA"))
        self.lbl_contrasea.setText(_translate("MainWindow", "Contraseña:"))
        self.lbl_usuario.setText(_translate("MainWindow", "Usuario:"))
        self.Button_ingresar.setText(_translate("MainWindow", "AGREGAR"))
        self.lbl_servicio.setText(_translate("MainWindow", "Servicio:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
