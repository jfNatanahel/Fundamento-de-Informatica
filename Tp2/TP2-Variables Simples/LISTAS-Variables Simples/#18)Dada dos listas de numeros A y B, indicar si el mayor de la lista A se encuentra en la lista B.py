tamaño_a=int(input("Ingresar el tamaño de la lista A: "))
primer_numero_a=int(input("Ingresar el primer numero de A: "))
mayor_a=primer_numero_a
i=1
while i<tamaño_a:
    a=int(input("Ingresar los elementos de la lista: "))
    if mayor_a<a:
        mayor_a=a
    i=i+1
#print("El mayor de A es: ",mayor_a)
tamaño_b=int(input("Ingresar el tamaño de la lista B: "))
primer_numero_b=int(input("Ingresar el primer numero de B: "))
mayor_b=primer_numero_b
i=1
while i<tamaño_b:
    b=int(input("Ingresar los elementos de la lista: "))
    if mayor_b<b:
        mayor_b=b
    i=i+1
print("El mayor de A es: ",mayor_a)
print("El mayor de B es: ",mayor_b)
if mayor_a==mayor_b:
    print("El mayor de A se encuentra en B")
else:
    print("EL mayor de A no se encuentra en B")