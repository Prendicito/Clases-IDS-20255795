def validacion_dui():
    numero_condiciones = 0 
    dui = str(input("Ingrese su dui: "))

    if len(dui) == 10:
        numero_condiciones += 1
    if dui.count("-") == 1:
        numero_condiciones += 1

    print(f"Cumple {numero_condiciones} condiciones.")
validacion_dui()
        
        

   