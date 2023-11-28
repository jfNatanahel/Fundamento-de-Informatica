n=int(input("ingresar el tamaño del vector: "))
v=[None]*n
i=0
while i<n:
    v[i]=int(input("Ingresar los elementos del vector: "))
    i=i+1
i=0 #Empezar desde el 1er numero.
pares=0
impares=1
while i<n:
    if v[i]%2==0:
        pares=pares+v[i]
    else:
        impares=impares*v[i]
    i=i+1
print("Suma de los pares es: ",pares)
print("La multiplicacion de los impares es: ",impares)