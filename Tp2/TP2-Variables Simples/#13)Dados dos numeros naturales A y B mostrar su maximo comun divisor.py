a=int(input("Ingresar un numero natural A: "))
b=int(input("Ingresar un numero natural B: "))
divisor_a=1
divisor_b=1
maximo_comun=0
while divisor_a<=a and divisor_b<=b:
    if a%divisor_a==0 and b%divisor_b==0:
        maximo_comun=divisor_a
    divisor_a+=1
    divisor_b+=1
print("MCD",maximo_comun)