# Primer reto de URI - Alliteration (1263)

El principal problema del reto es encontrar el número
de aliteraciones en una línea de texto. Una aliteración
consiste de dos o más palabras consecutivas que comienzan
con la misma letra (sin importar mayúsculas).

## Descripción del algoritmo
La idea del algoritmo usado en el método `getAlliterations` 
consiste en ir recorriendo la línea palabra a palabra y solo
nos interesa la primera letra. La última letra vista la 
tenemos que ir recordando y compararla con la letra actual,
si son iguales, entonces aumentamos un contador para saber
que se vio otra ocurrencia de esa letra, y revisamos
que el contador ya sea igual a 2, en ese caso aumentamos
el número de aliteraciones en 1. En el caso de que 
la letra actual y la anterior sean distintas, entonces
reiniciamos el contador en 1 y guardamos la letra actual
como la letra anterior.

## Ejecución del programa

- Compilar con `javac Main.java`
- Ejecutar con `java Main`
