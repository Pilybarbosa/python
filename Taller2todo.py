"""sb=500000


for n in range(3):
    nv=0
    while nv<=3:
        nv+=1
        v1=int(input("primera venta "))
        v2=int(input("primera venta "))
        v3=int(input("primera venta "))
        com=int((v1+v2+v3)*0.1)
        print(f"El empleado {n} tiene un sueldo base de {sb} mas las comisiones que son {com}, su suelto total es {sb+com}")
    n+=1  """


"""EJERCICIO 2 """
""" for i in range(1,5):
    compra=int(input("Ingrese el total de la compra"))
    bolita=int(input("Ingrese el numero de la bolita que ha sacado 1.Roja, 2.Amarilla, 3.Blanca"))

    if bolita==1:
        descuento=compra*40/100
        totalC=compra-descuento
        print("El total de su compra es: ",totalC)
        print("El descuento es de: ",descuento)
    elif bolita==2:
        descuentoA=compra*25/100
        totalC=compra-descuento
        print("El total de su compra es: ",totalC)
        print("El descuento es de: ",descuentoA)
    elif bolita==3:
        print("El total de su compra es: ",compra)
        print("No tiene descuento")   """
        
"""EJERCICIO 3 """
    
    
""" aprobado = 0
promedio=0
for i in (0,8,1):
    for p in (0,8,1):
        nota=int(input("Ingrese la nota"))
        promedio=promedio+nota
        
    total=promedio/8
    print("---------------------------------------")

    if total>6:
        aprobado+=1

print("Lo alumnos con derecho a aprobación son", aprobado)
""" 
    

"""EJERCICIO 4
candidato1=0
candidato2=0
candidato3=0
for x in range (0,5,1):
    voto=int(input("escoja el numero del candidato por el cual va a votar 1 miguel 2 sebastian 3 julian"))
    if voto==1:
        candidato1+=1
    elif voto==2:
        candidato2+=1
    elif voto==3:
        candidato3+=1

if candidato1>candidato2 and candidato1>candidato3:
    print("el candidato 1 ha ganado con la cantidad de votos",candidato1)
elif candidato2>candidato1 and candidato2>candidato3:
    print("el candidato 2 ha ganado con la cantidad de votos",candidato2)
elif candidato3>candidato1 and candidato3>candidato2:
    print("el candidato 3 ha ganado con la cantidad de votos",candidato3)"""
                
""" EJERCICIO5
n1=0
n2=0
n3=0
n4=0


for e in range(10):
    n=int(input("Cual fue tu calificacion en el examen de fisica? "))
    if n<50: 
        n1+=1
    elif n>=50 and n<70:
        n2+=1
    elif n>=70 and n<80:
        n3+=1
    elif n>=80:
        n4+=1

print(f"{n1} estudiante obtuvieron una calificación menor a 50")
print(f"{n2} estudiante obtuvieron una calificación entre 50 y 69.")
print(f"{n3} estudiante obtuvieron una calificación entre 70 y 79")
print(f"{n4} estudiante obtuvieron una calificación mayor a 80")
"""