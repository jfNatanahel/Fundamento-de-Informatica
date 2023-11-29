M=int(input("Ingresar el tamaño de la lista: "))
i=1
while i<M:
    A=int(input("Ingresar el elemento de la lista: "))
    i=i+1
print("Lista A",A)
i=1
while i<M:
    copia=A
    i=i+1
print("Copia de la lista A",A)
#for i in range(M):
#    for j in range(i+1,M):
#        if A[i]<A[j]:
#            aux=A[i]
#            A[i]=A[j]
#            A[j]=aux
#print("Ordenado de menor a mayor",A)
