#Dada una lista A de M numeros, ordenarla de menor a mayor, y luego informar cuantos elementos
#se encontraban originalmente en su posicion correcta. Consejo: Conservar una copia de la lista
#original antes de ordenarla.

#Carga de la lista A, tamaño M.
M=int(input("Ingresar el tamaño de la lista: "))
A=[None]*M
i=0
while i<M:
    A[i]=int(input("Ingresar el elemento de la lista: "))
    i=i+1
print("Lista A",A)

#Copia de la lista y cuantos elementos se encontraban en su posicion correcta.
i=0
contador_posicion_correcta=0
copia=[None]*M
while i<M:
    copia[i]=A[i]
    if copia[i]==i:
        contador_posicion_correcta+=1
    i=i+1
print("Copia de la lista A",A)

#Ordenar de menor a mayor.
for i in range(M):
    for j in range(i+1,M):
        if A[i]>A[j]:
            aux=A[i]
            A[i]=A[j]
            A[j]=aux
print("Ordenado de menor a mayor",A)
print("Elementos se encontraban originalmente en su posicion correcta:",contador_posicion_correcta)