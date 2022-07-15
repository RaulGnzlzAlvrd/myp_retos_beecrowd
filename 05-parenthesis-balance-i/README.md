# Modelado y Programación 2022-2
Reto de URI - Parenthesis Balance I (1068)

González Alvarado Raúl - 313245312

## Descripción
Se utilizó el lenguaje de programación python3.9.

## Algoritmo
Cómo que se lee un paréntesis izquierdo significa que más adelante debe
haber uno derecho que sea su par, y como puede haber más de un paréntesis
izquierdo consecutivo. 
El algoritmo implementado va recorriendo la expresión de cada caso de entrada
y va aumentando en uno un contador cada que vemos un paréntesis izquierdo, y
cada que vemos uno derecho decrementamos en 1 el contador.
Si al terminar de recorrer la expresión, el contador es mayor que 0, entonces
significa que se vio un paréntesis izquierdo pero no se vio uno derecho que
le hiciera par, entonces la expresión no es válida.
Si el contador termina en 0 entonces todo paréntesis izquierdo tenía su par
derecho y la expresión es válida.
Si al recorrer la expresión, el contador es menor que 0, quiere decir que
un paso antes, el contador estaba en 0 y se vio un paréntesis derecho, lo que
quiere decir que no hubo un paréntesis izquierdo antes que él en la expresión,
lo que quiere decir que la expresión no es válida.

## Instrucciones de ejecución

El programa se ejecuta como un archivo usual de python:
`python main.py`

El programa finaliza cuando se manda un `EOF` (pulsando `Ctrl+D`).

