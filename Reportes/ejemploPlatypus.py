from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary

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

#creamos el documento ahora: pagesize tamaño de pagina, showboundat crea margen
doc = SimpleDocTemplate("ejemploPlatypus.pdf",pagesize =A4, showBoundary = 1)

doc.build(guion)

#para saber que hay
#print(hojaEstilo.list())
