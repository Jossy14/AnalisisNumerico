import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def obtener_funcion():
    fn = input("Ingrese su funcion:\n")
    return lambda x: eval(fn)

def obtener_puntos():
    a = float(input("Punto inicial:\n"))
    b = float(input("Punto final:\n"))
    return a, b

def obtener_error_maximo():
    es = float(input("Error maximo:\n"))
    return es

def falsa_posicion(f, a, b, es):
    xl = a
    xu = b
    xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
    xrv = []
    ea = 2 * es
    eav = []
    count = 0
    countV = []
    xlV = []
    xuV = []
    falp_table = []
    
    fxl = f(xl)
    fxu = f(xu)
    fxr = f(xr)
    xlV.append(fxl)
    xuV.append(fxu)
    
    falp_table.append(["iteracion", "xl", "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "error"])
    
    while ea >= es:
        xrv.append(xu)
        count += 1
        countV.append(count)
        if fxl * fxr > 0:
            xl = xr
        elif fxl * fxr < 0:
            xu = xr
        else:
            ea = 0
        xrOld = xrv[-1]
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))

        if xr != 0:
            ea = abs((xu - xrOld) / xu) * 100
            eav.append(ea)

        fxl = f(xl)
        fxu = f(xu)
        fxr = f(xr)
        xlV.append(fxl)
        xuV.append(fxu)
        falp_table.append([count, xl, fxl, xu, fxu, xr, fxr, ea])
        
    print(" ")
    print(tabulate(falp_table, headers="firstrow", tablefmt="fancy_grid"))

f = obtener_funcion()
a, b = obtener_puntos()
emax = obtener_error_maximo()

falsa_posicion(f, a, b, emax)