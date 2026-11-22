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

print("total fichas: ", len(fichas))

assert len(jugador1) == 7 #Comprueba que tenga 7 fichas
assert len(computadora) == 7 #Comprueba que tenga 7 fichas
assert len(restantes) == 14 #Comprueba que tenga 14 fichas
assert len(jugador1) + len(computadora) + len(restantes) == 28 #Compruba que sumen 28
assert len(fichas) == 28, "Error: Deben existir 28 fichas" #comprobación de que las fichas están completas.


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

#Determinando quien empieza y primera jugada automatica
mesa = []
if doble_j1 > doble_pc:
    turno_actual = "humano"
    ficha_inicial = (doble_j1, doble_j1)
    jugador1.remove((ficha_inicial))
    mesa.append((ficha_inicial))

elif doble_j1 < doble_pc:
    turno_actual = "PC"
    ficha_inicial = (doble_pc, doble_pc)
    computadora.remove((ficha_inicial))
    mesa.append((ficha_inicial))
else:
    turno_actual = None


#Comporbando que no se pieurdan fichas
assert (
    len(jugador1)
    + len(computadora)
    + len(restantes)
    + len(mesa)
) == 28

print("Turno inicial:", turno_actual)
print("Mesa:", mesa)
print("Fichas humano:", len(jugador1))
print("Fichas PC:", len(computadora))

# RETO 08F - Jugar una ficha por la izquierda

mesa_prueba = [(6, 4), (4, 2), (2, 1)]
ficha_jugada = (4, 4)

extremo_izquierdo = mesa_prueba[0][0]
extremo_derecho = mesa_prueba[-1][-1]

if ficha_jugada[0] == extremo_izquierdo:
    ficha_invertida = (ficha_jugada[1], ficha_jugada[0])
    mesa_prueba.insert(0, ficha_invertida)

elif ficha_jugada[1] == extremo_izquierdo:
    mesa_prueba.insert(0, ficha_jugada)

else:
    print("La ficha no puede jugarse por la izquierda")

if ficha_jugada[1] == extremo_derecho:
    ficha_invertida = (ficha_jugada[1], ficha_jugada[0])
    mesa_prueba.append(ficha_invertida)

elif ficha_jugada[0] == extremo_derecho:
    mesa_prueba.append(ficha_jugada)

else:
    print("La ficha no puede jugarse por la derecha")

print("Mesa actualizada:", mesa_prueba)