# Modelado y Programación 2022-2
Reto de URI - Passwords Validator (2253)

González Alvarado Raúl - 313245312

## Descripción del algoritmo
Se quiere validar 4 condiciones que deben ser ciertas:
- Al menos una letra minúscula
- Al menos una letra mayúscula
- Al menos un dígito
- Tamaño entre 6 y 32
Y una condición que no se debe cumplir:
- Tener espacios, acentos o signos de puntuación

Inicializamos un arreglo con 4 entradas, todas falsas,
una por cada condición que queremos sea cierta.
Vamos a recorrer la cadena caracter a caracter,
si se encuentra algo que no sea dígito o número, entonces
regresamos falso (aquí ya cubrimos la condición que no 
queremos que se cumpla).
Si el caracter es minúscula entonces asignamos true a
la entrada correspondiente del arreglo.
Si el caracter es mayúscula entonces asignamos true a
la entrada correspondiente del arreglo.
Si el caracter es un dígito entonces asignamos true a
la entrada correspondiente del arreglo.
Finalizamos el ciclo.
Si el tamaño de la contraseña está entre 6 y 32,
asignamos true a la entrada correspondiente del arreglo.

Si todas las entradas del arreglo son verdaderas, entonces
regresamos verdadero; false en otro caso.

## Ejecución del programa
- Compilar con `javac Main.java`
- Ejecutar con `java Main`

## Casos de prueba
Se añadieron los casos de prueba que vienen en la
descripción del problema en la página de URI.
Estos se pueden ejecutar con usando la opción `--test`
al momento de ejecutar el programa, lo cuál ocasiona que
se ejecuten los tests y no el programa de forma usual
(`java Main --test`).

Aun que esto no es un buen diseño (ya que tenemos el
código y los tests en un mismo archivo), consideré que
estaban bien ahí, ya que es un programa relativamente
pequeño y consideré inecesario agregar algúna herramienta
como _Graddle_ o _Maven_ al proyecto.
