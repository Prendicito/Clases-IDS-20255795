#Crear una lista con 5 dias de la semana

Dias_de_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
Lunes = int(input("Ingrese el numero de kills del dia: "))
Martes =int(input("Ingrese el numero de kills del dia: "))
Miercoles = int(input("Ingrese el numero de kills del dia: "))
Jueves = int(input("Ingrese el numero de kills del dia: "))
Viernes =int(input("Ingrese el numero de kills del dia: "))
Dias_de_semana[0] = Lunes
Dias_de_semana[1] = Martes
Dias_de_semana[2] = Miercoles
Dias_de_semana[3] = Jueves
Dias_de_semana[4] = Viernes

print(Dias_de_semana)
print(f"La produccion de la semana fue: {Lunes+Martes+Miercoles+Jueves+Viernes}")
