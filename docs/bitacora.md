# Bitácora de desarrollo

## Sesión 01 - Fundamentos del dominó

### Objetivo

Desarrollar las estructuras de datos y los algoritmos iniciales de un juego de dominó doble seis utilizando Python, mediante la representación de fichas, generación del conjunto completo, distribución aleatoria entre jugadores e identificación del participante que inicia la partida.

El proyecto se desarrolla de manera incremental, mediante retos de programación que permiten comprender los fundamentos del lenguaje antes de construir las funcionalidades completas del videojuego.

### Conceptos estudiados

- Variables y asignación de valores.
- Tipos de datos: números enteros y tuplas.
- Listas y acceso a elementos mediante índices.
- Estructuras condicionales `if`, `elif` y `else`.
- Operadores de comparación.
- Ciclos `for` y función `range()`.
- Ciclos anidados.
- Métodos de listas: `append()`.
- Segmentación de listas mediante *slicing*.
- Importación de módulos.
- Aleatorización mediante `random.shuffle()`.
- Definición de funciones mediante `def`.
- Parámetros, argumentos y valores de retorno.
- Uso de `print()` para visualizar resultados.
- Validación mediante instrucciones `assert`.
- Indentación y control del flujo de ejecución.

### Desarrollo de los retos

#### Reto 01 - Representación de una ficha de dominó

**Problema planteado**

Representar una ficha de dominó mediante una estructura de datos que permita almacenar y consultar sus dos extremos.

**Proceso de solución**

Se estudió el concepto de tupla como una estructura que permite agrupar valores relacionados.

Se estableció que cada ficha estaría representada mediante dos números enteros comprendidos entre 0 y 6.

```python
ficha = (6, 4)
```

Posteriormente, se exploró el acceso a los elementos mediante índices:

```python
ficha[0]  # Primer extremo
ficha[1]  # Segundo extremo
```

Se comprendió que los índices de las secuencias en Python comienzan en cero.

**Resultado**

Se consiguió representar individualmente las fichas de dominó y consultar sus valores.

**Aprendizaje**

Una estructura de datos permite modelar objetos del mundo real. En este proyecto, las tuplas representan fichas con dos extremos definidos.

---

#### Reto 02 - Identificación de fichas dobles

**Problema planteado**

Determinar si una ficha de dominó es doble, es decir, si sus dos extremos contienen el mismo valor.

**Proceso de solución**

Se implementó una estructura condicional para comparar ambos elementos de la tupla.

```python
if ficha[0] == ficha[1]:
    print("La ficha es doble")
```

Se estudió la diferencia entre el operador de asignación `=` y el operador de comparación `==`.

**Resultado**

El programa logró identificar fichas dobles mediante la evaluación de una condición lógica.

**Aprendizaje**

Las estructuras condicionales permiten que un programa tome decisiones según las características de los datos.

---

#### Reto 03 - Generación de fichas mediante ciclos

**Problema planteado**

Evitar la creación manual de cada ficha y utilizar una estructura repetitiva para generarlas automáticamente.

**Proceso de solución**

Se creó una lista vacía y se utilizó un ciclo `for` con `range(7)` para producir las fichas comprendidas entre `(0, 0)` y `(0, 6)`.

```python
fichas = []

for numero in range(7):
    fichas.append((0, numero))
```

Se introdujo el método `append()` para agregar elementos a una lista.

**Resultado**

Se generaron automáticamente siete fichas mediante un ciclo.

**Aprendizaje**

Los ciclos permiten automatizar operaciones repetitivas y reducir la escritura manual de instrucciones.

---

#### Reto 04 - Construcción del conjunto completo de 28 fichas

**Problema planteado**

Generar todas las fichas del dominó doble seis, evitando duplicados equivalentes como `(2, 5)` y `(5, 2)`.

**Proceso de solución**

Se estudiaron los ciclos anidados, utilizando un primer ciclo para recorrer los posibles valores del extremo izquierdo y un segundo ciclo para construir las combinaciones restantes.

La solución implementada fue:

```python
fichas = []

for izquierda in range(7):
    for derecha in range(izquierda, 7):
        fichas.append((izquierda, derecha))
```

La decisión fundamental consistió en iniciar el segundo recorrido desde el valor de `izquierda`.

De esta manera, cuando el primer extremo vale 3, el segundo solamente puede tomar valores desde 3 hasta 6.

Esta estrategia evita generar combinaciones equivalentes en orden inverso.

**Resultado**

Se construyó el conjunto completo de 28 fichas únicas del dominó doble seis.

**Aprendizaje**

Los ciclos anidados permiten generar combinaciones de valores. La definición adecuada de los rangos evita duplicaciones y operaciones innecesarias.

---

#### Reto 05 - Aleatorización de las fichas

**Problema planteado**

Preparar el conjunto de fichas para que su distribución no siguiera siempre el mismo orden.

**Proceso de solución**

