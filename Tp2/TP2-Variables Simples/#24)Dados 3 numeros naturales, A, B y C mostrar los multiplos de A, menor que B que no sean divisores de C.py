a=int(input("Ingresar numero natural A: ")) 
b=int(input("Ingresar un numero natural B: "))
c=int(input("Ingresar un numero natural C: "))
multiplos=1
bandera=0
while bandera==0:
    multiplos_a=a*multiplos #Multiplos de A
    if multiplos_a<b: #Multiplos de A < B
        if c%multiplos_a!=0: #C dividido Multiplo de A no es igual a 0. Imprimir
            print(multiplos_a)
    else:
        bandera=1
    multiplos+=1
    
