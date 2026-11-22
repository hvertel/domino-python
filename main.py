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
print(fichas) 

#Revolver las fichas
random.shuffle(fichas)
print(fichas) 

#creando jugadores y asignando fichas al azar
jugador1 = fichas[:7]
computadora= fichas[7:14]
restantes = fichas[14:]


print("jugador1", jugador1)
print("computador", computadora)
print("restantes", restantes)        
print("total fichas: ", len(fichas))
assert len(jugador1) == 7 #Compruba que tenga 7 fichas
assert len(computadora) == 7 #Compruba que tenga 7 fichas
assert len(restantes) == 14 #Compruba que tenga 14 fichas
assert len(jugador1) + len(computadora) + len(restantes) == 28 #Compruba que sumen 28
assert len(fichas) == 28, "Error: Deben existir 28 fichas" #comporbación de que las fichas están completas.
