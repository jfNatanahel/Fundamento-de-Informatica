n_a=int(input("Ingresar el tamaño del vector A: "))
v_a=[None]*n_a
i=0
while i<n_a:
    v_a[i]=int(input("Ingresar un numero natural: "))
    i=i+1
print("Vector A",v_a)
i=0
y=0
while i<n_a:
    y=y*10+v_a[i]
    i=i+1
print("Numero de Vector A es: ", y)