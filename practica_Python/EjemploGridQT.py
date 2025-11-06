import sys
from practica_Python import CajaQTColor

from PyQt6.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QWidget, QHBoxLayout, QGridLayout


class EjemploCaja (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo con QGridLayout")

        malla = QGridLayout()

        malla.addWidget(CajaQTColor.CajaColor("red"))
        malla.addWidget(CajaQTColor.CajaColor("blue"),0,1,1,2)
        malla.addWidget(CajaQTColor.CajaColor("green"),1,0,2,1)
        malla.addWidget(CajaQTColor.CajaColor("pink"),1,1,1,2)
        malla.addWidget(CajaQTColor.CajaColor("orange"),2,1,1,1)
        malla.addWidget(CajaQTColor.CajaColor("yellow"),2,2,1,1)

        container = QWidget()
        container.setLayout(malla)
        self.setCentralWidget(container)

        self.show()

if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    ventana = EjemploCaja()
    aplication.exec()