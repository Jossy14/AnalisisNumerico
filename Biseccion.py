import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def bisec(a, b, es, imax):
  xl = a             #Valor inicial del intervalo de x
  xu = b             #Valor final del intervalo de x
  pm = (xl + xu)/2    #aproximacion de la raiz de f(x)
  xrv = []            #vector que almacenará xr
  ea = 2*es           #error(%) se le asigna un valor "grande" para poder empezar el ciclo de iteración
  eav = []            #vector que guarda el error
  count = 0           #contador de iteraciones
  countV = []         #vector que guarda las iteraciones
  fxrv = []           #vector que guarda las aproximaciones de f(x)
  bisec_table = []    #tabla de datos

  fxl = f(xl)         #aproximacion de f(x izquierda)
  fxu = f(xu)         #aproximacion de f(x derecha)
  fpm = f(pm)         #aproximacion de f(x raiz)
  fxrv.append(fxr)

  bisec_table.append(["--", "--", "--", "--", "--", "--", "--", "--"])    #primera linea de la tabla para la iteracion 0
  bisec_table.append([count, xl, xu, fxl, fxu, pm , fpm, "--"])    #primera linea de la tabla para la iteracion 0
  
  while ea > es and count <= imax:              #ciclo controlado por el error maximo y el numero de iteraciones

    xrv.append(pm)                              
    count += 1
    countV.append(count)
           
    if fxl*fxr < 0:                             #verifica si hay cambio de signo para reordenar xl y xu
      xu = pm
    elif fxl*fxr > 0:
      xl = pm
    else:
      ea = 0

    xrold = pm                                  #aproximacion anterior a la raiz de f(x)
    pm = (xl + xu)/2                            #aproximacion actual a la raiz de f(x)

    if pm != 0:                                 #Calcula el error
      ea = abs(pm - xrold)
      eav.append(ea)

    fxl = f(xl)                                 #aproximacion de f(x izquierda)
    fxu = f(xu)                                 #aproximacion de f(x derecha)
    fxr = f(pm)                                 #aproximacion de f(x raiz)
    fxrv.append(fxr)

    bisec_table.append([count, xl, xu, fxl, fxu, pm, fxr, ea])    #agrega datos a la tabla
    
  print(" ")
  print("Metodo Biseccion")
  print(tabulate(bisec_table, headers = ["Iteracion", "xl", "xu", "f(xl)", "f(xu)", "x", "fx", "e absoluto"]))

  print(" ")
  print("Grafica del error")
  plt.plot(countV, eav, label=("e absoluto"))

  plt.plot()                      #llamando grafica 

  plt.xlabel("Numero de iteraciones")            #Etiqueta de eje
  plt.ylabel("e absoluto")            #Etiqueta de eje
  plt.title("Grafica de e absoluto Vs Numero de Iteraciones") #Titulo del grafico
  plt.legend()                    #Leyendas
  plt.show()                      #Mostrar grafico

  return()


#Valores para graficar la funcion
a = 0           #Valor inicial del rango de x para graficar - CAMBIAR SEGUN EL PROBLEMA
b = 1           #Valor final del rango de x para graficar - CAMBIAR SEGUN EL PROBLEMA
n = 50          #Cantidad de puntos - CAMBIAR SEGUN SEA NECESARIO


#Parametros para controlar las aproximaciones
emax = 10**-3   #Error maximo - CAMBIAR SEGUN EL PROBLEMA
itermax = 20    #Numero de iteraciones maximo - CAMBIAR SEGUN EL PROBLEMA
x1 = 0          #primer valor inicial de X - CAMBIAR SEGUN EL PROBLEMA
x2 = 1          #segundo valor inicial de X - CAMBIAR SEGUN EL PROBLEMA

#f(x)
x = np.linspace(a, b, n)     #Se generan los valores de x para construir la grafica
def f(xs):
  f_x = np.tan(xs) - 1/(xs**2 + 1)  #Funcion - CAMBIAR SEGUN EL PROBLEMA
  return (f_x)

fx_table = []                 #Tabla de datos de x vs f(x)
cont = 0                      #contador
fx = f(x)                     
for i in range(len(x)):       #Ciclo para llenar la tabla
  fx_table.append([x[i], fx[i]])


#Tabla grafica de la funcion
print("Tabla de datos para la Grafica de la Funcion")
print(" ")
print(tabulate(fx_table, headers = ["x", "fx"]))

print(" ")

print("Grafica de la funcion")
plt.plot(x, fx, label=("fx"))
plt.plot(x, np.zeros(len(x)), label=("0"))

plt.plot()                      #llamando grafica 

plt.xlabel("x axis")            #Etiqueta de eje
plt.ylabel("y axis")            #Etiqueta de eje
plt.title("Grafica de fx") #Titulo del grafico
plt.legend()                    #Leyendas
plt.show()                      #Mostrar grafico


bisec(x1, x2, emax, itermax)