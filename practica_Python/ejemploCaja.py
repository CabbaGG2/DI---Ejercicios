import sys
from practica_Python import CajaQTColor

from PyQt6.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QWidget, QHBoxLayout


class EjemploCaja (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo con cajas")

        cajaRojo = CajaQTColor.CajaColor("red")
        cajaAmarilla = CajaQTColor.CajaColor("yellow")
        cajaRosado = CajaQTColor.CajaColor("pink")


        cajaCompleta = QHBoxLayout()
        cajaIzquierda = QVBoxLayout()


        cajaIzquierda.addWidget(cajaRojo)
        cajaIzquierda.addWidget(cajaAmarilla)
        cajaIzquierda.addWidget(cajaRosado)

        cajaCompleta.addLayout(cajaIzquierda)

        cajaCompleta.addWidget(CajaQTColor.CajaColor("yellow"))

        cajaDerecha = QVBoxLayout()
        cajaDerecha.addWidget(CajaQTColor.CajaColor("pink"))
        cajaDerecha.addWidget(CajaQTColor.CajaColor("grey"))

        cajaCompleta.addLayout(cajaDerecha)


        container = QWidget()
        container.setLayout(cajaCompleta)

        self.setCentralWidget(container)
        self.show()


if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    ventana = EjemploCaja()
    aplication.exec()