import sys
from logging import makeLogRecord
from mimetypes import inited

from ModeloTabla import ModeloTabla

from pkg_resources import non_empty_lines

from practica_Python import CajaQTColor

from PyQt6.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QWidget, QHBoxLayout, QGridLayout, QLineEdit, \
    QComboBox, QTextEdit, QRadioButton, QButtonGroup, QTableView, QTabWidget


class EjemploInterfazQT (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo interfaz Compleja QT")

        #creamos una lista con nombres de personas
        self.nombre_dni = [["Ana", "Pepe", "Juan"],["11111R","22222J","33333H"]]

        self.datos = [["Nombre","DNI","Genero","Fallecido"],
                      ["Ana","1514321K","F",False],
                      ["Pepe","65841Y","M",False],
                      ["Toño","354321Y","M",True]]

        malla = QGridLayout()
        #Esta tenia que ser la caja vertical 1 pero me dio flojera cambiar las referencias asi que se quda como la 2
        cajaV2 = QVBoxLayout()

        malla.addLayout(cajaV2,0,0,1,1)

        #Radio button
        #QRadioButton(nombre del boton, referencia del padre lo que hace que sean versiones distintas)
        self.rdButton1 = QRadioButton("Boton1")
        #Cuando se seleciona llama la funcion
        self.rdButton1.toggled.connect(self.on_rdButton1_toogled)
        rdButton2 = QRadioButton("Boton2")
        rdButton3 = QRadioButton("Boton3")
        rdButton4 = QRadioButton("Boton4")

        #Creamos dos grupos para agrupar los botones, se tienen que referenciar a ellos mismos para funcionar.
        grupo1 = QButtonGroup(self)
        grupo2 = QButtonGroup(self)
        grupo1.addButton(self.rdButton1)
        grupo1.addButton(rdButton2)
        grupo1.setExclusive(True)
        grupo2.addButton(rdButton3)
        grupo2.addButton(rdButton4)
        grupo2.setExclusive(True)

        cajaV2.addWidget(self.rdButton1)
        cajaV2.addWidget(rdButton2)
        cajaV2.addWidget(rdButton3)
        cajaV2.addWidget(rdButton4)

        #QTabWidget sirve para hacer pestañas
        clasificador = QTabWidget()
        #Sirve para colocar la orientación -> con tabpositicion.north ponemos la orientación arriba
        clasificador.setTabPosition(QTabWidget.TabPosition.North)

        malla.addWidget(clasificador, 0, 1, 1, 1)

        #Tablas = se crea la tablas con QTableView
        self.tTabla = QTableView()
        self.modelo = ModeloTabla(self.datos)
        self.tTabla.setModel(self.modelo)

        #setSelectionMode es para elegir como quiero que se comporte la tabla en el programa, podemos elekgir seleccion unica, no selecion o multiple
        self.tTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        #Con la selección podemos decidir si eso sirve para algun evento o no, ya sea con la accion de seleccionar o con otro evento que haga algo con la seleccion
        self.seleccion = self.tTabla.selectionModel()
        self.seleccion.selectionChanged.connect(self.on_tTabla_selectionChanged)

        # addTab añade una nueva  pestaña
        clasificador.addTab(self.tTabla, "Tabla")
        txe2CuadroTexto = QTextEdit()
        clasificador.addTab(txe2CuadroTexto, "Cuadro de texto")

        cajaV = QVBoxLayout()

        txtCuadro1 = QLineEdit()
        txtCuadro2 = QLineEdit()

        #Así se declara un comboBox en QT
        self.cmbComboBox = QComboBox()


        cajaV.addWidget(txtCuadro1)
        cajaV.addWidget(txtCuadro2)

        #esto es un combobox
        cajaV.addWidget(self.cmbComboBox)

        #La forma mas facil de ingresar items en Python es con listas o tuplas.
        self.cmbComboBox.addItems(self.nombre_dni[0])

        #Al hacer check podemos provocar eventos
        self.cmbComboBox.currentIndexChanged.connect(self.on_cmbComboBox_currentIndexChanged)
        self.cmbComboBox.currentTextChanged.connect(self.on_cmbComboBox_currentTextChanged)

        malla.addLayout(cajaV,1,0,1,1)

        #Editor multilinea en QT
        self.txeAreaTexto = QTextEdit()
        malla.addWidget(self.txeAreaTexto,1,1,1,1)


        container = QWidget()
        container.setLayout(malla)

        self.setCentralWidget(container)
        self.show()

    #el metodo que utilizamos para cambiar el indice de combobox y realizamos algun cambio
    def on_cmbComboBox_currentIndexChanged(self, indice):
        print(self.cmbComboBox.itemText(indice))
        print(self.cmbComboBox.currentText())
        self.txeAreaTexto.setPlainText("Seleccionaste el usuario: " + self.cmbComboBox.itemText(indice) + " con DNI: " + self.nombre_dni[1][indice])

    def on_cmbComboBox_currentTextChanged(self, texto):
        print("El combo tiene seleccionado el texto " + texto)

    #metodo que se llama cuando se selecciona un elemento en la tabla
    def on_tTabla_selectionChanged(self):
        indices = self.tTabla.selectedIndexes()
        if indices is not None:
            print(self.modelo.tabla[indices[0].row()][indices[0].column()])
            self.txeAreaTexto.setPlainText(str(self.modelo.tabla[indices[0].row()][indices[0].column()]))

    #Con esta función escribimos en el cuadro de texto una lista de elementos y las añadimos a la tabla con el primer radio buton
    def on_rdButton1_toogled(self):
        if self.rdButton1.isChecked():
            campos = self.txeAreaTexto.toPlainText().split(",")
            self.modelo.tabla.append([campos[0],campos[1],campos[2],True if campos[3] == 'True' else False])
            #Hay que forzar que la vista se repinte
            self.modelo.layoutChanged.emit()

if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    ventana = EjemploInterfazQT()
    aplication.exec()