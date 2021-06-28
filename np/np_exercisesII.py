import numpy as np
"""
Exercises taken from
https://www.iaa.csic.es/python/cientifico/ejercicios/numpy/
"""


"""
Descargue el fichero NucleosPoblacion.csv.
Léalo usando la rutina "numpy.genfromtxt"
"""
url = 'https://www.iaa.csic.es/python/cientifico/ejercicios/numpy/NucleosPoblacion.csv'
nucleo = np.genfromtxt(url, delimiter = ',',
                       names="FID,OBJECTID,Texto,Poblacion,CodMun,Municipio,CodProvin,Provincia,X,Y"
                       , encoding='utf-8', dtype=None, skip_header=1)

"""
Realice un histograma con la población de los Municipios para
cada una de las provincias.
Los intervalos de población del histograma irán desde 0 a 300000 personas
en intervalos de 20000 en 20000 personas.
Como ejemplo de formato de salida para cada provincia, tome el siguiente:
Provincia = Ceuta
Codigo de Provincia = 51
Histograma = [0 0 0 0 1 0 0 0 0 0 0 0 0 0 0]
Intervalos de poblacion = [0 20000 40000 60000 80000 100000 ... 280000 300000]]
"""
bins_range = np.arange(0, 320000, 20000)
cods_prov = set(nucleo['CodProvin']);
for cod in cods_prov:
    provincias = nucleo['CodProvin'] == cod
    provincia = nucleo['Provincia'][provincias][0]
    histograma, bin_edges = np.histogram(nucleo['Poblacion'][provincias], bins=bins_range)
    print('Provincia', provincia)
    print('Codigo de Provincia', cod)
    print('Histograma', histograma)
    print('Rango de poblacion', int(np.max(nucleo['Poblacion'][provincias]) - np.min(nucleo['Poblacion'][provincias])))
    print()

"""
¿Cuál es el rango de población? (población más grande - población más pequeña).
"""
print('Rango de poblacion A nivel pais', int(np.max(nucleo['Poblacion']) - np.min(nucleo['Poblacion'])))

"""
Genere 20 números aleatorios entre 0 y 30. Pueden tomar cualquier valor decimal en ese rango.
"""
randoms = np.random.rand(20) * 30
print(randoms)

"""
Lance un dado de 20 caras 10 veces. ¿cual es el valor promedio y la varianza de las tiradas?.
"""
np.random.seed(1)
dice_20 = np.arange(1,21,1)
shoots = np.random.choice(dice_20, 10)
print('Shoots', shoots, np.sum(shoots) )
print('valor promedo', np.mean(shoots))
print('varianza ', np.var(shoots))


