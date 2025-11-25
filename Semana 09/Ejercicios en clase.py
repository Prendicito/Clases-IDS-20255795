
codigos = []
nombres = []
correos = []
telefonos = []

for codigo,nombre,correo,telefono in zip(codigos,nombres,correos,telefonos):
    print(codigo,nombre,correo,telefono)
#menu de productos
código = []
nombre = [] 
categoría = []
precio = []

#menu 
print("""
1.	Mostrar productos
2.	Agregar producto
3.	Registrar nuevo cliente
4.	Mostrar clientes
5.	Registrar pedido
6.	Mostrar pedidos del día
7.	Mostrar categorías disponibles
8.	Salir
""")
