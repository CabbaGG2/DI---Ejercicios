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

        self.ventana.show()

    def run (self):
        sys.exit (self.aplicacion.exec())

if __name__ == "__main__":
    app = MiAplicacion()
    app.run()