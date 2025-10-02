print("Bienvenido a la tienda JUMP-ADIDAS")
#Entradas
print("Como te llamas?")
nombre=input()
modelo=input("Cual modelo deseas?")
talla=int(input("Que talla eres ->"))
#Procesos
precio=100
descuento=precio*0.25 #25% de descuento
total=precio-descuento #precio*0.75
#Salidas
print(f"""
Cliente: {nombre}
Modelo: {modelo}
Talla: {talla}
Descuento obtenido: {descuento}
Total a pagar: {total}""")