"""palabra = "Fortnite"
lista = [10,11,12,13,14]
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
#for m in palabra:
    #print(m)
for i in dias[3]:
    print(".")

Valores = [[1,3,6],[2,7,4],[6,5,9],[1,10,20]]
mayores = []
for v in Valores:
    for i in v:
        if i>6:
            mayores.append(i)
print(mayores)"""
gasto = 0
presupuesto = 1000
while gasto <= presupuesto:
    compra = int(input("Monto a comprar: "))
    gasto += compra
gasto -= compra
print("Ha llegado al limite.")
print(f"gasto {gasto}")