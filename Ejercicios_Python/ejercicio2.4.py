
def convertirFarenheitCelsius (gradosF):
    gradosC = (gradosF - 32) * (5/9)
    print(gradosF, "gradosFarenheit son: ",gradosC," grados Celsius")

convertirFarenheitCelsius(45)

def tablaGradosFarenheit(cantidad):

    for gradoF in range(0,cantidad,10):
        gradoC = (gradoF - 32) * (5/9)
        print(gradoF,": grados Farenheit son: %5.2f  grados Celsis" % gradoC)
        print("--------------------------")

tablaGradosFarenheit(300)

