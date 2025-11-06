import sys
from practica_Python import CajaQTColor, ModeloLista

from PyQt6.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QWidget, QHBoxLayout, QGridLayout, QLabel, \
    QPushButton, QListWidget, QListView


class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo 1 Ventana QT")

        malla = QGridLayout()

        listasHojas = [["Hoja1","F"],["Documento 2","D"],["Hoja3","F"],["Hoja4","F"],["Documento 5","D"]]
        listasHojasOcultas = []

        controlInerte = QWidget()
        controlInerte.setMinimumSize(1,20)

        self.listasVisibles = QListView()
        self.listasOcultas = QListView()
        self.modeloListasVisibles = ModeloLista.ModeloHojas(listasHojas)
        self.modeloListasOcultas = ModeloLista.ModeloHojas()

        self.listasVisibles.setModel(self.modeloListasVisibles)

        self.listasOcultas.setModel(self.modeloListasOcultas)

        btnMostrar = QPushButton("Grabar>>>")
        btnMostrar.clicked.connect(self.on_btnMostrar_clicked)

        btnOcultar = QPushButton("<<< Mover")
        btnOcultar.clicked.connect(self.on_btnOcultar_clicked)


        malla.addWidget(QLabel("Hoja nueva"))
        malla.addWidget(self.listasVisibles,1,0,5,1)
        malla.addWidget(btnMostrar,1,1,1,1)
        malla.addWidget(btnOcultar,3,1,1,1)
        malla.addWidget(QLabel("Hojas Ocultas"),0,2,1,1)
        malla.addWidget(self.listasOcultas,1,2,5,1)
        malla.addWidget(QPushButton("Cerrar"),8,2,1,1)
        malla.addWidget(controlInerte,7,2,1,1)

        container = QWidget()
        container.setLayout(malla)
        self.setCentralWidget(container)

        self.show()

    def on_btnOcultar_clicked(self):
        indices = self.listasOcultas.selectedIndexes()
        if indices:
            self.modeloListasVisibles.hojas.append(self.modeloListasOcultas.hojas[ indices[0].row()])
            del self.modeloListasOcultas.hojas[indices[0].row()]
            self.modeloListasVisibles.layoutChanged.emit()
            self.modeloListasOcultas.layoutChanged.emit()
            self.listasOcultas.clearSelection()

    def on_btnMostrar_clicked(self):
        indices = self.listasVisibles.selectedIndexes()
        if indices:
            self.modeloListasOcultas.hojas.append(self.modeloListasVisibles.hojas[ indices[0].row()])
            del self.modeloListasVisibles.hojas[indices[0].row()]
            self.modeloListasOcultas.layoutChanged.emit()
            self.modeloListasVisibles.layoutChanged.emit()
            self.listasVisibles.clearSelection()

if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    ventana = Ventana()
    aplication.exec()