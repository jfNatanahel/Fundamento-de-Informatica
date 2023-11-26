tamaño_lista=int(input("Ingresar el tamaño de la lista: "))
i=1
s=0
while i<=tamaño_lista:
    x=int(input("Ingresar elementos de la lista: "))
    s=s+x
    i=i+1
promedio=s//tamaño_lista
print("El promedio de la lista es: ",promedio)