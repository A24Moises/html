#for i in range(1, 50):
#    if i % 5 == 0 and i % 7 == 0:
#       print(f"{i} es el divisor entre 5 y 7")
#        break
"""
suma = 0
while True:
    entrada = input("Introduce un numero: ")
    if entrada.isdigit():
        entrada = int(entrada)
        break
    else:
        print("Eso no es un número entero válido. Por favor, intenta de nuevo.")
        
for i in range(1, entrada + 1):
    suma += i
print("La suma es:", suma)
"""   
def totalSeg(min: int, seg: int):
    totalSeg =(min * 60) + seg
    return totalSeg

print("--------------------------------------------------------")
print("-------------------Registro Horario---------------------")
print("--------------------------------------------------------")
print()

entradaH = int(input("Introduce las horas entre 1 y 12: "))
if entradaH < 1 or entradaH > 12:
    print("Las horas deben estar entre 1 y 12.")
    entradaH = int(input("Introduce las horas nuevamente: "))
    print()

entradaMin = int(input("Introduce los minutos entre 0 y 59: "))
if entradaMin < 0 or entradaMin >= 60:
    print("Los minutos deben estar entre 0 y 59.")
    entradaMin = int(input("Introduce los minutos nuevamente: "))
    print()

entradaSeg = int(input("Introduce los segundos entre 0 y 59: "))
if entradaSeg < 0 or entradaSeg >= 60:
    print("Los segundos deben estar entre 0 y 59.")
    entradaSeg = int(input("Introduce los segundos nuevamente: "))
    print()

entradaSeparador = input("Introduce el separador (por defecto ':'): ")
if entradaSeparador == "":
    entradaSeparador = ":"

horaFormato = f"{entradaH:02d}"
minFormato = f"{entradaMin:02d}"
segFormato = f"{entradaSeg:02d}"

print("--------------------------------------------------------")
print("Formato actual:", horaFormato + entradaSeparador + minFormato + entradaSeparador + segFormato)
print("--------------------------------------------------------")

print()
cambioSeparador = input("Introduce el nuevo separador: ")
if cambioSeparador == "":
    cambioSeparador = input("Ningun caracter registrado, introduce el nuevo separador: ")

print()
print("--------------------------------------------------------")
print("Nuevo formato:", horaFormato + cambioSeparador + minFormato + cambioSeparador + segFormato)
print("--------------------------------------------------------")
print()

print("Segundos a mayores de la hora:")
print("--------------------------------------------------------")
print("La cantidad total de segundos que pasan de la hora introducida son:", totalSeg(entradaMin, entradaSeg), "seg")
print("--------------------------------------------------------")
print()

