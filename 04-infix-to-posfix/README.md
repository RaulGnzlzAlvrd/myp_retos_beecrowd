# Modelado y Programación 2022-2
Reto de URI - Infix to Posfix (1077)

González Alvarado Raúl - 313245312

## Descripción
Se utilizó el lenguaje de programación python3.9.

Se implementó el algoritmo de
[Shunting yard](https://en.wikipedia.org/wiki/Shunting_yard_algorithm).
Es un algoritmo usado para parsear expresiones aritméticas en forma infija
a una forma postfija. La idea principal es ir metiendo los operadores en
un stack para luego sacarlos cuando se esté leyendo un símbolo con menor 
precedencia que el tope del stack. Tambén se ocupa una cola (en mi
implementación es una cadena) en la que se van agregando los elementos que
sacamos del stack de operadores, y los números o símbolos (que no sean 
operadores) que se van leyendo de la expresión infija.

## Instrucciones de ejecución

El programa se ejecuta como un archivo usual de python:
`python main.py`

Para los tests solo hay que ejecutar el archivo correspondiente: `python tests.py`
