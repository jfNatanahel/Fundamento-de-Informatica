a=int(input("Ingresar los numeros naturales A: "))
b=int(input("Ingresar los numeros naturales B: "))
divisor_a=1
divisor_b=1
while divisor_a<=a and divisor_b<=b:
    if a%divisor_a==0 and b%divisor_b==0:
        print("Divisores comunes")
