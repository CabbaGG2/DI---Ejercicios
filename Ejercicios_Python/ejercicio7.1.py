"""Escribir una funcion que reciba una tupla de elementos e iddique
    si se encuentran ordenados de mayor a menor"""
from unicodedata import numeric

tOrdenada = (1,2,3,4,5,6,7,8,9,10)
tDesornada = (1,5,8,12,45,0,8,3,1,45)

def estaOrdenado(tupla):
    numero = 0
    esMayor = True
    for t in tupla:
        if(t >= numero):
            numero = t
            continue
        else:
            esMayor = False
            break
    if(esMayor):
        print("Esta Ordenado")
    else:
        print("Esta Desordenado")

estaOrdenado(tOrdenada)