print("Tienes medio de transporte")
respuesta=input()

if respuesta.lower()=="si":
    print("puedes ir a la fiesta!")

if respuesta.upper()=="NO":
    print("No puedes ir a la fiesta!")

#entradas
print("Ingresa tus notas")
n1=float(input("Nota 1-> "))
n2=float(input("Nota 2-> "))
n3=float(input("Nota 3-> "))
#alt +shift + flecha hacia abajo
promedio=(n1+n2+n3)/3
print(f"Tu promedio es {round(promedio,1)}")

if promedio>15:
    print("Aprobado")
else:
    if promedio<10:
        print("Esfuerzate mas")
    else:
        if promedio<15:
            print("Esfuerzate un poco mas")
        else:
            print("Reprobado")

#3)
import random
saldo_disponible=random.randint(100,1000)
monto_caja=input()
if saldo_disponible>=monto_caja:
    print("Puede cancelar")
if saldo_disponible<monto_caja:
    print("No puede cancelar")
#4)
alumnos_inscritos=random.randint(0,14)
if alumnos_inscritos>=8:
    print("Si")
if alumnos_inscritos<=8:
    print("No")
#6
entradas=random.randint(0,9)
if entradas>=4:
    print("Si")
if entradas<=4:
    print("No")