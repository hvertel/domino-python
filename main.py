#Laboratorio Dominó
#Primera Sesión - Represetación de Fichas

ficha = (6, 4) #Crear una ficha
print("Ficha:",ficha) #esto muestra la ficha
print("lado izquierdo", ficha[0]) #viendo los lados de la ficha
print("lado derecho", ficha[1]) #viendo los lados de la ficha
if ficha[0] == ficha[1]: #Condicional comprueba cuando una ficha es doble o no
    print("Esta ficha es doble")
else:
    print("Esta ficha NO es doble")

