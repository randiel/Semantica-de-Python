# Diseño intruccional

En esta lección los alumnos deben entender las reglas que deben seguir para escribir y entender correctamente el lenguaje Python.

Todo lenguaje de programación tiene los siguientes elementos: una gramática y una sintaxis

  ## Objetivos de aprendizaje
  1. Entender las reglas para escribir código Python
  2. Conocer los tiempos y las estrategias para desarrollar con Python
  3. Manejo de comentarios, constantes, variables, cadenas, funciones, capturar un valor e imprimir en pantalla

### 1. Entender las reglas para escribir código Python
Así como en el español podemos identificar que las oraciones estan compuestas por sujeto y predicado, en los lenguajes de programación vamos a tener otros elementos que rigen la escritura correcta del lenguaje:

Variables y expresiones:
- Sentencias simples: Son declaraciones que solo tienen una palabra reservada (import, global, return)
- Sentencias compuestas: Son declaraciones que tienen mas de una palabra reservada (function, for, if, class)
- Asignación/Auto-asignación: Son expresiones que permiten asignar o actualizar el valor de una variable
- Operadores: Son caracteres que se utilizan para realizar operaciones entre variables del mismo tipo o compatibles
- Alcance de una sentencia: El alcance de una sentencia se establece utilizando el tabulado
```python
# PEP 8 Naming Conventions
# Para variables y funciones: Snake Case, todo en minusculas separando cada palabra con un subguion
# Para clases: Pascal Case, como Snake Case pero las primeras letras en mayusculas.
# Para constantes: Como Snake Case pero todo en mayusculas.

# Sentencia simple
import numpy
# Asignación
NOMBRE_CURSO = 'Python'
nombre_curso = 'Silabuz'
# Sentencia compuesta, Función personalizada
def obtener_codigo_curso(param_separador):
  # Sentencia simple
  global nombre_curso
  # Auto-Asignación
  nombre_curso += param_separador + 'Bootcamp'
  # Sentencia simple
  return nombre_curso

# Función predefinida
print(numpy.__version__)
# Función personalizada
print(obtener_codigo_curso('-'), NOMBRE_CURSO)
```
### 2. Conocer los tiempos y las estrategias para trabajar con Python
En todo lenguaje de programación se pueden y deben diferenciar los tiempos para la construcción de código:
- Tiempo de diseño: Cuando intentamos aterrizar el requerimiento y definir el objetivo del código que voy a escribir
- Tiempo de desarrollo: Cuando empezamos a escribir las líneas de código de acuerdo a nuestro diseño
- Tiempo de ejecución: Cuando hacemos correr el código escrito para que se construya en memoria el programa
- Tiempo de depuración: Cuando colocamos instrucciones para intervenir las operaciones que se estan realizando
- Tiempo de pruebas unitarias: Cuando aplicamos casos de prueba para garantizar que nuestro código cumple con el requerimiento

### 3. Manejo de comentarios, constantes, variables, cadenas, funciones, capturar un valor e imprimir en pantalla
Para incluir un comentario en Python utilizamos:
```python
# Esto es un comentario
```
Para incluir una constante en Python utilizamos:
```python
CONSTANTE_PI = 3.1416
```
Para incluir una variable en Python utilizamos:
```python
area_circulo = CONSTANTE_PI * radio * radio
```
Para incluir una cadena en Python utilizamos:
```python
label_respuesta = 'El area del circulo es: ' + str(area_circulo)
```
Para incluir una función en Python utilizamos:
```python
def calcular_area_circulo(param_radio):
```
Para capturar un valor ingresado en pantalla con Python utilizamos:
```python
input('Ingrese el radio del circulo: ', radio)
```
Para imprimir en pantalla con Python utilizamos:
```python
print(calcular_area_circulo(radio))
```

  ![](assets/silabuz-logo.png "Silabuz")
