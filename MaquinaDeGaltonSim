# Importar las bibliotecas necesarias
import random  # Usar para generar movimientos aleatorios de las canicas
import matplotlib.pyplot as plt  # Usar para graficar los resultados en un histograma

# Definir una función para simular el recorrido de las canicas
def simular_canicas(num_canicas, niveles):
    """
    Simula el recorrido de canicas en una máquina de Galton y calcula cuántas caen en cada contenedor.
    
    Argumentos:
        num_canicas (int): Cantidad total de canicas a lanzar.
        niveles (int): Número de niveles (o filas de obstáculos) en la máquina.
    
    Devuelve:
        list: Una lista con el conteo de canicas en cada contenedor.
    """
    # Crear una lista para representar los contenedores con ceros iniciales
    contenedores = [0] * (niveles + 1)

    # Simular el movimiento de cada canica
    for _ in range(num_canicas):
        posicion = niveles // 2  # Las canicas comienzan desde el centro
        
        # Iterar a través de los niveles, moviendo la canica aleatoriamente
        for _ in range(niveles):
            movimiento = random.choice([-1, 1])  # Elegir entre moverse izquierda (-1) o derecha (+1)
            posicion += movimiento  # Actualizar la posición de la canica
            
            # Asegurarse de que la posición no salga de los límites de los contenedores
            if posicion < 0:
                posicion = 0
            elif posicion > niveles:
                posicion = niveles
        
        # Incrementar el contador del contenedor final donde cae la canica
        contenedores[posicion] += 1

    return contenedores  # Devolver el conteo de canicas en cada contenedor

# Definir una función para graficar los resultados en un histograma
def graficar_histograma(contenedores):
    """
    Genera un histograma con los resultados de la simulación de la Máquina de Galton.
    
    Argumentos:
        contenedores (list): Lista con el conteo de canicas en cada contenedor.
    """
    # Crear un gráfico de barras para visualizar los resultados
    plt.bar(range(len(contenedores)), contenedores, color="lightblue", edgecolor="black")
    
    # Añadir un título y etiquetas a los ejes
    plt.title("Distribución de Canicas - Máquina de Galton", fontsize=16)
    plt.xlabel("Contenedor", fontsize=12)
    plt.ylabel("Número de Canicas", fontsize=12)
    
    # Mostrar el gráfico
    plt.show()

# Definir una función para guardar los resultados en un archivo de texto
def guardar_resultados(contenedores, archivo="resultados_galton.txt"):
    """
    Guarda los resultados de la simulación en un archivo de texto.
    
    Argumentos:
        contenedores (list): Lista con el conteo de canicas en cada contenedor.
        archivo (str): Nombre del archivo donde se guardarán los datos.
    """
    # Abrir el archivo en modo escritura
    with open(archivo, "w") as f:
        f.write("Contenedor\tCanicas\n")  # Escribir la cabecera
        for i, cantidad in enumerate(contenedores):
            f.write(f"{i}\t{cantidad}\n")  # Escribir el índice del contenedor y la cantidad de canicas

    print(f"Resultados guardados en {archivo}")  # Informar al usuario

# Parámetros de la simulación
NUM_CANICAS = 3000  # Definir cuántas canicas se lanzarán
NIVELES = 12  # Definir el número de niveles en la máquina

# Ejecutar la simulación
resultados = simular_canicas(NUM_CANICAS, NIVELES)

# Graficar los resultados
graficar_histograma(resultados)

# Guardar los resultados en un archivo
guardar_resultados(resultados)
