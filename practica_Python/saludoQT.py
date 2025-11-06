import sys
from enum import nonmember
from unicodedata import category

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout)
from PyQt6.QtWidgets import QLineEdit
from PyQt6.uic.exceptions import NoSuchWidgetError

from practica_Python import saludoFiestaSegundaria

class NuestraPrimeraFiesta (QMainWindow):
    def __init__(self):
        super().__init__()
        self.saludoFiestaSegundaria = None
        self.nombreOculto = ''

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
        #Para mandar la señal pusando Enter
        self.txtSaludo.returnPressed.connect(self.on_btnSaludo_clicked)
        #Cambia de mayuscula a minuscula cuando hay cambio de texto y reconozca si es mayuscula o miniuscula y lo cambia automaticamente.
        self.txtSaludo.textChanged.connect(self.on_btnSaludo_textChanged)

        #el checklist es un boton que ustiliza toogled para hacer cambios entes seleccionado y deselenccionado
        btnSaludo = QPushButton("Saludo")
        btnSaludo.clicked.connect(self.on_btnSaludo_clicked)

        #Boton que oculta ventanas entre ellas
        btnMostrarFiestaSegundaria = QPushButton("Otra Ventana!")
        btnMostrarFiestaSegundaria.clicked.connect(self.cambiarFiesta)

        #Boton que se puede comprobar su comportamiento si es seleccionado o no
        """ Cambiamos el btnMayuscula por un check que se llamara chkMayuscula
        self.btnMayusculas = QPushButton("Mayusculas")
        self.btnMayusculas.setCheckable(True)
        self.btnMayusculas.setChecked(True)
        self.btnMayusculas.toggled.connect(self.on_btnMayuscula_toggled)
        self.mayusculas = True
        """
        #Creamos la caja horizontal en donde insertaremos dos checkbox
        cajaH = QHBoxLayout()

        #checkbox que revisa las mayusculas
        self.chkMayuscula = QCheckBox("Mayusculas")
        self.mayusculas = True
        self.chkMayuscula.setChecked(True)
        self.chkMayuscula.toggled.connect(self.on_chkMayuscula_toggled)

        #checkbox que oculta el texto
        self.chkOculto = QCheckBox("Ocultar texto")
        self.chkOculto.toggled.connect(self.on_chkOculto_toggled)

        self.chkOculto2 = QCheckBox("Oculta tenxto 2")

        #Agregamos los checkbox en la caja horizontal
        cajaH.addWidget(self.chkMayuscula)
        cajaH.addWidget(self.chkOculto)

        #Se añaden los 3 controles a la cajaV
        cajaV.addWidget(self.lblEtiqueta)
        cajaV.addWidget(self.txtSaludo)
        cajaV.addWidget(btnSaludo)
        cajaV.addWidget(btnMostrarFiestaSegundaria)
        #cajaV.addWidget(self.chkMayuscula)
        cajaV.addLayout(cajaH)
        cajaV.addWidget(self.chkOculto2)

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
        self.on_chkMayuscula_toggled()
        #self.on_btnMayuscula_toggled()

    def on_btnMayuscula_toggled(self):
        if self.btnMayusculas.isChecked():
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper())
            self.mayusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower())
            self.mayusculas = False

    def on_chkMayuscula_toggled(self):
        if self.chkMayuscula.isChecked():
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper())
            self.txtSaludo.setText(self.txtSaludo.text().upper())
            self.mayusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower())
            self.txtSaludo.setText(self.txtSaludo.text().lower())
            self.mayusculas = False

    def on_btnSaludo_textChanged(self):
        if self.mayusculas:
            self.txtSaludo.setText(self.txtSaludo.text().upper())
        else:
            self.txtSaludo.setText(self.txtSaludo.text().lower())


    def on_chkOculto_toggled(self):
        if self.chkOculto.isChecked():
            self.txtSaludo.setEchoMode(QLineEdit.EchoMode.Password)

        else:
            self.txtSaludo.setEchoMode(QLineEdit.EchoMode.Normal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiesta = NuestraPrimeraFiesta()
    app.exec()