total = 0
while True:
    velocidad = input("Ingrese velocidad: ")
    velocidad = int(velocidad)
    if velocidad >= 120 and velocidad < 200:
        print("Usted ha exedido la velocidad máxima permitida")
        total = total + 3000
    elif velocidad >= 200:
        print("Usted se encuentra en super exceso de velocidad")
        total = total + 6000
    elif velocidad < 120:
        print("Velocidad permitida")
    print("El total de las multas es: " , total)