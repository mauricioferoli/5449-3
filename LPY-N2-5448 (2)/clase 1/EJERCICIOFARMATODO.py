import random
print("Cómo se llama?")
nombre=input() #entrada
print("Ingrese el número de cédula?")
cedula=input()
print("Cómo se llama el producto?")
producto=input()
precio=random.randint(100,1500)
print(f"Precio del producto? {precio}")
print("Cuál es el Saldo disponible?")
saldo_disponible=float(input())
iva=precio*0.16
total=precio+iva
#calcular el IVA sobre el precio 16%
if total<=saldo_disponible: #saldo_disponible>=total
    print("-"*30)
    print("Factura Nro 001")
    print(f"Cliente: {nombre}")
    print(f"Cédula: {cedula}")
    print(f"Producto: {producto} - Precio: {precio}$")
    print(f"IVA {iva}")
    print(f"Total a pagar {total}")
    print(f"Saldo disponible: {saldo}")
    print("-"*30)
if total>saldo_disponible: #saldo_disponible<=total
    print("-"*30)
    print("No se puede realizar la vanta")
    print("-"*30)