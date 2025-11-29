#Este modulo contendrá las funciones
def ordenar_pizza(*ingrediente):
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza de: ")
    for i in ingrediente:
        print(f"-{i}")



def registro_profesores(nombre, apellido, **materias):
    """Crear un registro de profesores, usando Kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t {materias} ")

def saludar_usuarios(nombres):
    """saludará usuarios"""
    for nombre in nombres:
        print(f"Hola, {nombre.capitalize()}")
        