Se importó el módulo `random` de la biblioteca estándar de Python.

```python
import random
```

Posteriormente, se utilizó:

```python
random.shuffle(fichas)
```

Se comprobó que las fichas cambiaban de posición sin alterar la cantidad total de elementos.

También se incorporó una validación:

```python
assert len(fichas) == 28
```

**Resultado**

El programa logró mezclar las 28 fichas antes de repartirlas.

**Aprendizaje**

Los módulos permiten incorporar funcionalidades existentes. El método `shuffle()` modifica el orden de los elementos de una lista sin crear un conjunto nuevo.

---

#### Reto 06 - Distribución de fichas y visualización de jugadores

**Problema planteado**

Distribuir las fichas entre un jugador humano, una computadora y un conjunto de fichas restantes.

**Proceso de solución**

Se utilizó la segmentación de listas (*slicing*) para seleccionar diferentes intervalos del conjunto previamente mezclado.

```python
jugador1 = fichas[:7]
computadora = fichas[7:14]
restantes = fichas[14:]
```

La distribución quedó definida así:

- Jugador humano: 7 fichas.
- Computadora: 7 fichas.
- Pozo o fichas restantes: 14 fichas.

Posteriormente, se identificó que imprimir repetidamente la información de cada participante generaba instrucciones redundantes.

Para resolverlo, se construyó una función reutilizable:

```python
def mostrar_fichas(nombre, mano):
    print("Participante:", nombre)
    print("Fichas:", mano)
    print("Cantidad:", len(mano))
    print("------------------------")
```

La función se utilizó con diferentes argumentos:

```python
mostrar_fichas("humano", jugador1)
mostrar_fichas("PC", computadora)
mostrar_fichas("Fichas restantes", restantes)
```

Finalmente, se incorporaron comprobaciones:

```python
assert len(jugador1) == 7
assert len(computadora) == 7
assert len(restantes) == 14

assert len(jugador1) + len(computadora) + len(restantes) == 28
```

**Resultado**

Se implementó la distribución inicial de las fichas y una función para visualizar su contenido.

**Aprendizaje**

La segmentación permite extraer subconjuntos de una lista. Las funciones facilitan la reutilización del código y las aserciones permiten comprobar condiciones que deben cumplirse durante la ejecución.

---

#### Reto 07 - Identificación del doble mayor y determinación del jugador inicial

**Problema planteado**

Determinar cuál de los dos participantes posee la ficha doble de mayor valor para establecer quién comienza la partida.

**Proceso de solución**

Inicialmente se construyó una función que recorría las fichas de un jugador e identificaba aquellas cuyos extremos eran iguales.

Durante el desarrollo aparecieron varias dificultades que permitieron profundizar en la comprensión del lenguaje.

**Primera dificultad: comparación entre tipos de datos incompatibles.**

Se intentó comparar una ficha completa, representada mediante una tupla, con un valor entero:

```python
if ficha > doble_mayor:
```

Se identificó que esta comparación no era válida porque `ficha` contenía una tupla y `doble_mayor` un número entero.

La solución consistió en acceder al primer elemento de la ficha:

```python
if ficha[0] > doble_mayor:
```

**Segunda dificultad: almacenamiento de un tipo de dato incorrecto.**

Inicialmente se utilizó:

```python
doble_mayor = ficha
```

Esto almacenaba la tupla completa en una variable destinada a guardar un valor numérico.

La instrucción se corrigió por:

```python
doble_mayor = ficha[0]
```

**Tercera dificultad: ubicación incorrecta de `return`.**

En una primera versión, `return` estaba dentro del ciclo de búsqueda, lo que podía finalizar la función al encontrar el primer doble sin revisar las fichas restantes.

Se comprendió que la instrucción debía ejecutarse después de completar el recorrido.

**Cuarta dificultad: utilización innecesaria de `else`.**

Se incorporó inicialmente un bloque que contenía únicamente el nombre de la variable:

```python
else:
    doble_mayor
```

Se identificó que esta expresión no modificaba el estado de la variable ni era necesaria para resolver el problema.

El bloque se eliminó.

**Solución final de la función**

```python
def doble_mayor(mano):
    doble_mayor = -1

    for ficha in mano:
        if ficha[0] == ficha[1]:
            if ficha[0] > doble_mayor:
                doble_mayor = ficha[0]

    return doble_mayor
```

La variable se inicializa con `-1` para representar la ausencia de fichas dobles.

Posteriormente, se comprendió la diferencia entre imprimir resultados y devolver valores mediante `return`.

Se almacenaron los resultados de la función en variables:

```python
doble_j1 = doble_mayor(jugador1)
doble_pc = doble_mayor(computadora)
```

Finalmente, se implementó la comparación:

```python
if doble_j1 > doble_pc:
    print("Inicia Humano")
elif doble_j1 < doble_pc:
    print("Inicia PC")
else:
    print("No se pudo determinar por doble mayor")
```

