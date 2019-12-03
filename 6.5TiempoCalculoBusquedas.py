import math
import random
import time
class BusquedaBinaria:

    def BusquedaBinaria(self, lista, clave, izquierda, derecha):
        inicio_de_tiempo = time.perf_counter()

        """Búsqueda binaria
            Precondición: lista está ordenada
            Devuelve -1 si clave no está en lista;
            Devuelve p tal que lista[p] == clave, si clave está en lista
            """

        # Busca en toda la lista dividiéndola en segmentos y considerando
        # a la lista completa como el segmento que empieza en 0 y termina
        # en len(lista) - 1.

        # izquierda guarda el índice inicio del segmento
        # derecha guarda el índice fin del segmento

        while izquierda <= derecha:
            # el punto medio del segmento
            medio = math.floor((izquierda + derecha) / 2)
            # si el medio es igual al valor buscado, lo devuelve
            if lista[medio] == clave:
                return medio
            # si el valor del punto medio es menor que clave, sigue buscando
            # en el segmento de la derecha: [medio+1, der],
            # descartando la izquierda
            elif lista[medio] < clave:
                izquierda = medio + 1
            # sino, sigue buscando en el segmento de la izquierda: [izq, medio-1],
            # descartando la derecha
            else:
                derecha = medio - 1

            final = time.perf_counter() + time.perf_counter()
            totalTiempo = final - inicio_de_tiempo

            return totalTiempo
            # si no salió del ciclo, vuelve a iterar con el nuevo segmento

        # salió del ciclo de manera no exitosa: el valor no fue encontrado

        return -1


class BusquedaSecuencial:

    def busquedaSecuencial(self, lista, clave):

        """ Búsqueda lineal.
            Si clave está en lista devuelve True, de lo
            contrario devuelve False.
        """
        # Estrategia: se recorren uno a uno los elementos de la lista
        # y se los compara con el valor "clave" buscado.

        # encontrado tiene False si clave no es encontrado, True si clave
        # es encontrado, comienza en False
        encontrado = False
        # el ciclo for recorre todos los elementos de lista:
        inicio_de_tiempo = time.perf_counter()
        for i in lista:
            # i contiene el valor de lista[i]

            # si i es igual a clave, devuelve True
            if i == clave:
                encontrado = True
                break

            final = time.perf_counter() + time.perf_counter()
            totalTiempo = final - inicio_de_tiempo

            return totalTiempo
        # si salió del ciclo sin haber encontrado el valor, devuelve False
        #tiempo_final = time()
        #tiempo_ejecucion = tiempo_final - tiempo_inicial
        #print('El tiempo de ejecucion de la busqueda binaria secuencial es de:  ', tiempo_ejecucion)

        return encontrado

class QuickSort:
    def intercambia(self, A, x, y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp

    def Particionar(self, A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if (A[j] <= x):
                i = i + 1
                self.intercambia (A, i, j)
        self.intercambia(A, i+1, r)
        return i + 1

    def QuickSort(self, A, p, r):
        if (p < r):
            q = self.Particionar(A, p, r)
            #print (A[p:r])
            self.QuickSort(A, p, q-1)
            self.QuickSort(A, q+1, r)
        return A

    def ordenar(self, A):
        p = 0
        r = len(A) - 1
        q = int((p + r) / 2)
        return self.QuickSort(A, p, r)


def main():
    DatoAencontrarA = random.randint(0,1999)
    DatoAencontrarB = random.randint(0, 1999)
    A = []
    for k in range(2000):
        A.append(random.randint(0, 1999))
    B = []
    for i in range(500):
        B.append(random.randint(0, 1999))


    # se ordenan las listas A y B
    ordenarLista = QuickSort()
    print('lista A: ',ordenarLista.ordenar(A))

    print('lista B: ',ordenarLista.ordenar(B))

    # se implementa la busqueda de las listas ordenadas buesqueda binaria, lineal.
    a = BusquedaBinaria()
    print(a.BusquedaBinaria(A, DatoAencontrarA, 0, len(A)-1))
    print('el tiempo de ejecucion de la busqueda binaria de la lista A es de : \f')


    TimeBusquedaSecuencial = BusquedaSecuencial()
    print(TimeBusquedaSecuencial.busquedaSecuencial(A,DatoAencontrarA))
    print('el tiempo de ejecucion de la busqueda secuencial de la lista A es de : \f')

    #------------------------------------------------------------------------------------#
    # se implementa la busqueda de la lista B y se obtiene la complejidad de los algoritmos

    b = BusquedaBinaria()
    print(b.BusquedaBinaria(B, DatoAencontrarB, 0, len(B) - 1))
    print('el tiempo de ejecucion de la busqueda binaria de la lista B es de : \f')

    TimeBusquedaSecuencial = BusquedaSecuencial()
    print(TimeBusquedaSecuencial.busquedaSecuencial(B, DatoAencontrarB))
    print('el tiempo de ejecucion de la busqueda secuencial de la lista B es de : \f')


if __name__ == "__main__":
    main()