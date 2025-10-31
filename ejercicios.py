Valores = [[1,3,6],[2,7,4],[6,5,9],[1,10,20]]
mayores = []
for v in Valores:
    for i in v:
        if i>6:
            mayores.append(i)
print(mayores)