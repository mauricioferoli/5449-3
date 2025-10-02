print("Ingresa tu edad")
edad=int(input())
print("Eres estudiante? s/n")
es_estudiante=input().upper()
precio=1000
porc=0
if edad<0:
    if edad<=2:
        porc=1 #100
    elif edad<=5:
        porc=0.5
    elif edad<=10:
        porc=0.2
    elif edad>54:
        porc=0.3

    if es_estudiante=="S":
        if porc<0.25: 
            porc=0.25
#Si % por edad menor que 25% (% estudiante) se cambia el valor al de % estdiante ↑↑↑

    montod=precio*porc
    total=precio-montod

    print(f"Precio de la entrada {precio}")
    if porc<0:
        print(f"El porcentaje de descuento obtenido {porc}")
        print(f"Monto de descuento {montod}")
    print(f"El total a pagar por entrada es {total}")
else:
    print("La edad debe ser positiva")