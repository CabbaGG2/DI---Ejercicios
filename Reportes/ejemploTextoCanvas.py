from reportlab.pdfgen import canvas

#fuente de donde se sacara el texto
texto = ('Este texto es para ejemplo', 'de utilización de Canvas', 'para usar con texto.', 'Alargo el texto', 'para tener más lineas', 'y notar el efecto')

#creamos un objecto canvas del pdf resultante
objCanvas = canvas.Canvas("textoCanvas.pdf")

#begintext permite crear texto
objTexto = objCanvas.beginText()

#da las cordenadas para empezar a escribir
objTexto.setTextOrigin(100,300)

#se puede formatear con setFont
objTexto.setFont("Courier",16)

#creamos una linea por frase
for linea in texto:
    objTexto.textLine(linea)

#cambia de color el texto y el texto largo en ese formato ya identa automaticamente
objTexto.setFillGray(0.5)
textoLargo = """Otro texto con varias
                lineas incorporadas,
                con retorno de carro
                incluidos
"""

#textLines en plural busca el retorno de carro de varias lineas y facilita la colocación.
objTexto.textLines(textoLargo)

#
objTexto.setTextOrigin(20,800)

#tipos de letras
for tipo_letra in objCanvas.getAvailableFonts():
    objTexto.setFont(tipo_letra, 16)
    objTexto.textLine("Texto de ejemplo con fuente: " + tipo_letra)
    #es un diferencial, va a ir aumentando

#El color, la posicion, y la fuente tienen que ir antes para que se pueda ver y leer
objTexto.setFillColorRGB(0.2,0,0.6)

objTexto.setFillColor("Pink",1)

objTexto.setFont("Helvetica",18)

for linea in texto:
    # vamos dandole posicion segun el lugar del cursor
    objTexto.moveCursor(20, 15)
    #otro metodo para colocar texto
    objTexto.textOut(linea)

#Vamos ahora a configurar el espacio entre caracteres
objTexto.moveCursor(-60,15)
espacioCaracteres = 0
for linea in texto:
    objTexto.setCharSpace(espacioCaracteres)
    objTexto.textLine("Espacio %s: %s " % (espacioCaracteres, linea))
    #incrementamos...
    espacioCaracteres += 1

objTexto.setFillColor("Green",0.5)
objTexto.setTextOrigin(20,110)
#tambien podemos configurar el espacio entre palabras...
objTexto.setCharSpace(1)
objTexto.setWordSpace(8)
objTexto.textLines((textoLargo))


#imprimimos en el pdf, mostramos y guardamos.
objCanvas.drawText(objTexto)

objCanvas.showPage()
objCanvas.save()