from Servicios.Proyecto import *
from Monitoreo.logger import *

log=logger()

def showOpcions():
    msg="""
    Tengan una bienvenida.
    ==> Elige una opcion
1. Cargar la Data
2. Generar el reporte
3. Mostar un gráfico
4. Salir
"""
    print(msg)
    opcion=input("Ingrese la opción: ")
    return opcion

def getFunction(opcion):
        if opcion=="1":
            print("Ingrese aquí")
            log.message(f"Realizo la carga de archivo")
            loadData()
        elif opcion =="2":
             log.message(f"Reporte Realizado")
             generateReport()
        elif opcion =="3":
            log.message(f"Se realizo el grafico")
            shOwData()
        elif opcion =="4":
            print("¡Hasta luego! gracias por usar esta opcion")
            return True
        else:
             print("Ingresa opcion valida")

if __name__=='__main__':
    while True:
        opcion=showOpcions()
        if getFunction(opcion)==True:
             break
        #getFunction(opcion)