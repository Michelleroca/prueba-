#EN ESTA ACTIVIDAD SE BUSCARÁ EL AREA DE 5 FIGURAS
print("\nHola, ingresa el numero de la figura a la cual te gustaria sacar el area.")
print("1.triangulo\n2.cuadrado\n3.rectangulo\n4.circulo\n5.rombo")

opcion=int(input("\ningresar numero: "))

if(opcion==1):
    base=int(input("ingresa la base: " ))
    altura=int(input("ingrese la altura: "))
    res=(base*altura)/2
    print("el área es: ",res)
elif(opcion==2):
    base=int(input("ingrese base: "))
    res=base**2
    print("el area es: ",res)
elif(opcion==3):
    base=int(input("ingrese la base: "))
    altura=int(input("ingrese la altura"))
    res=base*altura
    print("el area es: ",res)
elif(opcion==4):
    pi=float(input("inserte pi: "))
    radio=int(input("inserte radio: "))
    res=pi*radio**2
    print("el area es: ",res)
elif(opcion==5):
    Diagonal=int(input("ingresa la diagonal: "))
    diagonal=int(input("ingresa la diagonal: "))
    res=diagonal*Diagonal/2/2
    print("el area es: ",res)
else:
    print("no existe ese numero de figura")



