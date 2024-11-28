import sys
from PyQt5.QtWidgets import QApplication
from calculadora import Calculadora

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    qt.exec_()