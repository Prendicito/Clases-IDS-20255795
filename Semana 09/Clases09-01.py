#Diccionarios
#vamos a crear un diccionario
"""mi_gato =  {"nombre": "pelusa", 
            "edad": 3,
            "personalidad": "simpatico"} # [Nombre,edad, caracteristica]
            #clave : valor
abys_cat = {"personalidad": "simpatico",
            "nombre": "pelusa",
            "edad": 3}
    """


#Diccionarios 2 
"""birthdays = {"Alice": "Apr1",
             "Bob":"Dec 12",
             "Carol": "Mar4"}

birthdays["Carol"] = "Abr 21"
birthdays["Fer"] = "May 3"
del birthdays["Bob"]
print(birthdays)
"""
#Diccionarios 3
Semana = {}
Semana["uno"] = "Lunes"
Semana["dos"] = "Martes"
Semana["tres"] = "Miercoles"
Semana["cuatro"] = "Jueves"
Semana["cinco"] = "Viernes"

print(Semana.values())
for v, k in Semana.items():
    print(f"{v}: {k}")