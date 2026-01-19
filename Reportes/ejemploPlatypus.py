from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary

from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie, Pie3d
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.rl_settings import strikeWidth

guion = []

#cojemos la hoja de estilo
hojaEstilo = getSampleStyleSheet()

cabecera = hojaEstilo ["Heading2"]

#esto puede ser 0 o 1, si es 1 daria un salto de página completa
cabecera.pageBreakBefore = 0

#modifica el color
cabecera.backColor = colors.lightblue

#----Hacemos otra cabecera----
cabeceraCursiva = hojaEstilo ["Heading4"]

cabeceraCursiva.fontName = "Helvetica-Oblique"

cabeceraCursiva.fontSize = 18

cabeceraCursiva.alignment = 1

cabeceraCursiva.borderColor = colors.blue

cabeceraCursiva.borderWidth = 1

#aplicamamos el estilo al nuevo paragraph
titulo = Paragraph("Titulo del documento", cabeceraCursiva)
guion.append(titulo)

#creamos un paragraph basandonos en la hoja de estilos del ejemplo
paragrafo = Paragraph("CABECERA DEL DOCUMENTO", cabecera)
guion.append(paragrafo)

texto = "Texto incluido en el documento, el que forma el contenido" * 1000

#recogemos el cuerpo del texto
cuerpoTexto = hojaEstilo ['BodyText']

cuerpoTexto.fontSize = 12

#hacemos un paragrafo en donde pasamos el texto y el estilo es cuerpoTexto
paragrafo2 = Paragraph (texto, cuerpoTexto)

guion.append(paragrafo2)

#dejamos un prqueñ hueco para dar espacio
guion.append (Spacer (0,30))

imagen = Image("foto.jpg",400,400)

guion.append(imagen)

#--------AÑADIMOS UN GRAFICO-----------
d = Drawing(400,200)

datos = [(13.3,8,14.3,25,33.3,37.5,21.1,28.6,45.5,38.1,54.6,36.0,42.3), (67,69,68,81,92,90,87,82,77,79,59,69,61)]
lendaDatos = ['11/12','12/13','13/14','14/15','15/16','16/17','17/18','18/19','19/20','20/21','21/22','22/23','23/24','24/25']

#tipo de grafico, en este caso barras verticales
graficoBarras = VerticalBarChart()

graficoBarras.x = 50
graficoBarras.y = 50
graficoBarras.height = 125
graficoBarras.width = 300
graficoBarras.data = datos
graficoBarras.valueAxis.valueMin = 0
graficoBarras.valueAxis.valueMax = 100
graficoBarras.valueAxis.valueStep = 10
graficoBarras.categoryAxis.labels.boxAnchor = 'ne'
graficoBarras.categoryAxis.labels.dx = 8
graficoBarras.categoryAxis.labels.dy = -10
graficoBarras.categoryAxis.labels.angle = 30
graficoBarras.categoryAxis.categoryNames = lendaDatos
#espace los graficos
graficoBarras.groupSpacing = 10
#se espacea entre las barras
graficoBarras.barSpacing = 3

d.add(graficoBarras)

guion.append(Spacer(0,20))

guion.append(d)

#creamos el documento ahora: pagesize tamaño de pagina, showboundat crea margen
doc = SimpleDocTemplate("ejemploPlatypus.pdf",pagesize =A4, showBoundary = 1)

doc.build(guion)

#para saber que hay
#print(hojaEstilo.list())
