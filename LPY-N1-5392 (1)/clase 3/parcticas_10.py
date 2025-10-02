import random

print("-"*40)
print("Compra de Dolares")
cantidad=random.randint(10,100)
tasa_binance=148.25
tasa_bcv=220.10
total_bcv=cantidad*tasa_bcv
#NOTAS:↑↑↑ esto y print("Si es tasa BCV...") cumplen la misma funcion ↑↑↑
total_b=cantidad*tasa_binance
#NOTAS:↑↑↑ esto y print("Si es tasa Binance...") cumplen la misma funcion ↑↑↑
diferencia_totales=total_bcv-total_b

print("▬"*40)
print(f"Para comprar {cantidad} dolar")
print("Si es tasa BCV debes cancelar",cantidad*tasa_bcv)
print("Si es tasa Binance debes",cantidad*tasa_binance)
#calcular la diferencia del monto se las dos tasas

print("Diferencia entre ambas totales", round(diferencia_totales))
#NOTAS:↑↑↑ esto necesitara de "total_bcv" y "total_b" ya que: ↓
#      diferencia_totales=total_bcv-total_b             ←  ←  ←
print("-"*40)