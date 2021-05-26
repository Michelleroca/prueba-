#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado
peso = input("¿Cuál es tu peso?\n ")
estatura = input("¿Cuál es tu estatura?\n")
imc = round(float(peso)/float(estatura)**2)
print("Tu índice de masa corporal es \n " + str(imc))