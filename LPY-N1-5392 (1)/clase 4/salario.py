print("Calculo de salario")
print("Como te llamas?")
nombre=input()
print("Cuanto vandiste este mes?")
monto_v=float(input())
print("Cuanta horas trabajaste?")
horas=int(input())
#procesos
salrio_base=200
comision=monto_v*0.3 #30% del monto de ventas
m_horas=horas*5
deducciones=salrio_base*0.05
salario=salrio_base+comision+m_horas-deducciones
#salidas
print(f"""
Empleado: {nombre}
Salario base: {salrio_base}
Comision por ventas: {comision}
Monto por horas trabajadas: {m_horas}
IVSS: {deducciones}
Salario a percibir: {salario}""")