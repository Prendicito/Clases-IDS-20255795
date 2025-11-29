def describir_mascota(nombre_mascota: str,tipo_animal:str= "perro"):
    print(f"Mi mascota se llama {nombre_mascota.capitalize()}")
    print(f"y es un {tipo_animal}")
    

#describir_mascota("keitdapro", "siperodejaalniño")

#saludar_usuarios(usuarios)

def ordenar_pizza(*ingrediente):
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza de: ")
    for i in ingrediente:
        print(f"-{i}")
ordenar_pizza("queso", "jamon", "piña", "fortnite")
