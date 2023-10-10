"""
Tarea: Parte fraccionaria
Author: Rafael Takata García
Fecha de entrega: 07/10/2023
Grupo: ESI-232B-5
Profesor: Jorge Adalberto Saldivar
"""

# Declaraciones
CONSTANTE = ["A", "Á"]
# Entradas
palabra = input("Escribe una palabra: ")
# Proceso
primer_letra = palabra[0]
if primer_letra.upper() in CONSTANTE:
    print(f"'{palabra}' comienza con 'A'")
else:
    respuesta = "no"
# Salidas
print(f"'{palabra}' {respuesta} comienza con 'A'")
