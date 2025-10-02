
print("Cuanto vendiste ?")
monto=float(input())
print("Cuantos años tienes?")
edad=int(input())
salario=5000
print("Ingresa tu genero m/f")
genero=input().upper()

if monto>0 and monto<75000:
    porc=0.05
elif  monto>=90000 and monto<200000:
    porc=0.07
elif  monto>=300000 and monto<1000000:
    porc=0.08
elif monto>=1500000:
    porc=0.10
else:
    porc=0.06

if (edad<55 and genero=="F") or (edad<60 and genero=="M"):
    bono=40000
else:
    bono=0

comision=monto*porc
salariof=salario+comision+bono

print(f"""
Salario: {salario}
Vendio: {monto}
% comision: {porc}
Comision: {comision}
Bono: {bono}
Salario a percibir: {salariof}
""")