**Comprobación realizada**

En una ejecución documentada, el jugador humano recibió la ficha `(6, 6)` y la computadora recibió como doble mayor `(4, 4)`.

El programa produjo correctamente:

```text
Inicia Humano
total fichas: 28
```

**Resultado**

Se implementó un algoritmo que identifica el doble mayor de cada jugador y determina quién debe iniciar cuando existe un doble mayor entre las manos.

Queda pendiente definir el criterio alternativo cuando ninguno de los jugadores posee fichas dobles.

**Aprendizaje**

Se comprendió la importancia de los tipos de datos, la indentación, los valores de retorno, las variables de seguimiento y la utilización de condicionales para construir algoritmos de decisión.

---

### Dificultades encontradas

Durante la sesión se identificaron las siguientes dificultades:

1. **Comprensión de los índices:** fue necesario distinguir entre una ficha completa y los valores almacenados en sus posiciones.
2. **Generación de combinaciones sin duplicados:** se requirió comprender cómo interactúan los ciclos anidados y cómo establecer sus rangos.
3. **Comparación de tipos de datos:** se intentó comparar una tupla con un entero, lo que evidenció la necesidad de reconocer el tipo de cada variable.
4. **Actualización de variables:** se identificó la diferencia entre almacenar una ficha completa y almacenar uno de sus valores.
5. **Indentación y flujo de ejecución:** la ubicación inicial de `return` impedía recorrer completamente la mano.
6. **Diferencia entre `print()` y `return`:** inicialmente se imprimían los dobles encontrados durante el recorrido, sin almacenar los resultados para utilizarlos posteriormente.
7. **Condiciones sin acciones necesarias:** se incorporó un bloque `else` que no realizaba ninguna operación útil.

### Soluciones implementadas

Al finalizar la sesión, el programa dispone de las siguientes funcionalidades:

- Representación de fichas mediante tuplas de dos enteros.
- Generación automática de las 28 fichas únicas del dominó doble seis.
- Mezcla aleatoria del conjunto de fichas.
- Distribución de siete fichas para el jugador humano y siete para la computadora.
- Conservación de catorce fichas restantes para el pozo.
- Visualización de las manos mediante una función reutilizable.
- Validación de las cantidades de fichas mediante `assert`.
- Identificación del doble de mayor valor en una mano.
- Comparación de los dobles mayores para determinar el jugador inicial.

### Aprendizajes

El principal aprendizaje de esta sesión fue comprender que un programa puede construirse progresivamente mediante la resolución de problemas pequeños y verificables.

Se avanzó desde la representación de un objeto mediante una tupla hasta la construcción de un algoritmo capaz de tomar decisiones utilizando estructuras de datos, ciclos, funciones y condicionales.

También se reconoció la importancia de la depuración. Los errores encontrados no solamente permitieron corregir instrucciones, sino comprender cómo Python interpreta los tipos de datos, ejecuta los ciclos y administra los valores de retorno.

El uso de funciones permitió comenzar a separar responsabilidades dentro del programa, mientras que las aserciones introdujeron una práctica básica de verificación del comportamiento esperado.

### Estado actual del proyecto

**Etapa 1: Fundamentos del dominó — Completada.**

Se finalizaron los siete retos iniciales y se dispone de una primera implementación funcional de la preparación de una partida.

El programa todavía no constituye un juego completo: no permite colocar fichas sobre una mesa, validar movimientos, alternar turnos, robar del pozo ni determinar al ganador.

**Decisiones de diseño establecidas:**

- Lenguaje: Python.
- Modalidad: dominó doble seis.
- Participantes: un jugador humano y una computadora.
- Distribución inicial: siete fichas por participante.
- Pozo: catorce fichas.
- Modalidad de juego: dominó con robo.
- Criterio inicial de apertura: mayor doble disponible entre los jugadores, con regla alternativa pendiente.

### Próxima sesión - Construcción de la lógica del juego

**Reto 08: creación de la mesa y primera jugada.**

Se estudiarán los métodos `remove()` y `append()` para trasladar fichas desde la mano de un jugador hasta la mesa.

Posteriormente, se implementarán las reglas para validar movimientos y actualizar el estado de la partida.

El desarrollo continuará mediante ejercicios progresivos, pruebas de consola y registro de las dificultades y soluciones en esta bitácora.

### Referencias técnicas

Python Software Foundation. (2026). *The Python tutorial: An informal introduction to Python*. https://docs.python.org/3/tutorial/introduction.html

Python Software Foundation. (2026). *The Python tutorial: More control flow tools*. https://docs.python.org/3/tutorial/controlflow.html

Python Software Foundation. (2026). *The Python tutorial: Data structures*. https://docs.python.org/3/tutorial/datastructures.html

Python Software Foundation. (2026). *random — Generate pseudo-random numbers*. https://docs.python.org/3/library/random.html
