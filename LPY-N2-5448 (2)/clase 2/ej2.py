import random
precio=random.randint(1000,100000)
print(f"El producto cuesta {precio}")
print("Cuantos deseas llevar?")
cantidad=int(input("-> "))
subtotal=precio*cantidad
print("Saldo")
saldo=random.randint(0,150000)

if saldo<precio:
    print("Saldo insuficiente")

if subtotal>50000:
    porc=0.05
else:
    porc=0.02

montod=subtotal*porc
total=subtotal-montod

if cantidad>0:
    print(f"Subtotal a pagar {subtotal}")
    print(f"% de descuento {porc}")
    print(f"Monto descuento {montod}")
    print(f"Total a pagar {total}")
else:
    print("La cantidad minima para comprar debe ser 1")