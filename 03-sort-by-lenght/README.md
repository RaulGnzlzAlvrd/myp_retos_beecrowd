# Modelado y Programación 2022-2
Reto de URI - Sort by Lenght (1244)

González Alvarado Raúl - 313245312

## Descripción
Se utilizó el lenguaje de programación python3.9.

La idea principal es muy similar a lo que se hace en un merge sort.
Pero en este caso se toman en cuenta dos listas, una con las palabras
y otra con las longitudes de las palabras, de modo que el índice `i` de
las longitudes es la longitud de la palabra `i`.

Al hacer el merge sort, se van comparando las longitudes y se van extrayendo
los elementos correspondientes tanto de la lista de palabras como de la lista
de longitudes.

Como adicional, se puede pasar cualquier función que se aplique sobre la lista
de las palabras para así poder ordenar por otros atributos y no solo por longitud.
También se puede hacer que sea un ordenamiendo ascendente o descendente.

## Instrucciones de ejecución

El programa se ejecuta como un archivo usual de python:
`python main.py`

Para los tests solo hay que ejecutar el archivo correspondiente: `python tests.py`
