#Cargar una lista
n=int(input("Ingresar el tamaño de la lista: "))
x=int(input("Ingresar el primer numero de la lista: "))
mayor=x
i=1
while i<n:
    x1=int(input("Ingresar un numero de la lista: "))
    if mayor<x1:
        mayor=x1
    i=i+1
print("El mayor es:",mayor)