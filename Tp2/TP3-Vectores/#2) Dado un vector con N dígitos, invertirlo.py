#Algoritmos
n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
i=0
while i<n:
    v[i]=int(input("Ingresar elementos del vector: "))
    i=i+1
i=n-1
while i>=0:
    print("Elementos invertidos",v[i])
    i=i-1