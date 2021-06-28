import numpy as np

"""
Exercises taken from
https://www.iaa.csic.es/python/cientifico/ejercicios/numpy/
"""

"""
Cree un array que contenga los siguientes elementos: [1, 3., True, 'Hola Mundo'].
¿De qué tipo es este array?. Muéstrelo por pantalla.
"""
x = np.array([1, 3., True, 'Hola Mundo'])
print(x.dtype)

"""
¿Cuál es el tamaño en bytes de un array de 1000 elementos de tipo booleano?
"""
booleans = np.zeros(1000, dtype=bool)
print(booleans.itemsize * 1000)

"""
Cree un array cuyos elementos sean los enteros pares en [1,100] y
en orden decreciente.
Muestre los 10 últimos por pantalla.
"""
even = np.arange(100, 1, -2)
print(even[-10:])

"""
Cree un array con 10 elementos en el intervalo [-2,2] y
equidistantes entre ellos. Muestre por pantalla el array.
Después muestre sólo el tercer y cuarto elemento.
"""
equidistant = np.linspace(-2, 2, 10)  
print(equidistant)

"""Genere un array de tipo 'float' de dimensiones (4, 4).
Debe contener números consecutivos del 1 al 16."""
a2d = np.arange(1,17, dtype=float).reshape(4, 4)
print(a2d)

"""
Dado el array

2 4 5 6
0 3 7 4
8 8 5 2
1 5 6 1

Seleccione con una instrucción el subarray de elementos
0 3 7 4

Después, seleccione el subarray de elementos

2 5
8 5
"""
array = np.array([[2, 4, 5, 6], [0, 3, 7, 4], [8, 8, 5, 2], [1, 5, 6, 1]])
print(array[1, :])

subarray = array[::2,::2]
print(subarray)

"""
Cree un array de enteros de dimensiones (3,3) y valores iguales a 0.
Asigne el valor de 1 a las cuatro esquinas.
"""
corner = np.zeros((3,3), dtype=int)
corner[::2, ::2] = 1
print(corner)

"""
Opción a: Dado el array de tipo float64 y elementos [3., 4., 6., 1, 1.5],
agregue un cero al principio del array y un -1 al final.
"""
a = np.array([3., 4., 6., 1, 1.5])
a = np.append([0], a)
a = np.append(a, [-1])
print(a)

"""
Opción b: Tengo valores de cordenadas (x, y) en las columnas del array

1.33 4.5
30.0 10.7
70.2 0.5

Agregue a este array las coordenadas (37.1, -3.6).
Muestre por pantalla las dimensiones del nuevo array.
"""
da = np.array([[1.33, 4.5], [30.0, 10.7], [70.2, 0.5]])
da_r = np.append(da, [37.1, -3.6]).reshape(-1, 2)
print(da.shape, da_r.shape)

"""
Copie el array del ejercicio anterior. Traspóngalo.
Agregue ahora dos nuevos pares de coordenadas: (10.8, 3.0) y (35.8, 12.0).
"""
da_copy = da.copy()
print(da_copy)
print(da_copy.T)
da_copy = da_copy.T
coords = np.array([[10.8, 35.8], [3.0, 12.0]])
da_copy = np.append(da_copy, coords, axis = 1)
print(da_copy)
print(da_copy.T)

"""
¿Puedo sumar los arrays a = [[1, 2, 3]] y b = [[0], [1], [0]]?.
¿Por qué?. De ser posible, ¿cuál es su suma?.
"""
a = np.array([[1, 2, 3]])
b = np.array([[0], [1], [0]])
print(a + b)

"""
¿Todos los valores del arraya = [0, 1, 2, 3, 4]
son menores que b = [0, 0, 0, 0]?.
¿Y alguno de ellos?.
"""
a = np.array([0, 1, 2, 3, 4])
b = np.array([0, 0, 0, 0, 0])
print(np.all(a < b))
print(np.any(a < b))

"""
Los arrays a = [0, 1, 2, 3] y b = [-0.1, 1.01, 1.98, 3.15],
¿son iguales si se considera un valor de tolerancia absoluta
(diferencia entre elementos de la misma posición) inferior a 0.16
"""
a = np.array([0, 1, 2, 3])
b = np.array([-0.1, 1.01, 1.98, 3.15])
print(abs(a - b))
print(np.all(abs(a - b) < 0.16))

