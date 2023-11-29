
n=int(input("Ingresar el tamaño del vector: "))
v=[None]*n
x=int(input("Ingresar el numero a buscar en el vector: "))
bandera=0
for i in range(n):
    v[i]=int(input("Elementos del vector: "))
    if x==v[i]:
        bandera=1
if bandera==1:
    print("El elemento se encuentra en el vector: ")
else:
    print("El elemento no se encuentra en el vector")