#Laboratorio Dominó
#Primera Sesión - Represetación de Fichas


#Importar modulo random para revolver las fichas
import random

#Crear la lista que contiene las fichas
fichas = [] 

#agregar fichas a la lista de fichas
for izquierda in range(7):
    for derecha in range(izquierda, 7):
        fichas.append((izquierda, derecha))

#Revolver las fichas
random.shuffle(fichas)

#creando jugadores y asignando fichas al azar
jugador1 = fichas[:7]
computadora= fichas[7:14]
restantes = fichas[14:]

#Creando la funcion que muestra las fichas
def mostrar_fichas(nombre, mano):
    print("Participante: ", nombre)
    print("Fichas: ", mano)
    print("Cantidad: ", len(mano))
    print("------------------------")

mostrar_fichas("humano", jugador1)
mostrar_fichas("PC", computadora)
mostrar_fichas("Fichas restantes", restantes)

#Funcion para recorrer listas y ecnontrar el doble mas grande
def doble_mayor(mano):
    doble_mayor = -1

    for ficha in mano:
        if ficha[0] == ficha[1]:
            if ficha[0] > doble_mayor:
                doble_mayor = ficha[0]
    return doble_mayor
    
doble_j1 = doble_mayor(jugador1)
doble_pc = doble_mayor(computadora)

#Determinando quien empieza
if doble_j1 > doble_pc:
    turno_actual = "humano"
elif doble_j1 < doble_pc:
    turno_actual = "PC"
else:
    turno_actual = None
print("Turno inicial:", turno_actual)
    
print("total fichas: ", len(fichas))
assert len(jugador1) == 7 #Comprueba que tenga 7 fichas
assert len(computadora) == 7 #Comprueba que tenga 7 fichas
assert len(restantes) == 14 #Comprueba que tenga 14 fichas
assert len(jugador1) + len(computadora) + len(restantes) == 28 #Compruba que sumen 28
assert len(fichas) == 28, "Error: Deben existir 28 fichas" #comprobación de que las fichas están completas.