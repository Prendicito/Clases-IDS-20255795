def registro_profesores(nombre, apellido, **materias):
    """Crear un registro de profesores, usando Kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t {materias} ")
    
registro_profesores(
    "Alvin",
    "Portillo",
    Ciclo1 = ["BD1","IIJ","A&F"],
    Ciclo2 = ["DA1", "FR2", "SINE"]
)
    
