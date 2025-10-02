for i in range(2000,2026,2):    #valor inicial,valor final,paso
    print(f"{i}")

for i in range(2026,2000,-2):    #mismo ciclo pero descendente
    print(f"{i}")

for i in range(2000,2026,2):    #msotrando años bisiestos 
    if i%4==0:
        print(f"{i}")