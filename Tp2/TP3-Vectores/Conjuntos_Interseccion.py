#Interseccion: C debe contener solo los elementos que pertenecen a ambos conjuntos.
n=int(input("Ingresar el tamaño del vector A: "))
A=[None]*n
for i in range(n):
    A[i]=int(input("Elementos A: "))
m=int(input("Ingresar el tamaño del vector B: "))
B=[None]*m
for j in range(m):
    B[j]=int(input("Elementos B: "))
bandera=0
c=[None]*(n+m)
t=0
for i in range(n):
    for j in range(m):
        if A[i]==B[j]:
            bandera=1
    if bandera==1:
        t=t+1
        c[t-1]=A[i]
        bandera=0
        
print("Interseccion entre A y B")
for i in range(t):
    print(c[i])