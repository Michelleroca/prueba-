#Una panadería vende barras de pan a 27 pesos cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
Barra = int(input("Introduce el número de barras vendidas que no es del dia:\n"))
precio = 27
remanente = .4
costo = Barra * precio * remanente
print("El precio de la barra es:\n " + str(precio))
print("El descuento sobre una barra que no es del dia es: \n" + str((1-remanente)* 100) + "%")
print("El costo final a pagar es: \n " + str(round(costo, 2)))