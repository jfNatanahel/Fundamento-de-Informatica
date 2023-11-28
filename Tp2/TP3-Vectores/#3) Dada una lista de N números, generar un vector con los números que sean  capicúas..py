n=int(input("Ingresar el tamaño de la lista: "))
mi_lista=[]
i=0
while i<n:
    elemento=int(input("Ingresar elementos de la lista: "))
    mi_lista=mi_lista+[elemento]
    i+=1
print("Lista es: ",mi_lista)
i=0
v_aux=[]
while i<n:
    numero=mi_lista[i]
    original=numero
    y=0
    while numero>0:
        r=numero%10
        y=y*10+r
        numero=numero//10
    if y==original:
        v_aux=v_aux+[original]
    i=i+1
print("El vector con los numeros capicua es: ",v_aux)        