from primerEjercicioBrayanMartinez import detectarPrimos, n,arrayPrim;palindo=[];n=int(input('Indique el rango: '))
def palindromicos(primos):
  for i in primos:
    if i > 10 and str(i) == str(i)[::-1]: palindo.append(i);return palindo
print('Los numeros palindromicos primos son: ',palindromicos(detectarPrimos(arrayPrim,n)))



