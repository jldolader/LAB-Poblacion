from poblacion import *

def test_lee_poblaciones(ruta_fichero):
    return lee_poblaciones(ruta_fichero)

def test_calcula_paises(poblaciones):
    print(calcula_paises(poblaciones))
    
def test_filtra_por_pais(poblaciones, nombre_o_codigo):
    print(filtra_por_pais(poblaciones, nombre_o_codigo))
    
def test_filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    print(filtra_por_paises_y_anyo(poblaciones, anyo, paises))

if __name__ == '__main__':
    poblaciones = test_lee_poblaciones("data/population.csv")
    #print(poblaciones)
    #test_calcula_paises(poblaciones)
    #test_filtra_por_pais(poblaciones, "ESP")
    test_filtra_por_paises_y_anyo(poblaciones, 2014, set(['Yemen', 'Arab World', 'TWE', 'ESP', 'HRV']))