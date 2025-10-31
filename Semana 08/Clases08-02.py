"""ejecucion = True

while ejecucion:
    opcion = input("Continuamos ejecutando el menu? Y/N:")
    if opcion.lower() == "n":
        ejecucion = False
    elif opcion.lower() == "y":
        print("Ok,sigamos.")
    else:
        print("La opcion no es valida.")
        
print("Gracias por utilizar nuestro sistema!!!")"""

#Sistema de registro de alumnos con "for"
"""lista_alumnos = []
cantidad = int(input("Cuanto alumnos va a ingresar?: "))
for i in range(cantidad):
    alumno = input("Digite nombre del pajarito:")
    lista_alumnos.append(alumno)

alumnos = len(lista_alumnos)
print(f"La cantidad de alumnos es: {alumnos}")"""

#aqui vamos a hacerlo con While
lista_alumnos = []
print("Bienvenido a nuestro sistema de control de Alumnos.")
menu_activo = True


while menu_activo:
    opcion = input("Elija la opcion (1: Ingresar alumnos)(2:Salir)(3:Modificar)(4:Borrar):")
    if opcion == "1":
        alumno = input("Nombre de alumno a agregar: ")
        lista_alumnos.append(alumno)
    elif opcion == "2":
        menu_activo = False
    elif opcion == "3":
        i = int(input("Digite la posicion del alumno que quiere cambiar:"))
        n = input("Ingrese el nombre del nuevo alumno: ")
        lista_alumnos[i-1] = n
    elif opcion == "4":
        if len(lista_alumnos) == 0:
            print("No tiene alumnos ingresados todavia")
        else:
            borrado = lista_alumnos.pop(int(input("Ingrese el numero de alumno al que quiere borrar:")))
            print(f"Usted mato a {borrado-1}")
    
print("soltame")
