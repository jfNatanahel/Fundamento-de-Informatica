n=int(input("Ingresar el tamaño del vector A: "))
v_a=[None]*n
for i in range (n):
    v_a[i]=int(input("Ingresar elementos del vector A: "))
m=int(input("Ingresar el tamaño del vector B: "))
v_b=[None]*m
for j in range (m):
    v_b[j]=int(input("Ingresar elementos del vector B: "))
#Pasar los elementos de A para C.
c=[]*n
for i in range(n):
    c[i]=v_a[i]
l=n #cantidad del vector n

for j in range(m):
    bandera=0
    for i in range(n):
        if v_a[i]==v_b[j]:
            bandera=1 #Quiere decir que existen repetidos entre A y B
    if bandera==0:
        l=l+1
        c[l]=v_b[j]

#Mostrar el Vector union.
for i in range (l):
    print(c[i])