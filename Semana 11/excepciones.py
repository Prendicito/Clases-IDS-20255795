"""def calcular_impuesto():
    pass"""


while True:
    try:    
        monto = int(input("Monto a calcular: "))
    except TypeError as te:
        print("Se genera un error: ", te)
    except ValueError as ve:
        print("Es un error de valor.")
    else:
        impuesto = monto + 25
        print(f"El valor del impuesto es de ${impuesto:,.2f}")
        break
    finally:
        print("Hemos terminado la ejecución de esta pregunta.")
        
        


