#Dado un numero natural X, construir un vector que contenga lso divisores de X, y mostrarlo. Al final
#decir si es un numero primo.

#¿Cuantos divisores tiene? Dependiendo de eso haremos la dimension del vector.
x=int(input("Ingresar un numero natural: "))
divisores=1
cantidad_divisores=0
while divisores<=x:
    if x%divisores==0:
        cantidad_divisores+=1
    divisores+=1

#Cargamos el vector con la dimension de cantidad de divisores.
divisores=1
vector=[None]*cantidad_divisores
indice_vector=0
while divisores<=x:
    if x%divisores==0:
        vector[indice_vector]=divisores
        indice_vector+=1
    divisores+=1
print(vector)
contador_primo=0
divisores=1
while divisores<=x:
    if x%divisores==0:
        contador_primo+=1
    divisores+=1
if contador_primo==2:
    print("Es un numero primo")
else:
    print("No es un numero primo")