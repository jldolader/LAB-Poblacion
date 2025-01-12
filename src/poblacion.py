from collections import namedtuple
import csv
from matplotlib import pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero: str) -> list[RegistroPoblacion]:
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [RegistroPoblacion(
                pais = str(p[0]),
                codigo = str(p[1]),
                año = int(p[2]),
                censo = int(p[3])
            )
            for p in reader
        ]

def calcula_paises(poblaciones: list[RegistroPoblacion]):
    return sorted(set(p.pais for p in poblaciones))

def filtra_por_pais(poblaciones: list[RegistroPoblacion], nombre_o_codigo: str) -> list[tuple[int, int]]:
    nombre_o_codigo = nombre_o_codigo.lower()
    return [(p.año, p.censo) for p in poblaciones if p.pais.lower() == nombre_o_codigo or p.codigo.lower() == nombre_o_codigo]

def filtra_por_paises_y_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set[str]) -> list[tuple[str, int]]:
    return [(pais, datos[1]) for pais in paises for datos in filtra_por_pais(poblaciones, pais) if anyo == datos[0]]

def muestra_evolucion_poblacion(poblaciones: list[RegistroPoblacion], nombre_o_codigo: str):
    datos = filtra_por_pais(poblaciones, nombre_o_codigo)
    lista_años, lista_habitantes = zip(*datos) if datos else ([], [])
    
    plt.title(f"Evolución de la población de {nombre_o_codigo.capitalize()}")
    plt.plot(lista_años, lista_habitantes)
    plt.text(0.01, 0.95, "(a)", transform=plt.gca().transAxes, fontsize=12, weight='bold')
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set[str]):
    datos = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    lista_paises, lista_habitantes = zip(*datos) if datos else ([], [])
    
    plt.title(f"Población en el año {anyo}")
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
