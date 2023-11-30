tamaño_vector=int(input("Ingresar el tamaño del vector: "))
v=[None]*tamaño_vector
for i in range(tamaño_vector):
    v[i]=int(input("Elementos vector: "))
elemento_buscar=int(input("Elemento a Buscar: "))
incio=0
fin=tamaño_vector-1
posicion=-1 #Saber la posicion en que se encuentra. No es necesario
bandera=0
while incio<=fin and bandera==0:
    medio=(incio+fin)//2
    if v[medio]==elemento_buscar:
        bandera=1
        posicion=medio
    else:
        if v[medio]<elemento_buscar:
            incio=medio+1
        else:
            fin=medio-1
if bandera==1:
    print(f"Elemento {elemento_buscar} encontrado en la posicion {posicion}")
else:
    print("Elemento no encontrado en el vector")