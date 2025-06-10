# Programa: Gestión de canciones del álbum "Addison" - Addison Rae
# Tema: Algoritmos de Ordenamiento (Insertion Sort) y Búsqueda (Lineal)
# Autor: Ignacio Robles
# Fecha: 09/06/2025

# Lista de canciones del álbum "Addison" con el formato:
# (número de track, nombre de la canción, duración en minutos)
canciones = [
    (1, "New York", 2.32),
    (2, "Diet Pepsi", 2.49),
    (3, "Money Is Everything", 2.02),
    (4, "Aquamarine", 2.42),
    (5, "Lost & Found", 0.48),
    (6, "High Fashion", 3.18),
    (7, "Summer Forever", 3.47),
    (8, "In the Rain", 3.33),
    (9, "Fame Is a Gun", 3.03),
    (10, "Times Like These", 3.52),
    (11, "Life’s No Fun Through Clear Waters", 0.57),
    (12, "Headphones On", 4.00),
]


def insertion_sort(lista, key=lambda x: x):
    """
    Algoritmo de ordenamiento por inserción (Insertion Sort).

    Parámetros:
    - lista: lista de elementos a ordenar.
    - key: función opcional que define el criterio de ordenamiento.

    Retorna:
    - Una nueva lista ordenada según el criterio definido.
    """
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        # Desplaza elementos mayores hacia adelante
        while j >= 0 and key(lista[j]) > key(actual):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista


def busqueda_lineal(lista, numero_track):
    """
    Algoritmo de búsqueda lineal.

    Busca una canción por su número de track en la lista.

    Parámetros:
    - lista: lista de canciones.
    - numero_track: número del track que se desea buscar.

    Retorna:
    - Una tupla con la información de la canción si se encuentra, o None si no se encuentra.
    """
    for cancion in lista:
        if cancion[0] == numero_track:
            return cancion
    return None

# Programa principal


# Ordenamiento de las canciones por número de track
canciones_ordenadas = insertion_sort(canciones.copy(), key=lambda x: x[0])
print("Canciones ordenadas por número de track:")
for num, nombre, duracion in canciones_ordenadas:
    print(f"{num}. {nombre} - {duracion} min")

# Ordenamiento de las canciones por duración
print("\nCanciones ordenadas por duración:")
canciones_por_duracion = insertion_sort(canciones.copy(), key=lambda x: x[2])
for num, nombre, duracion in canciones_por_duracion:
    print(f"{num}. {nombre} - {duracion} min")

# Bucle interactivo para buscar canciones por número de track
print("\nBuscar canciones por número de track (escriba '0' para salir):")
while True:
    try:
        numero = int(input("Ingrese el número de track: "))
        if numero == 0:
            print("Finalizando búsqueda.")
            break
        resultado = busqueda_lineal(canciones, numero)
        if resultado:
            print(
                f"El track número {numero} es '{resultado[1]}' con una duración de {resultado[2]} minutos.")
        else:
            print(f"No se encontró ningún track con el número {numero}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