"""
¿Algún valor de la operación OR lógico entre los arrays
a = [0, 1, 1] y b = [1, 0, 0] es verdadero?.
¿Y si la operación es un AND lógico?.
"""
a = np.array([0, 1, 1])
b = np.array([1, 0, 0])
print(np.any([a[i] or b[i] for i in range(a.size)]))
print(np.any([a[i] and b[i] for i in range(a.size)]))

"""
Dados los arrays a = [1, 4, 2, 7] y b = [1, 3, 2, 9],
obtenga la media aritmética de la diferencia (a-b).
"""
a = np.array([1, 4, 2, 7])
b = np.array([1, 3, 2, 9])
print(np.mean(a - b))

"""
Dado el array a = ['1', '2', '3'],
realice las operaciones necesarias para obtener la suma todos ellos.
"""
a = np.array(['1', '2', '3'])
print(np.sum(a.astype('i')))

"""
Descargue el fichero NucleosPoblacion.csv.
Léalo usando la rutina "numpy.genfromtxt"
"""
url = 'https://www.iaa.csic.es/python/cientifico/ejercicios/numpy/NucleosPoblacion.csv'
nucleo = np.genfromtxt(url, delimiter = ',',
                       names="FID,OBJECTID,Texto,Poblacion,CodMun,Municipio,CodProvin,Provincia,X,Y"
                       , encoding='utf-8', dtype=None, skip_header=1 )
"""
¿Cuántos Municipios tienen más de 100000 habitantes?.
¿Cuál es la segunda ciudad más poblada?.
¿Qué posición ocupa Granada en el ranking de las más pobladas?.
"""
print(sum(np.array(nucleo['Poblacion']) > 100000))
nucleo = np.sort(nucleo, order='Poblacion')[::-1]
print(nucleo['Municipio'][1])
print(np.where(nucleo['Municipio'] == 'Granada')[0] + 1)

"""
Escriba los nombres de los 10 municipios con menos población.
"""
print(nucleo['Municipio'][-10::])

"""
¿Cuál es el municipio situado más al Norte?
(Usar el valor de la coordenada "Y" que representa la latitud en grados).
Proporcione también la provincia a la que pertenece y su población.
"""
latitude_order = np.sort(nucleo, order='Y')[::-1]
print(latitude_order[['Municipio', 'Provincia', 'Poblacion']][0])
print(nucleo[['Municipio', 'Provincia', 'Poblacion']][np.argmax(nucleo['Y'])])

"""
¿Cual es el municipio de la provincia de Granada situado más al Este?. ¿Cual es el situado más al Oeste?.
"""
granada = nucleo[nucleo['Provincia'] == 'Granada']
print(granada[[np.argmin(granada['X']), np.argmax(granada['X'])]]['Municipio'])

"""
Dígame los nombres de los Municipios más cercano y más lejano a Madrid.
Para ello debe calcular la distancia en todos ellos y Madrid. Por supuesto, Madrid no cuenta.
"""

def calculate_distances(nucleo, municipio):
    municipio_mask = nucleo['Municipio'] == municipio
    municipio_coords = nucleo[['X','Y']][municipio_mask]
    other_coords = nucleo[['X','Y']]
    X = other_coords['X'] - municipio_coords['X']
    Y = other_coords['Y'] - other_coords['Y']
    distances = np.sqrt(X ** 2 + Y ** 2)
    data = [(nucleo['Municipio'][i], distances[i]) for i in range(X.size)]
    return data

data = calculate_distances(nucleo, 'Madrid')
distance_city = np.array(data, dtype=[('Municipio', 'U100'), ('Distancia_Madrid', None)])
distance_city = np.sort(distance_city, order='Distancia_Madrid')
print(distance_city[:10])
print(distance_city[-10:])

"""
¿Cuántos Municipios hay en un radio de 5 grados de la ciudad de Barcelona?.
"""
data = calculate_distances(nucleo, 'Barcelona')
distance_city = np.array(data, dtype=[('Municipio', 'U100'), ('Distancia_Barcelona', None)])
print(np.sum([distance_city['Distancia_Barcelona'] < 5]))

"""
Obtenga la media, mediana, desviación estándar, valor máximo
y valor mínimo de la población de los municipios de la provincia de Granada.
"""
poblacion_granada = granada['Poblacion']
print(granada[['Municipio','Poblacion']])
print('media: ', np.mean(poblacion_granada))
print('mediana: ', np.median(poblacion_granada))
print('desviacion standar: ', np.std(poblacion_granada))
print('max: ' + str(np.max(poblacion_granada)) +'; min:' + str(np.min(poblacion_granada)))

