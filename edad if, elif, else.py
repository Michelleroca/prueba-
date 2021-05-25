edad=int(input("Hola, escribe tu edad" ))
if (edad>=18):
    print("ya eres mayor de edad")
    print ("naciste en el año : " +str(2021-edad))
elif (edad<18 and edad>0):
    print ("es menor de edad")
else:
    print("no se sabe")
