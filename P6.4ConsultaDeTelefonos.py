from ConsultaDeDatos import *
class ImplentacionDeLaBusqueda:

    def leerArchivo(self, archivo):
        datos = []
        datos2 = []
        elementos = []
        file = open(archivo, 'r')
        for f in file.readlines():
            linea = f.replace('\n', '')
            elementos = linea.split(',')
            try:
                datos.append([str(elementos[0]), int(elementos[1])])

            except ValueError:
                datos.append(['', 0.0])

        file.close()
        del (file)
        return datos
    def generarResultados(self, lista,datoencontrar):
        #print('esta es la lista', lista)
        #print('este es el dato a encontrar: ', datoencontrar)
        rectangulo = BusquedaSecuencial()
        resultados = []
        for f in range(0, len(lista)):
            #print(datoencontrar)
            area = rectangulo.busqueda(lista,datoencontrar)

            resultados.append([area])
            #print(resultados)

        return resultados

    def guardarResultados(self, archivo, datos, resultados):
        file = open(archivo, 'w')
        for f in range(0, len(datos)):
            linea =  str(resultados[f][0]) + ',' + '\n'
            file.write(linea)

        file.close()
        del (file)





def main():
    file = ImplentacionDeLaBusqueda()
    arreglo = []
    datoAencontrar = 7676798567
    arreglo = file.leerArchivo('datos.txt')
    resultados = file.generarResultados(arreglo,datoAencontrar)
    file.guardarResultados('ResultadosDeBusqueda.txt', arreglo, resultados)
   # print(resultados)



if __name__ == '__main__':
    main()