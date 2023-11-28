#menor a mayor
tamaño_lista=int(input("Ingresar el tamaño de la lista: "))
primer_numero=int(input("Ingresar el primer numero de la lista: "))
i=0
bandera=0
while i<tamaño_lista and bandera==0:
    x=int(input("Ingresar numeros de la lista: "))
    if primer_numero<x:
        primer_numero=x
    else:
        bandera=1
    i=i+1
if bandera==0:
    print("La lista viene ordenada ascendentemente")
else:
    print("La lista NO viene ordenada ascendentemente")