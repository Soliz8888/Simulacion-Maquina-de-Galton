import random  # Importamos la librería random para generar números aleatorios
import matplotlib.pyplot as plt  # Importamos matplotlib para crear gráficos

def simular_canica():
    """
    Simula el recorrido de una canica a través de 12 niveles de obstáculos.
    Retorna la posición final de la canica.
    """
    posicion = 0  # Inicia la posición en 0 (centro)
    for _ in range(12):  # Itera a través de los 12 niveles
        if random.random() < 0.5:  # Si el número aleatorio es menor a 0.5, se mueve a la izquierda
            posicion -= 1
        else:  # Si el número aleatorio es mayor o igual a 0.5, se mueve a la derecha
            posicion += 1
    return posicion

def contar_canicas(num_canicas=3000):
    """
    Simula la caída de 'num_canicas' y cuenta cuántas caen en cada contenedor.
    Retorna una lista con el conteo de canicas en cada contenedor.
    """
    contenedores = [0] * 25  # Crea una lista con 25 contenedores (de -12 a 12)
    for _ in range(num_canicas):  # Itera a través de todas las canicas
        posicion = simular_canica()  # Simula la caída de una canica
        contenedores[posicion + 12] += 1  # Ajusta el índice y cuenta la canica en el contenedor correspondiente
    return contenedores

def graficar_histograma(contenedores):
    """
    Genera y muestra un histograma de los contenedores usando matplotlib.
    """
    plt.bar(range(len(contenedores)), contenedores)  # Crea un gráfico de barras
    plt.xlabel('Contenedores')  # Etiqueta el eje X
    plt.ylabel('Cantidad de Canicas')  # Etiqueta el eje Y
    plt.title('Simulación de la Máquina de Galton')  # Título del gráfico
    plt.show()  # Muestra el gráfico

# Ejecuta la simulación y grafica los resultados
contenedores = contar_canicas()
graficar_histograma(contenedores)
