# Trabajo con fechas para TPI II de matemáticas y programación

# Parte B:
# Importamos la librería de fechas y horas
from datetime import datetime as fecha_actual

# fechas = {"Nahuel" : 1977, "Martín" : 2000,"José" : 1977,"Thiago" : 2004,"Franco" : 2005}

# Pedimos los nombres de los integrantes del grupo
# Ingresamos los 5 años y guardamos en una lista
def obtener_nombres_fechas():
    fechas = {}
    for _ in range(5):
        nombre = input("Ingresa un nombre del integrante del grupo: ")
        fechas[nombre] = input("Indique el año de nacimiento del integrante recién ingresado: ")
    return fechas
# Grupo de nacidos post año 2000
def grupo_z(fechas):
    grupo_Z = {}
    for fecha in fechas:
        anio = int(fechas[fecha])
        if anio > 2000:
            grupo_Z[fecha] = fechas[fecha]
    return grupo_Z

# Definimos si el año ingresado es bisiesto
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0): 
        return True
    else:
        return False
# Grupo año bisiesto
def grupo_bisiesto(fechas):
    grupo_especial = {}
    for fecha in fechas:
        anio = int(fechas[fecha])
        if es_bisiesto(anio):
            grupo_especial[fecha] = fechas[fecha]
    return grupo_especial
# Grupo años pares
def grupo_pares(fechas):
    grupo_par = {}
    for fecha in fechas:
        anio = int(fechas[fecha])
        if anio % 2 == 0:
            grupo_par[fecha] = fechas[fecha]
    return grupo_par
# Grupo años impares
def grupo_impares(fechas):
    grupo_impar = {}
    for fecha in fechas:
        anio = int(fechas[fecha])
        if anio % 2 != 0:
            grupo_impar[fecha] = fechas[fecha]
    return grupo_impar
# Grupo de las edades de los integrantes del grupo
def grupo_edades(fechas):
    anio_actual = fecha_actual.now().year
    grupo_edades = {}
    for fecha in fechas:
        anio = int(fechas[fecha])
        grupo_edades[fecha] = anio_actual - anio
    return grupo_edades
# Cargamos los nombres y las fechas de los integrantes del grupo
fechas = obtener_nombres_fechas()

# Revisamos las funciones
print(f"Grupo fechas: {fechas}")
print(f"Grupo Z: {grupo_z(fechas)}")
print(f"Grupo bisiesto: {grupo_bisiesto(fechas)}")
print(f"Grupo pares: {grupo_pares(fechas)}")
print(f"Grupo impares: {grupo_impares(fechas)}")
print(f"Grupo edades: {grupo_edades(fechas)}")

# anio_actual = date.now().year
# grupo_z = []
# bisiestos = []
# pares = 0
# impares = 0
# cartesiano = []

# for nombre, anio in fechas.items():
#     if anio > 2000:
#         grupo_z.append(nombre)
#     if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#         bisiestos.append(nombre)
#     if anio % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     edad = anio_actual - anio
#     cartesiano.append((anio, edad))