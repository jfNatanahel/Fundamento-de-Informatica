#Dada una lista de N numeros naturales, cargalos en un vector y luego agrupar hacia la dercha todos
#los numeros pares y havia la izquierda los impares. Usar si fuera necesario un vector auxiliar.
tamaño_lista=int(input("Ingresar el tamaño de la lista: "))
lista=[None]*tamaño_lista
for i in range(tamaño_lista):
    lista[i]=int(input("Elementos lista: "))
print("Lista cargada",lista)

#Cargarlos en un vector A
A=[None]*tamaño_lista
for i in range(tamaño_lista):
    A[i]=lista[i]
print("Vector A cargado",A)

#Agrupacion
indice_derecha=tamaño_lista-1
indice_izquierda=0
vector_auxiliar=[None]*tamaño_lista
for i in range(tamaño_lista):
    num=A[i]
    if num%2==0:
        vector_auxiliar[indice_derecha]=num
        indice_derecha-=1
    else:
        vector_auxiliar[indice_izquierda]=num
        indice_izquierda+=1
print("La lista organida por: Izquierda IMPARES y Derecha Pares:",vector_auxiliar)