from PyQt6 import QtGui
from PyQt6.QtCore import QAbstractTableModel, Qt

class ModeloTabla (QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla

    #El metodo data es para representar el rol, y tipo de dato y desde donde comenzar segun el indice
    def data (self,indice,rol):
        #Display Role sirve para imprimir texto en la fila/columna de la tabla
        if rol == Qt.ItemDataRole.DisplayRole:
            #si la columna 3 tiene algun texto o dato tipo texto y la fila es distinta a la cero devuelve una cadena vacia
            if indice.column() == 3 and indice.row() != 0:
                return ""
            else:
                return self.tabla [indice.row()][indice.column()]
        #muestra en azul los datos de los hombres y rosados las mujeres(color de fondo)
        if rol == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[indice.row()][2] == "M":
                return QtGui.QColor('lightblue')
            elif self.tabla[indice.row()][2] == "F":
                return QtGui.QColor('pink')
        #MNuestra en rojo el texto de la gente que ha fallecido
        if rol == Qt.ItemDataRole.ForegroundRole:
            if self.tabla[indice.row()][3] == True:
                if (indice.column() == 3):
                    return QtGui.QColor('green')
        #
        if rol == Qt.ItemDataRole.DecorationRole:
            #isinstance sirve para reconocer el tipo de datos, si es booleano usa una imagen, sino la otra
            if isinstance(self.tabla[indice.row()][indice.column()], bool):
                if self.tabla[indice.row()][indice.column()]:
                    return QtGui.QIcon('tic16x16.jpg')
                else:
                    return QtGui.QIcon('equis16x216.jpg')

    #El metodo rowCount cuanta las cantidad de columnas del modelo cuando es llamada en una interfaz (la vista sabe cuantas filas va a representar)
    def rowCount(self, indice):
        return len (self.tabla)

    # regresar las columnas del modelo
    def columnCount(self, indice):
        return len(self.tabla[0]) if len(self.tabla) != 0 else 0

