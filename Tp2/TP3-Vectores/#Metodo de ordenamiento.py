#Dado un vector A[i], ordenadrlo de forma ascendente.
n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
for i in range(n):
    v[i]=int(input("Elementos del vector: "))
for i in range(n):
    for j in range(i+1,n):
        if v[i]>v[j]:
            aux=v[i]
            v[i]=v[j]
            v[j]=aux
print(v)