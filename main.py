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

if turno_actual == "humano":
    mano_actual = computadora
    turno_actual = "PC"

elif turno_actual == "PC":
    mano_actual = jugador1
    turno_actual = "humano"

else:
    mano_actual = None

if mano_actual is not None:
    print("Siguiente turno:", turno_actual)
    print("Fichas disponibles:", mano_actual)

    extremo_izquierdo = mesa[0][0]
    extremo_derecho = mesa[-1][1]

    print("Extremo izquierdo:", extremo_izquierdo)
    print("Extremo derecho:", extremo_derecho)


# Identificar fichas jugables
ficha_seleccionada = None
if mano_actual is not None:
    print("Fichas que puede jugar ", turno_actual)

    fichas_jugables = []

    for ficha in mano_actual:
        if ficha[0] == extremo_derecho or ficha[1] == extremo_derecho:
            fichas_jugables.append(ficha)

        elif ficha[0] == extremo_izquierdo or ficha[1] == extremo_izquierdo:
            fichas_jugables.append(ficha)
    
    print("Fichas jugables:", fichas_jugables)
    print("Cantidad de opciones:", len(fichas_jugables))

    if turno_actual == "PC":
        if len(fichas_jugables) > 0:

            # Seleccionar una ficha aleatoria
            ficha_seleccionada = random.choice(fichas_jugables)

            print("La PC seleccionó:", ficha_seleccionada)

        else:
            print("La PC no tiene fichas jugables")

    #Selección de ficha del jugador humano
    else:
        if len(fichas_jugables) > 0:
            print("Opciones disponibles:", fichas_jugables)
            while True:
                try:
                    opcion = int(input("Selecciona una ficha: "))

                    if 1 <= opcion <= len(fichas_jugables):
                        ficha_seleccionada = fichas_jugables[opcion - 1]
                        print("El humano seleccionó:", ficha_seleccionada)
                        break
                    else:
                        print("Opción no válida")

                except ValueError:
                    print("Error: debes ingresar un número entero")
        else:
            print("No tienes fichas jugables")

if ficha_seleccionada is not None:
    jugada_realizada = False

    if ficha_seleccionada[0] == extremo_derecho:
        mesa.append(ficha_seleccionada)
        jugada_realizada = True
    elif ficha_seleccionada[1] == extremo_derecho:
        invertir_ficha = (ficha_seleccionada[1], ficha_seleccionada[0])
        mesa.append(invertir_ficha)
        jugada_realizada = True
    elif ficha_seleccionada[1] == extremo_izquierdo:
        mesa.insert(0, ficha_seleccionada)
        jugada_realizada = True
    elif ficha_seleccionada[0] == extremo_izquierdo:
        invertir_ficha = (ficha_seleccionada[1], ficha_seleccionada[0])
        mesa.insert(0, invertir_ficha)
        jugada_realizada = True
    if jugada_realizada:
        mano_actual.remove(ficha_seleccionada)
        print("Mesa actualizada:", mesa)
        print("Fichas restantes:", len(mano_actual))
        assert (
            len(jugador1)
            + len(computadora)
            + len(restantes)
            + len(mesa)
        ) == 28, "Error: se perdió o duplicó una ficha"