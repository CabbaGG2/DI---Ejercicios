from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary

guion = []

fila1 = ['','','','','','FACTURA SIMPLIFICADA','']

fila2 = ['','','Nombre de tu Empresa','','','Logo de la empresa','']

fila3 = ['','','Dirección','','','','']

fila4 = ['','','Ciudad y País','','','','']

fila5 = ['','','CIF/NIF','','','Fecha Emisión','DD/MM/AAAA']

fila6 = ['','','Teléfono','','','Número de Factura','A0001']

fila7 = ['','','Mail','','','','']

fila8 = ['','','','','','','']

fila9 = ['','','Descripción','','Importe','Cantidad','Total']

fila10 = ['','','Producto1','','3.2','5','16.00']

fila11 = ['','','Producto2','','2.1','3','6.30']

fila12 = ['','','Producto3','','2.9','76','220.40']

fila13 = ['','','Producto4','','5','23','115.00']

fila14 = ['','','Producto5','','4.95','3','14.85']

fila15 = ['','','Producto6','','6','2','12.00']

fila16 = ['','','','','','TOTAL','385$']

fila17 = ['','','','','','','']

fila18 = ['GRACIAS POR SU CONFIANZA','','','','','','']

fila19 = ['','','','','','','']

tabla = Table ([fila1,fila2,fila3,fila4,fila5,fila6,fila7,fila8,fila9,fila10,fila11,fila12,fila13,fila14,fila15,fila16,fila17,fila18,fila19])

tabla.setStyle([
    ('INNERGRID',(0,0),(-1,-1),0.25, colors.lightgrey),
    ('SPAN',(5,0),(6,0)),
    ('SPAN', (5, 1), (6, 1)),
])

guion.append(tabla)

doc = SimpleDocTemplate("facturaEjemplo.pdf", pagesize = A4, showBoundary = 0)

doc.build(guion)