print("bienvenidos al calculo de sueldos")
print("-----------------------------------------")
horas = input("ingrese la cantidad de horas trabajadas por dia: ")
horas = int(horas)
dias = input("ingrese la cantidad de dias trabajados: ")
dias = int(dias)
sueldo = dias * horas
precio = input("ingrese el valor por hora: ")
precio = float(precio)
salario = sueldo * precio
print("la cantidad de horas trabajadas en el mes es de: ")
print(sueldo)
print("el salario generado este mes es de: ")
print(salario)