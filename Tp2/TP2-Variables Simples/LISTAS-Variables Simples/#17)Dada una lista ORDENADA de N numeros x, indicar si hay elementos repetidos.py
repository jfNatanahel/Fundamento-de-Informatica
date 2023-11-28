tamaño_lista=int(input("Ingresar el tamaño de la lista: "))
i=1
x1=int(input("Ingresar el primer numero de la lista ORDENADA: "))
bandera=0
while i<=tamaño_lista and bandera==0:
    x=int(input("Ingresar numeros ORDENADOS: "))
    if x1==x:
        bandera=1
    else:
        x1=x
    i=i+1
if bandera==1:
    print("Hay elementos repetidos")
else:
    print("No hay elementos repetidos")
