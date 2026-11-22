#Laboratorio Dominó
#Primera Sesión - Represetación de Fichas

#Crear la lista que contiene las fichas
fichas = [] 

#agregar fichas a la lista de fichas
for izquierda in range(7):
    for derecha in range(izquierda, 7):
        fichas.append((izquierda, derecha))

print(fichas)        
print("total fichas: ", len(fichas))
assert len(fichas) == 28, "Error: Deben existir 28 fichas" #comporbación de que las fichas están completas.