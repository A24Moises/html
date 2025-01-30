"""
for i in range(1, 50):
    if i % 5 == 0 and i % 7 == 0:
       print(f"{i} es el divisor entre 5 y 7")
        break
"""
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
"""
"""
entrada = int(input("Escribe un número entero: "))
print()

lista = []
while entrada > 1:
    lista.append(entrada)
    print("Número ingresado:", lista)
    print("----------")
#--------------------------Pares---------------------------------------    
    lista.extend([item for item in range(1, entrada) if item % 2 == 0])
    lista.sort()
    print("Lista de números pares que hay de 1 a",entrada,":",lista)
    print()
#--------------------Media de los numeros Pares-------------------------   
    suma=0
    for num in lista:
        suma+=num
        media=int(suma / len(lista))
    print("La media de todos los numeros es:", media)
    print("----------")
#--------------------------Impares--------------------------------------    
    lista.clear()
    lista.append(entrada)
    lista.extend([item for item in range(1, entrada) if item % 2 == 1])
    lista.sort()
    print("Lista de números impares que hay de 1 a",entrada,":",lista)
    print()
#---------------------Suma de todos los numeros-------------------------
    lista.clear()
    lista.append(entrada)
    lista.extend([item for item in range(1, entrada)])
    lista.sort()
    suma=0
    for num in lista:
        suma+=num
    print("La suma de todos los numeros es:", suma)
    print("----------")
    break
"""
"""
def opPotencia (base,exponente):
    if exponente == 0:
        return 1
    return base * opPotencia(base, exponente -1)

def main():
    print()
    print("Calcula la potencia de un número")
    print("----------")
    base = int(input("Escribe la base: "))
    print()
    exponente = int(input("Escribe el exponente: "))
    potencia = opPotencia(base,exponente)
    print("----------")
    print(f"{base} elevado a {exponente} vale {potencia}")
    print("----------")

main()
"""
def buscar(lista: List, objetivo)

def main():
    entrada= input("Ingresa valores, se agregaran a una lista, pueden ser letras o numeros: ")
    valores= entrada.split()
    valores_ordenados=sorted(valores, key=str)

    lista_copia=valores.copy()

    print(valores_ordenados)

main()