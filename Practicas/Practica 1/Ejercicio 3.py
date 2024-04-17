# 3. Realice un programa que calcule la suma de los numeros hasta el valor ingresado.
# Ejemplo : Si ingresa 5 se tendra que calcular 1+2+3+4+5
Number= int(input("ingrese la cantidad de numeros a sumar "))
suma=0
for i in range (1, Number + 1):
    suma += i
print("la suma de los numeros hasta", Number, "es: ", suma)