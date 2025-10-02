for i in range(1,5): #simular varis ventas
    print(f"VENTA N {i}")
    print("Tipo de Precio")
    print("A -> 80")
    print("B -> 105")
    print("C -> 250")
    tipo=input().upper() # .upper(): TRANSFORMACION DE CARACTERES (Interpretacion del sistema)
    print("Cuantos deseas lleavar?")
    cant=int(input())

    if tipo=="A":
        precio=80
    elif tipo=="B":
        precio=105
    elif tipo=="C":
        precio=250
    else:
        precio=0

    total=precio*cant
    if cant>0:
        if precio>0: #precio mayor que cero, tipo valido
            print(f"Tipo de pantalon {tipo}")
            print(f"Precio: {precio}")
            print(f"Total a pagar: {total}")
        else:
            print("Tipo de pantantalon inavalido")
    else:
        print("La cnatidad debe ser positiva")