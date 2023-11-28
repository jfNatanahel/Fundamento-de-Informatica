n_a=int(input("Ingresar el tamaño del vector A: "))
v_a=[None]*n_a
i=0
while i<n_a:
    v_a[i]=int(input("Ingresar un numero natural: "))
    i=i+1
print("Vector A",v_a)
i=0
y_a=0
while i<n_a:
    y_a=y_a*10+v_a[i]
    i=i+1
print("Numero de Vector A es: ",y_a)
##################
n_b=int(input("Ingresar el tamaño del vector B: "))
v_b=[None]*n_b
j=0
while j<n_b:
    v_b[j]=int(input("Ingresar un numero natural: "))
    j=j+1
print("Vector B",v_b)
j=0
y_b=0
while j<n_b:
    y_a=y_a*10+v_b[j]
    j=j+1
print("Numero formado por el Vector A y B: ",y_a)
