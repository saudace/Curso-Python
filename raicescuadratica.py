# -*- coding: utf-8 -*-
"""raicescuadratica.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WVaGIHeFyLynhmYTlYvqdPHCV7b08C4y
"""

import numpy as np
a = [[16/13, 16/ 13], [1, -1]]
b = [72000, 8500]
x = np.linalg.solve(a, b)
print("La solución del sistema es: ", x)


import numpy as np
a = [[1, 1, 1], [1, -1, 0], [3, 3, -13]]
b = [72000, 8500, 0]
x = np.linalg.solve(a, b)
print("La solución del sistema es: ", x)

from sympy import linsolve, symbols

p, a, o = symbols('p a o')
aficionado = {p : 'pumas', a: 'américa', o : 'otro equipo'}

var =[p, a, o]
sol = linsolve([p + a + o - 72000, p - a + 0*o - 8500, 3*p + 3*a - 13*o + 0],
         var)

#print(type(sol))

i=0
for v in sol:
    for y in v:
        print(f'Los aficionados de {aficionado[var[i]]} son {y}')
        i+=1

a = 3.1416
print('Aproximación de pi es', a , 'ya es buena')

a = 3.1416
print('Aproximación de pi es ' + str(a) + ' y ya es buena')

import math
a = math.pi
print('Aproximación de pi es ' + str(a) + ' y ya es buena')
print(f'Aproximación de pi es {a:.4f} y ya es buena´)')
print(f'Aproximación de pi es {a:.30f} y ya es buena´)')

votos = 123_456_789
padron_electoral = 340_123_456
porcentaje = votos/padron_electoral
print('De {:7} votantes solo votaron {:9d} \n que equivale  al {:2.2%} de votantes'
 .format(padron_electoral, votos,porcentaje))

a = int(input("Dame la primera aproximación: "))
n = int(input("Dame el radicando: "))

b = 0.5*(a+n/a)
print(b)

import math

serieRaiz= []

n = 5
x = 8

for i  in range(6):
    x = (1/2)*(x + (n/x))
    serieRaiz.append(x)

print("La raiz aproximada de {0} es {1:.20} \n".format(n,x))

a = int(input("Dame el coeficiente principal a: "))
b = int(input("Dame el coeficiente lineal b: "))
c = int(input("Dame el coeficiente independiente c: "))

if (b**2 - 4*a*c) >= 0 :

    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

    print("Las soluciones son: ", x1, x2)

else:
    print("No hay soluciones reales")