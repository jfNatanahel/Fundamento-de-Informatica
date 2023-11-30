#Dado el siguiente problema: Dada una lista de N numeros, cargarla en un vector y luego transferir
#los elementos que sean mayores que un numero dado X a otro vector B. Luego ordenar el vector B
#de menor a mayor y mostrar el resultado.

tamaño_lista=int(input("Tamaño de la lista: "))
lista=[None]*tamaño_lista
i=0
while i<tamaño_lista:
    lista[i]=int(input("Elementos lista: "))
    i+=1
print("Lista: ",lista)
x=int(input("Ingresar un numero para crear el vector B dependiendo de ese numero: "))
vector=[None]*tamaño_lista

tamaño_b=0
for i in range(tamaño_lista):
    vector[i]=lista[i]
    if x<vector[i]:
        tamaño_b+=1
print("Vector:",vector)
b=[None]*tamaño_b
for i in range(tamaño_lista):
    bandera=0
    for j in range(tamaño_b):
        if x<vector[i]:
            b[j]=vector[i]

    
print(b)         

