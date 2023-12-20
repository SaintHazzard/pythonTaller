# 1. En matemáticas, los números primos gemelos son aquellos números primos que difieren en 2 unidades. Por ejemplo, (3, 5), (5, 7), (11, 13) son pares de números primos gemelos.

# Instrucciones: 
# Escriba un programa en Python que encuentre todos los pares de números primos gemelos en un rango dado.
# El programa debe solicitar al usuario que ingrese el límite superior del rango de búsqueda.
# Luego, debe verificar todos los números en el rango (2, límite) para determinar si son números primos y si su diferencia con el siguiente número también es primo.
# Finalmente, el programa debe imprimir los pares de números primos gemelos encontrados.


def detectarPrimos(arrayPrim,n):
  noprimo=0
  for i in range(2,n):
    for j in range(2,int(i**0.5)+1):
      if i % j == 0:
        noprimo+=1
    if noprimo==0:
      arrayPrim.append(i)
    noprimo=0
  return arrayPrim


if __name__ == "__main__":
  n=int(input('Indique el rango: '))
  cont=0
  arrayPrim=[1,2]
  arrayPrim = detectarPrimos(arrayPrim,n)
  print('Los numeros primos gemelos son: ');[print(arrayPrim[i],arrayPrim[i+1]) for i in range(len(arrayPrim)-1)  if arrayPrim[i+1]-arrayPrim[i] == 2]




