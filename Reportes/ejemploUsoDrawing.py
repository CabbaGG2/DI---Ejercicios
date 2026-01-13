from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

#aqui los elementos que utilicemos se colocan en listas
guion = []

imaxe = Image(0,0,500,180,"foto.jpg")

#la imagen va dentro de un Drawing
debuxo = Drawing(300,102)
#al drawing añadimos la imagen
debuxo.add(imaxe)

debuxo2 = Drawing()
debuxo2.add(imaxe)
#el translate ayuda a mover la imagen en la hoja de dibujo
debuxo2.translate(150,350)

guion.append(debuxo2)

#============================

debuxo3 = Drawing()

debuxo3.add(imaxe)

#NOTA: se rota primero y luego se traslada de posición para que se traslade con la nueva rotecion y si quiero puedo trasladarlo
#y luego rotarlo
debuxo3.rotate(45)
debuxo3.translate(300,100)
guion.append(debuxo3)


#====================================

debuxo4 = Drawing()
debuxo4.add(imaxe)

#vamos a realizar un escalado
debuxo4.translate(150,500)
debuxo4.scale(0.5,0.5)
guion.append(debuxo4)

#al guion eñadimos el drawing
guion.append(debuxo)

#creamos la hoja de dibujo Drawing(ancho,alto) dimensiona en A4
folla = Drawing(A4[0],A4[1])

#esto es para añadir todos los elementos drawing que vayamos creando
for elemento in guion:
    folla.add(elemento)


renderPDF.drawToFile(folla,"ejemploConDrawing.pdf")
