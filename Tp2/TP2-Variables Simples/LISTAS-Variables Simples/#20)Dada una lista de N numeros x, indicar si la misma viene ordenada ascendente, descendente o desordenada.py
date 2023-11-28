tamaño_lista=int(input("Ingresar el tamaño de la lista: "))
primer_numero=int(input("Ingresar el primer numero de la lista: "))
i=1
bandera_asc=0
bandera_desc=0
bandera_desor=0
while i<tamaño_lista:
    x=int(input("Ingresar numeros de la lista: "))
    if primer_numero<x: #Ascendente
        bandera_asc=0
    else:
        bandera_asc=1
    if primer_numero>x: #Descendente
        bandera_desc=0
    else:
        bandera_desc=1
    primer_numero=x
    i=i+1 #Desordenada
if bandera_asc==1 and bandera_desc==1:
    print("La lista viene DESORDENADA")
else:
    if bandera_asc==0:
        print("La lista viene ordenada ASCENDENTE")
    else:
        print("La lista viene ordenada DESCENDENTE")