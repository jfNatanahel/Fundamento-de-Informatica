x=int(input("Ingresar un numero natural: "))
divisor=1
while divisor<=x: #Debe cumplir una condicion.
    if x%divisor==0:
        print("Divisores",divisor)
    divisor=divisor+1
