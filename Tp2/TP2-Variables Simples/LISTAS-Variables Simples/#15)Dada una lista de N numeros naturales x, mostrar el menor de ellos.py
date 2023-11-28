tamaño_lista=int(input("Ingresar el tamaño de la lista: "))
x=int(input("Ingresar el primer numero de la lista: "))
menor=x
i=1
while i<tamaño_lista:
    x1=int(input("Ingresar numero de la lista: "))
    if menor >x1:
        menor=x1
    i=i+1
print("El menor de la lista es: ",menor)