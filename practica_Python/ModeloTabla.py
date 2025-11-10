from PyQt6 import QtGui
from PyQt6.QtCore import QAbstractTableModel, Qt

class ModeloTabla (QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla

    #El metodo data es para representar el rol, y tipo de dato y desde donde comenzar segun el indice
    def data (self,indice,rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            return self.tabla [indice.row()][indice.column()]
        #muestra en azul los datos de los hombres y rosados las mujeres
        if rol == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[indice.row()][2] == "M":
                return QtGui.QColor('lightblue')
            elif self.tabla[indice.row()][2] == "F":
                return QtGui.QColor('pink')
        #MNuestra en rojo el texto de la gente que ha fallecido
        if rol == Qt.ItemDataRole.ForegroundRole:
            if self.tabla[indice.row()][3] == True:
                if (indice.column() == 3):
                    return QtGui.QColor('red')

    #El metodo rowCount cuanta las cantidad de columnas del modelo cuando es llamada en una interfaz (la vista sabe cuantas filas va a representar)
    def rowCount(self, indice):
        return len (self.tabla)

    # regresar las columnas del modelo
    def columnCount(self, indice):
        return len(self.tabla[0]) if len(self.tabla) != 0 else 0

