

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from database import Database


class ListaWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.setup_connections()
        self.update_password_table()

    def setup_connections(self):
        self.ui.Button_editar.clicked.connect(self.edit_password)
        self.ui.Button_eliminar.clicked.connect(self.delete_password)
        self.ui.Button_volver.clicked.connect(self.back_to_options)

    def update_password_table(self):
        self.ui.tableWidget.setRowCount(0)  # Limpiar la tabla
        passwords = self.db.get_all_passwords()  # Obtener contraseñas de la base de datos
        for password in passwords:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)

            # Ajusta el rango para empezar desde la segunda columna de datos
            for col, value in enumerate(password[1:]):  # Omite el ID
                self.ui.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))

    def edit_password(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            try:
                password_id = int(self.ui.tableWidget.item(current_row, 0).text())
                password_data = {
                    'usuario': self.ui.tableWidget.item(current_row, 1).text(),
                    'contrasena': self.ui.tableWidget.item(current_row, 2).text(),
                    'servicio': self.ui.tableWidget.item(current_row, 3).text()
                }

                from ventana_agregarcontraseña import AgregarWindow
                self.hide()
                self.agregar_window = AgregarWindow(password_id, password_data)
                self.agregar_window.show()
            except Exception as e:
                print(f"Error al editar: {e}")
                QMessageBox.warning(self, "Error", "Error al cargar los datos para editar")
        else:
            QMessageBox.warning(self, "Error", "Por favor seleccione una contraseña para editar")

    def delete_password(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            reply = QMessageBox.question(self, "Confirmar",
                                         "¿Está seguro de eliminar esta contraseña?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                password_id = int(self.ui.tableWidget.item(current_row, 0).text())
                if self.db.delete_password(password_id):
                    self.update_password_table()
                    QMessageBox.information(self, "Éxito", "Contraseña eliminada correctamente")
                else:
                    QMessageBox.warning(self, "Error", "Error al eliminar la contraseña")
        else:
            QMessageBox.warning(self, "Error", "Por favor seleccione una contraseña para eliminar")

    def back_to_options(self):
        self.hide()
        from opciones import OpcionesWindow
        self.opciones_window = OpcionesWindow()
        self.opciones_window.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 343)
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
        self.lbl_listacontra = QtWidgets.QLabel(self.centralwidget)
        self.lbl_listacontra.setGeometry(QtCore.QRect(110, 0, 501, 101))
        self.lbl_listacontra.setStyleSheet("font: 75 28pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.lbl_listacontra.setScaledContents(True)
        self.lbl_listacontra.setObjectName("lbl_listacontra")
        self.Button_editar = QtWidgets.QPushButton(self.centralwidget)
        self.Button_editar.setGeometry(QtCore.QRect(110, 260, 151, 51))
        self.Button_editar.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"background-color: rgb(60, 180, 180);")
        self.Button_editar.setObjectName("Button_editar")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 90, 321, 121))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.Button_eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.Button_eliminar.setGeometry(QtCore.QRect(290, 260, 151, 51))
        self.Button_eliminar.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"background-color: rgb(255, 0, 0);")
        self.Button_eliminar.setObjectName("Button_eliminar")
        self.Button_volver = QtWidgets.QPushButton(self.centralwidget)
        self.Button_volver.setGeometry(QtCore.QRect(470, 260, 151, 51))
        self.Button_volver.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"background-color: rgb(66, 198, 0);")
        self.Button_volver.setObjectName("Button_volver")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 80, 171, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("9710187.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_listacontra.setText(_translate("MainWindow", "LISTA DE CONTRASEÑAS"))
        self.Button_editar.setText(_translate("MainWindow", "EDITAR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "USUARIO"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CONTRASEÑA"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SERVICIO"))
        self.Button_eliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.Button_volver.setText(_translate("MainWindow", "VOLVER "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
