#Dado el siguiente problema: Dada una lista de N numeros, cargarla en un vector y luego transferir
#los elementos que sean mayores que un numero dado X a otro vector B. Luego ordenar el vector B
#de menor a mayor y mostrar el resultado.

#Cargamos la lista.
tamaño_lista=int(input("Tamaño de la lista: "))
lista=[None]*tamaño_lista
i=0
while i<tamaño_lista:
    lista[i]=int(input("Elementos lista: "))
    i+=1
print("Lista: ",lista)
x=int(input("Ingresar un numero para crear el vector B dependiendo de ese numero: "))

#Cargamos el Vector A
A=[None]*tamaño_lista
tamaño_b=0 #Dimension del vector B
for i in range(tamaño_lista):
    A[i]=lista[i] #Duplicamos la lista.
    if x<A[i]:
        tamaño_b+=1
print("Vector:",A)

#Cargamos el Vector B
b=[None]*tamaño_b
indice=0 
for i in range(tamaño_lista): #Recorro el vector A
    if x<A[i]:
        b[indice]=A|[i]
        indice+=1
print("Vector B con los elementos mayores a X",b)

#Ordenamiento del Vector B: Menor a mayor.
for i in range(tamaño_b):
    for j in range(i+1,tamaño_b):
        if b[i]>b[j]:
            aux=b[i]
            b[i]=b[j]
            b[j]=aux
print("Vector ordenado de menor a mayor",b)    

