usuario = "alvin"
monto_hope = 1236
cantidad_alumnos = 79
media_edad = 18.232456
inversion_evento = -12139.1212

print(type(cantidad_alumnos))
print(type(media_edad))

print(type(cantidad_alumnos) is int)
print(type(media_edad) is int)
print("el usuario es" , usuario , "y tiene" , cantidad_alumnos , "pajaritos en su aula")
print("y la edad promedio es de" , media_edad)

print(f"el usuario es {usuario}")
print (f"y con sus {cantidad_alumnos - 4} pajaritos ha recolectado ${monto_hope} para la funcion Hope")
print(f"y la totalidad de gastos fue de ${abs(inversion_evento):,.2f}")
print(f"la media de edad de los alumnos es de{media_edad: .2f} años")
print(type(usuario))