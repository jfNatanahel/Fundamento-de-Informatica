#Dado un numero natural X, construir un vector que contenga lso divisores de X, y mostrarlo. Al final
#decir si es un numero primo.
x=int(input("Ingresar un numero natural: "))
divisores=1
indice_vector=0
vector=[]
while divisores<=x:
    if x%divisores==0:
        vector[indice_vector]=divisores
        indice_vector+=1
    divisores+=1
print(vector)