from reportlab.pdfgen import canvas


folla = canvas.Canvas ("primerDocumento.pdf")

folla.drawString(0,0,"Posicion inicio (x,y) = (0,0)")
folla.drawString(50,750,"Posicion inicio (x,y) = (50,100)")
folla.drawString(150,20,"Posicion inicio (x,y) = (150,20)")



folla.drawImage("imagen 20*20.jpg",20,700,20,20)

folla.showPage()
folla.save()