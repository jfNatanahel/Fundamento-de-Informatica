n_a=int(input("Ingresar el tamaño del vector A: "))
v_a=[None]*n_a
i=0
while i<n_a:
    v_a[i]=int(input("Ingresar un numero natural: "))
    i=i+1
i=0
m_a=v_a[i]
while i<n_a:
    if m_a<v_a[i]:
        m_a=v_a[i]
    i=i+1
print("El mayor del Vector A es:",m_a)
###########VECTOR B###########
n_b=int(input("Ingresar el tamaño del vector B:"))
v_b=[None]*n_b
j=0
while j<n_b:
    v_b[j]=int(input("Ingresar un numero natural: "))
    j=j+1
j=0
bandera=0
m_b=v_b[j]
while j<n_b and bandera==0:
    if m_b<v_b[j]:
        m_b=v_b[j]
    j=j+1
print("El mayor de B es:",m_b)
if m_b==m_a:
    print("El mayor de A se encuentra en B")
else:
    print("El mayor de A no se encuentra en B")
