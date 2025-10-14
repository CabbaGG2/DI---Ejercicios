import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)
from PyQt6.uic.exceptions import NoSuchWidgetError

from practica_Python import saludoFiestaSegundaria

class NuestraPrimeraFiesta (QMainWindow):
    def __init__(self):
        super().__init__()
        self.saludoFiestaSegundaria = None
        self.setWindowTitle("Fiesta Principal!")
        self.setMinimumSize(400,300)

        #La cajaV es un contenedor que ocupa toda la ventana del programa
        cajaV = QVBoxLayout()

        # las etiquetas si no van a cambiar dinamicamente se puedes declarar como una constante como la cajaV
        self.lblEtiqueta = QLabel("Hola a todos amixes")
        fuente = self.lblEtiqueta.font()
        fuente.setPointSize(30)
        self.lblEtiqueta.setFont(fuente)
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.lblEtiqueta.setText("Hola a todos y todas!")

        #Una caja de texto que se puede llenar
        self.txtSaludo = QLineEdit()
        self.txtSaludo.setPlaceholderText("Escribe un nombre")
        self.txtSaludo.returnPressed.connect(self.on_btnSaludo_clicked)

        #el checklist es un boton que ustiliza toogled para hacer cambios entes seleccionado y deselenccionado
        btnSaludo = QPushButton("Saludo")
        btnSaludo.clicked.connect(self.on_btnSaludo_clicked)

        #Boton que oculta ventanas entre ellas
        btnMostrarFiestaSegundaria = QPushButton("Otra Ventana!")
        btnMostrarFiestaSegundaria.clicked.connect(self.cambiarFiesta)

        #Boton que se puede comprobar su comportamiento si es seleccionado o no
        btnMayusculas = QPushButton("Mayusculas")
        btnMayusculas.setCheckable(True)
        btnMayusculas.toggled.connect(self.on_btnMayuscula_toggled)
        self.mayusculas = True


        #Se añaden los 3 controles a la cajaV
        cajaV.addWidget(self.lblEtiqueta)
        cajaV.addWidget(self.txtSaludo)
        cajaV.addWidget(btnSaludo)
        cajaV.addWidget(btnMostrarFiestaSegundaria)

        #Hay que adaptar los widget a layour o viceversa
        container = QWidget()
        container.setLayout(cajaV)

        self.setCentralWidget(container)
        self.show()
        #self.hide()

    def cambiarFiesta (self):
        self.hide()
        if self.saludoFiestaSegundaria is None:
            self.saludoFiestaSegundaria = saludoFiestaSegundaria.FiestaSegundaria(self)
        self.saludoFiestaSegundaria.show()

    def on_btnSaludo_clicked (self):
        nombre = self.txtSaludo.text()
        if nombre.strip() == "":
            self.lblEtiqueta.setText("Por favor introduce un nombre")
            self.txtSaludo.setText("")
            return

        self.lblEtiqueta.setText("!Hola " + nombre + "!")
        self.txtSaludo.setText("")

    def on_btnMayuscula_toggled(self):
        if self.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiesta = NuestraPrimeraFiesta()
    app.exec()