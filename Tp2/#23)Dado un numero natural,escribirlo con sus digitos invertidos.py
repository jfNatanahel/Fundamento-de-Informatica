#3589 = 9853
x=int(input("Ingresar un numero natural: "))
y=0
while x>0:
    r=x%10
    y=y*10+r
    x=x//10
print(y)