import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.uic import loadUi

class MiAplicacion:
    def __init__(self):
        self.aplicacion = QApplication(sys.argv)

        #Pasamos la ruta del form.ui que creamos en QTCreator
        self.ventana = loadUi("form.ui")

        #la ventana esta referenciada entonces para obtener los items de la ventana hacemos:
        self.txtApellidos = self.ventana.txtApellidos
        self.btnEngadir = self.ventana.btnEngadir
        self.cmbNumeroCliente = self.ventana.cmbNumeroCliente

        #agregamos eventos a los botones
        self.btnEngadir.pressed.connect(self.on_btnEngadir_pressed)

        #El combo se le agrega un modelo con insertItems
        self.cmbNumeroCliente.insertItems(0,['1','2','3','4','5'])

        self.ventana.show()

    #metodos
    def on_btnEngadir_pressed(self):
        numCliente = self.cmbNumeroCliente.currentText()
        self.txtApellidos.setText("El numero de cliente es: " + numCliente)

    def run (self):
        sys.exit (self.aplicacion.exec())

if __name__ == "__main__":
    app = MiAplicacion()
    app.run()