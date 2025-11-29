import modulo_datos as dat


def registrar_estudiantes():
    """Esta funcion validara y registrara estudiantes."""
    
    while True:
        carnet_i = input("Ingrese su numero de carnet: ")
        largo_carnet = len(carnet_i)
        existe = False
        for estu in dat.estudiantes:
            if estu["Carnet"] == carnet_i:
                existe = True
        if largo_carnet >= 6 and largo_carnet<= 10 and existe == False:
            print("Vamos bien")
            break
        else:
            print("El carnet no tiene el largo requerido, o existe")
            
            
    while True:
        nombre_i = input("Digite su nombre: ")
        if len(nombre_i) > 1:
            break
        else:
            print("El largo del apellido no es permitido.")
          
            
    while True:
        apellido_i = input("Digite su apellido: ")
        if len(apellido_i) > 1:
            break
        else: 
            print("El largo del apellido no es permitido.")
    
    dat.estudiantes.append({
        "Carnet": carnet_i,
        "Nombre": nombre_i,
        "Apellido":apellido_i,
        })

def inscribir_en_curso():
    alo = True
    while alo:
        carnet = input("Ingrese su carnet(Si desea salir al menu principal, escriba: salir): ").lower()
        if carnet == "salir":
            break
        for estudian in dat.estudiantes:
            if carnet == estudian["Carnet"]:
                while True:
                    curso = input("""Escriba el codigo del curso que desea inscribir:
        "PY": "Python Basico"
        "JS": "Javascript para principiantes"
        "BD": "Introduccion a base de datos"
        "SE" : "Seguridad en Entornos Digitales" """).upper()
        
                    if curso not in dat.cursos:
                        print("Esa materia no existe.")
                
                    
                    elif curso in dat.cursos:
                        if (carnet, curso) in dat.inscripciones:
                            print("El estudiante ya está inscrito en ese curso.")
                        else:
                            dat.inscripciones.append((carnet, curso))
                            print(f"El estudiante se ha registrado con exito")
                            alo = False
                            break
                                               
            else:
                print("Ese numero de carnet no está registrado")
                        
def generar_reporte():
    if len(dat.inscripciones) == 0:
        print("No hay inscripciones realizadas todavia.")
    
                            
                        
                        
         

       
            
        
             
