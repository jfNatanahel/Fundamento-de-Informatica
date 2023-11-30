#Dado un vector A de N numeros enteros, duplicar sus elementos pares, dentro del mismo vector A.
n=int(input("Tamaño vector A: "))
v=[None]*n
contador_pares=0
for i in range(n):
    v[i]=int(input("Elementos A: "))
    if v[i]%2==0:
        contador_pares+=1
v_aux=[None]*(n+contador_pares)
for i in range(n):
    v_aux[i]=v[i]
    if v_aux[i]%2==0:
        for j in range(i+1,n):
            v_aux[j]=v[i]
        
print(v_aux)