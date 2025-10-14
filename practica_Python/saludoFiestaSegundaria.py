import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)

from practica_Python import saludoQT

class FiestaSegundaria (QMainWindow):
    def __init__(self, ventanaPadre):
        super().__init__()
        self.ventanaPadre = ventanaPadre
        self.setWindowTitle("Fiesta Segundaria!")
        self.setMinimumSize(400,300)

        #La cajaV es un contenedor que ocupa toda la ventana del programa
        cajaV = QVBoxLayout()

        # las etiquetas si no van a cambiar dinamicamente se puedes declarar como una constante como la cajaV
        self.lblEtiqueta = QLabel("Segunda ventana")
        fuente = self.lblEtiqueta.font()
        fuente.setPointSize(30)
        self.lblEtiqueta.setFont(fuente)
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.lblEtiqueta.setText("Segunda ventana")

        #
        self.txtSaludo = QLineEdit()
        self.txtSaludo.setPlaceholderText("Escribe un nombre")
        self.txtSaludo.returnPressed.connect(self.on_btnSaludo_clicked)

        #el checklist es un boton que ustiliza toogled para hacer cambios entes seleccionado y deselenccionado
        btnSaludo = QPushButton("Saludo")
        btnSaludo.clicked.connect(self.on_btnSaludo_clicked)

        # Boton que oculta ventanas entre ellas
        btnMostrarFiestaSegundaria = QPushButton("Regresar a principal")
        btnMostrarFiestaSegundaria.clicked.connect(self.cambiarFiesta)

        #Se añaden los 3 controles a la cajaV
        cajaV.addWidget(self.lblEtiqueta)
        cajaV.addWidget(self.txtSaludo)
        cajaV.addWidget(btnSaludo)
        cajaV.addWidget(btnMostrarFiestaSegundaria)

        #Hay que adaptar los widget a layout o viceversa
        container = QWidget()
        container.setLayout(cajaV)

        self.setCentralWidget(container)
        self.show()
        #self.hide()

    def on_btnSaludo_clicked (self):
        nombre = self.txtSaludo.text()
        if nombre.strip() == "":
            self.lblEtiqueta.setText("Por favor introduce un nombre")
            self.txtSaludo.setText("")
            return

        self.lblEtiqueta.setText("!Hola " + nombre + "!")
        self.txtSaludo.setText("")

    def cambiarFiesta (self):
        if self.ventanaPadre is not None:
            self.ventanaPadre.show()
            self.ventanaPadre.saludoFiestaSegundaria = None
            self.hide()
            self.destroy()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiesta = FiestaSegundaria(None)
    app.exec()