x=int(input("Ingresar un numero natural: "))
copia=x
y=0
while x>0: 
    r=x%10
    y=y*10+r
    x=x//10
if copia==y:
    print("Es capicua")
else:
    print("No es capicua")