#MAIN
import sys
from PyQt5 import QtWidgets
from src.login import LoginWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())