import sys
from logging import makeLogRecord
from ModeloTabla import ModeloTabla

from pkg_resources import non_empty_lines

from practica_Python import CajaQTColor

from PyQt6.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QWidget, QHBoxLayout, QGridLayout, QLineEdit, \
    QComboBox, QTextEdit, QRadioButton, QButtonGroup, QTableView, QTabWidget, QListView


class Actividad6QT (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actividad 6 Interfaz QT")

        # Lista de nombres
        self.nombres = [
            "Ana", "Bruno", "Carlos", "Daniel", "Elena", "Fernando", "Gabriela",
            "Hugo", "Irene", "Javier", "Laura", "Mario", "Natalia", "Oscar",
            "Paula", "Quintín", "Raquel", "Sofía", "Tomás", "Uxía"
        ]

        self.lista = QListView()




        self.setCentralWidget(container)
        self.show()


if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    ventana = Actividad6QT()
    aplication.exec()