Monto = float(input("Digite el monto: "))
tipo = input("Tipo(local/internacional): ").lower()
if tipo == "local":
    if Monto > 100:
        imp = 0.07
    elif Monto > 75:
        imp = 0.05
    else:
        imp = 0
elif tipo == "internacional":
        if Monto > 100:
            imp = 0.12
        elif Monto > 75:
            imp = 0.09
        else:
            imp = 0
else: 
    print("Ese tipo no existe")
print(f"El tipo {tipo} con monto {Monto:,.2f}")
print(f"paga un impuesto de ${Monto*imp:,.2f}")
