x=int(input("Ingresar los numeros naturales: "))
contador=0
divisores=1
while divisores<=x:
    if x%divisores==0:
        contador=contador+1
    divisores=divisores+1
print("Todos sus divisores: ",contador)