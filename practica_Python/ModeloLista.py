import sys
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage

doc = QImage('documento-png.png')
fol = QImage('hoja-de-calculo.png')

class ModeloHojas (QAbstractListModel):
    def __init__(self, hojas = None):
        super().__init__()
        self.hojas = hojas or []

    def data(self, indice,rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            texto , _ = self.hojas [indice.row()]
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            _,tipo = self.hojas [indice.row()]
            if tipo == "F":
                return fol
            if tipo == "D":
                return doc

    def rowCount(self,indice):
        return len(self.hojas)