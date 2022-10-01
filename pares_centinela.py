#input
n=int(input("digite un numero: "))
#processing
par=0
impar=0
while n!=0:
    p=n%2

    if p==0:
        par= par+1
    else:
        impar=impar+1
    n=int(input("digite un numero: "))
print("Hay "+ str(par)+" numeros pares y "+ str(impar)+" numeros impares")

