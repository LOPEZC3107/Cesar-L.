# 4.Realizar un programa que permita saber si un usario puede obtener un tarjeta de credito
# condiciones : ser mayor de 18 años , un ingreso mensual de 1000 soles mensual.
# si cumple con las 2 condiciones imprimir que tipo de tarjeta puede obtener
# si su ingreso mensual es de 1000 hasta 3000 soles es tarjeta de clasica , mayor a ello tarjeta dorada.
Edad=int(input("ingrese su edad: "))
if Edad>= 18:
    ingreso=float(input("Digite su ingreso mensual, moneda soles: "))
    if  ingreso>=1000:
        print("¡Feliciades!, puede obtener una tarjeta de credito")
        if ingreso<=3000:
            print("Con el ingreso obtenido, usted aplica a una tarjeta de credito clasica")
        else: 
            print("su ingreso mensual aplica para una tarjeta dorada")
    else: 
        print("su ingeso mensual es insuficiente")    
else:
    print("No cumple con la edad minima")