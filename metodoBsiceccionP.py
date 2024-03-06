from math import *
import matplotlib.pyplot as plt
import numpy as np

print("Se te pedira cierto tipo de datos para calcular una funcion usando el metodo de biseccion")

# matplotlib -> es para realizar graficos, biblioteca de visualizacion de datos
# sympy -> Proporciona herramientas para realizar cálculos simbólicos, como resolver ecuaciones, integrar funciones, derivar expresiones
fn = input("Ingrese su funcion\n")
x = 'x'
puntoA = input("Punto inicial\n")
puntoB = input("Punto final\n")

def tranfFunctSimbo(punto):
    return eval(fn.replace('x', str(punto)))

print(puntoA)
resultadoA = tranfFunctSimbo(puntoA)
resultadoB = tranfFunctSimbo(puntoB)

print("Resultado en el punto A:", resultadoA)
print("Resultado en el punto B:", resultadoB)

#Puntos inicial y final

#Margen de error que queremos llegar
criterioError = float(input("Ingrese el valor de error a buscar"))
cont = 0 #Numero de iteración
error=1 #Valor del error
pmAnterior = 0 #Punto medio anterior (calcular error)



if tranfFunctSimbo(puntoA) * tranfFunctSimbo(puntoB) < 0:
    print(" ")
    print("{:^70}".format("Metodo Bisección"))
    print("{:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10}".format("i", "a", "f(a)", "pm", "b", "f(b)", "Error"))

    while error > criterioError:
        pm = (puntoA * puntoB)/2
        criterioError = abs((pm - pmAnterior) /pm)
        if tranfFunctSimbo(pm) * tranfFunctSimbo(puntoA) < 0:
            puntoB = pm 
        else:
            puntoA = pm
        
        pmAnterior = pm
        
        print("{:^10} {:^10f} {:^10f} {:^10f} {:^10f} {:^10f} {:^10f}".format(cont, puntoA, f(puntoA), pm, puntoB, f(puntoB), round(error*100,6)))
        cont+=1
        
        print("")
        print("Valor de x: ", round(pm,6), 
              "\nValor aproximado a: ", round(pm*100,6),"%")
        