from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary

#el guion es donde va a ir el contenido de nuestro informe
guion = []

imagen = Image("../foto.jpg", 23, 23)

texto = Paragraph('Libre')

titulo = ['HORARIO','','','','','','','']

cab = ['', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

actM = ['Mañan', 'Clases', 'Correr', [imagen,texto], [imagen,texto],[imagen,texto],'Estudiar','Trabajar']

actT = ['Tarde', 'Trabajar', 'Clases', 'Clases', 'Clases', 'Trabajar', 'Trabajar', 'Leer' ]

actN = ['Noche', [imagen,texto], 'Trabajar', 'Trabajar', 'Trabajar', [imagen,texto], [imagen,texto], [imagen,texto]]

tabla = Table ([titulo,cab, actM,actT,actN])

#-----Realizamos estilos a la tabla
#setstyle(propiedas,desde donde, hasta donde, parametro ene ste caso color)
#el conteo puede ser de positivo desde las celdas (0,1,2...) o empieza desde la ultima en negativo(-1,-2,-3...)
#Innergrid sirve para realizar una malla en el rango de coordenada indicado
#lineabove realiza una linea superior en el rango indicado
#lineafter realiza una linea despues de un rango indicado
#SPAN une celdas en un rango indicado
#align centra en horizontal el contenido de un rango
#verticalalign centra en vertical duh
#background pone un color de fondo en un rango
tabla.setStyle(
    [('TEXTCOLOR',(1,-4),(7,-4), colors.red),
     ('TEXTCOLOR',(0,1),(0,4), colors.blue),
     ('BACKGROUND',(0,0),(-1,0),colors.lightblue),
     ('BOX',(0,0),(-1,-1),1, colors.blue),
     ('INNERGRID',(1,1),(-1,-1),0.25, colors.lightgrey),
     ('LINEABOVE',(1,1),(-1,1),0.25,colors.lightgrey),
     ('LINEAFTER',(0,1),(0,-1),0.25,colors.lightgrey),
     ('SPAN',(0,0),(-1,0)),
     ('ALIGN',(0,0),(-1,0),'CENTER')
     ])


guion.append(tabla)

doc = SimpleDocTemplate("tablasPlatypus.pdf", pagesize = A4, showBoundary = 0)

doc.build(guion)