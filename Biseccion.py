import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def obtener_funcion():
    fn = input("Ingrese su funcion\n")
    return lambda x: eval(fn)

def obtener_puntos():
    a = float(input("Punto inicial\n"))
    b = float(input("Punto final\n"))
    return a, b

def obtener_error_maximo():
    es = float(input("Error maximo\n"))
    return es

def bisec(f, a, b, es):
    xl = a
    xu = b
    pm = (xl + xu) / 2
    xrv = []
    ea = 2 * es
    eav = []
    count = 0
    countV = []
    xlV = []
    xuV = []
    bisec_table = []

    fxl = f(xl)
    fxu = f(xu)
    fpm = f(pm)
    xlV.append(fxl)
    xuV.append(fxu)

    bisec_table.append(["I", "a", "f(a)", "pm", "f(pm)", "b", "f(b)", "Error"])

    while ea >= es:
        xrv.append(pm)
        count += 1
        countV.append(count)
        if fxl * fpm < 0:
            xu = pm
        elif fxl * fpm > 0:
            xl = pm
        else:
            ea = 0
        xrOld = pm
        pm = (xl + xu) / 2

        if pm != 0:
            ea = abs((pm - xrOld)/pm)*100
            eav.append(ea)

        fxl = f(xl)
        fxu = f(xu)
        fpm = f(pm)
        xlV.append(fxl)
        xuV.append(fxu)
        bisec_table.append([count, xl, fxl, pm, fpm, xu, fxu, ea])
        
    print(" ")
    print(tabulate(bisec_table, headers="firstrow", tablefmt="fancy_grid"))
    
    # Imprimir los puntos de la función utilizados para graficar
    puntos_funcion = []
    for point in np.linspace(a, b, 100):
        puntos_funcion.append([point, f(point)])
    print("\n")
    print("Puntos de la función utilizados para graficar:")
    print(tabulate(puntos_funcion, headers=["x", "f(x)"], tablefmt="fancy_grid"))
    
    # Graficar los puntos iniciales y finales de la función
    plt.scatter([a], [f(a)], color='g', label='Punto inicial (a)')
    plt.scatter([b], [f(b)], color='m', label='Punto final (b)')
    plt.plot(np.linspace(a, b, 100), f(np.linspace(a, b, 100)), label='Función')
    plt.axhline(0, color='r')
    plt.title("Grafica Metodo Bisección")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

f = obtener_funcion()
a, b = obtener_puntos()
emax = obtener_error_maximo()

bisec(f, a, b, emax)
