#funciones
#Este es un docstring de modulo
#Vamos a crear varias funciones

"""def saludar():
    
    nombre = input("Digite el nombre: ")
    apellido = input("Digite el apellido: ")
    nombre_completo = f"{nombre.title()} {apellido.title()}"
    print(f"Hola {nombre_completo}!")
    
def saludar_con_param(nombre, apellido):

    print(f"Hola {nombre.title()} {apellido.title()}")
saludar_con_param("Fer", "ROSALES")

def describir_mascota(animal,nombre_mascota):
   
    
    print(f"Tengo un {animal} y su nombre es {nombre_mascota}")

describir_mascota(nombre_mascota="perro",animal="firulais")
describir_mascota("gato","mishito")
describir_mascota(
    input("Digite el tipo de animal: "),
    input("Digite el nombre de la mascota")
)"""

def calculo_impuesto(ventas): 
    """Esta función calcula el valor del impuesto"""
    if ventas < 500:
        tasa = 0.1
    else:
        tasa = 0.25
    return tasa
ventas = 100

print(f"""El valo de la venta fue de {ventas}, la tasa de impuesto
      fue de {calculo_impuesto(ventas)} y el monto por tanto es ${calculo_impuesto(ventas)* ventas:,.2f}""")