import random

def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(10000000,70000000)
      return lista

#print("Ingrese cuantos numeros aleatorios desea obtener")
n= 100

aleatorios=listaAleatorios(n)
print(aleatorios)