#Modelo
#1.Tomar los datos del Conjunto A
#2.Tomar los datos del Conjunto B
#3.Pasar los datos del conjuto A al Conjunto C.
#4.Pasar los datos del Conjunto B, que no esten A al conjunto C.
n=int(input("Ingresar el tamaño del vector A: "))
v_a=[None]*(n+1)
for i in range (1,n+1,1):
    v_a[i]=int(input("Ingresar elementos del vector A: "))
m=int(input("Ingresar el tamaño del vector B: "))
v_b=[None]*(m+1)
for j in range (1,m+1,1):
    v_b[j]=int(input("Ingresar elementos del vector B: "))
#Pasar los elementos de A para C.
c=[None]*(n+m+1)
for i in range(1,n+1,1):
    c[i]=v_a[i]
l=n #cantidad del vector n

for j in range(1,m+1,1):
    bandera=0
    for i in range(1,n+1,1):
        if v_a[i]==v_b[j]:
            bandera=1 #Quiere decir que existen repetidos entre A y B
    if bandera==0:
        l=l+1
        c[l]=v_b[j]

#Mostrar el Vector union.
for i in range (1,l+1,1):
    print(c[i])