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