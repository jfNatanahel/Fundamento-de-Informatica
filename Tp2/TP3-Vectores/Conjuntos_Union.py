n_a=int(input("Ingresar el tamaño del vector A: "))
v_a=[None]*n_a
i=0
while i<n_a:
    v_a[i]=int(input("Ingresar elementos del vector: "))
    i=i+1
#####
n_b=int(input("Ingresar el tamaño del vector B: "))
v_b=[None]*n_b
j=0
while j<n_b:
    v_b[j]=int(input("Ingersar los elementos del vector B: "))
    j=j+1
i=0
j=0
k=0
c=[]
while i<n_a:
    bandera=0
    while j<n_b:
        if v_a[i]==v_b[j]:
            bandera=1
        j=j+1
    if bandera==0:
        c[k]=v_a[i]
    i=i+1
i=0
while i<=k:
    print(c[k])
    i=i+1     