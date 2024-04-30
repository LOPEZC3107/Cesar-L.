#1. Crear un menu iterativo con las siguientes opciones
#2. opcion 1 'Saludar' , pedir datos personales
#3. opcion 2 Realizar una operacion matematica pedir 2 numeros
#4. opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
#5. opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista
#6. opcion 5 mostrar listado de alumnos aprobados
#7. opcion 6 mostrar listado de alumnos desaprobados
#8. opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
#9. opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
#10. opcion 9 Salir.

def saludar():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    print(f"Hola, {nombre}! Tienes {edad} años.")

def operacion_matematica():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print(f"La suma de {num1} y {num2} es {num1 + num2}")
alumnos = []

def agregar_alumno():
    nombre = input("Nombre del alumno: ")
    edad = input("Edad del alumno: ")
    correo = input("Correo del alumno: ")
    cursos = []
    while True:
        curso = input("Nombre del curso (deja en blanco para terminar): ")
        if not curso:
            break
        notas = []
        while True:
            entrada = input("Ingresa una nota (deja en blanco para terminar): ")
            if entrada == '':
                break
            nota = float(entrada)
            if 0 <= nota <= 20:
                notas.append(nota)
            else:
                print("Nota inválida. Ingresa una nota de 0 a 20.")
        cursos.append({'nombre_curso': curso, 'notas': notas})
    alumnos.append({'nombre': nombre, 'edad': edad, 'correo': correo, 'cursos': cursos})

def calcular_promedios():
    for alumno in alumnos:
        for curso in alumno['cursos']:
            if len(curso['notas']) > 0:
                promedio = sum(curso['notas']) / len(curso['notas'])
                curso['promedio'] = promedio

def mostrar_aprobados():
    calcular_promedios()
    print("Alumnos aprobados:")
    for alumno in alumnos:
        for curso in alumno['cursos']:
            if curso.get('promedio', 0) >= 14:
                print(alumno['nombre'], curso['nombre_curso'], curso['promedio'])

def mostrar_desaprobados():
    calcular_promedios()
    print("Alumnos desaprobados:")
    for alumno in alumnos:
        for curso in alumno['cursos']:
            if curso.get('promedio', 0) < 14:
                print(alumno['nombre'], curso['nombre_curso'], curso['promedio'])

def rango_grande():
    numeros = []
    for num in range(0, 10**10, 210):
        numeros.append(num)
    print(f"Tamaño de la lista: {len(numeros)}")

def maximo_de_dos():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print(f"El mayor es: {max(num1, num2)}")

opcion = 0
while opcion != 9:
    print("""Menu:
    DIGITE LA OPCIÓN DESEADA
    1. Ingresar datos personales
    2. Realizar una operación matemática
    3. Agregar alumno a lista
    4. Calcular promedio de notas y agregar a lista
    5. Mostrar listado de alumnos aprobados (> 14)
    6. Mostrar listado de alumnos desaprobados (< 14)
    7. Rango grande
    8. Mayor de dos números
    9. Salir del menu""")
    opcion = int(input("Elige una opción>> "))

    if opcion == 1:
        saludar()
    elif opcion == 2:
        operacion_matematica()
    elif opcion == 3:
        agregar_alumno()
    elif opcion == 4:
        calcular_promedios()
    elif opcion == 5:
        mostrar_aprobados()
    elif opcion == 6:
        mostrar_desaprobados()
    elif opcion == 7:
        rango_grande()
    elif opcion == 8:
        maximo_de_dos()
    elif opcion == 9:
        print("Saliendo del programa...")
    else:
        print("Opción inválida, intentar de nuevo.")

