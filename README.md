Simulación de la Máquina de Galton /  Proyecto del Ucamp Proyecto Fundamentos de Python M3
Este repositorio contiene el código y la explicación de mi proyecto de simulación de la Máquina de Galton, un mecanismo diseñado por Francis Galton en el siglo XIX para ilustrar la aproximación de la distribución binomial a la distribución normal.

Introducción
La Máquina de Galton es un dispositivo que demuestra cómo, al lanzar un número grande de canicas a través de un sistema de obstáculos donde tienen igual probabilidad de ir hacia la izquierda o la derecha, el resultado final tiende a formar una distribución en forma de campana. Este proyecto implementa una simulación en Python para demostrar este concepto.

Características del Proyecto Simulación de la Máquina de Galton
Simular el recorrido de 3000 canicas a través de 12 niveles de obstáculos.
Calcular el contenedor final donde cae cada canica.
Generar un histograma para representar la distribución de las canicas en los contenedores.
Guardar los resultados en un archivo de texto para análisis posterior.
Usar funciones bien definidas para modularizar el código:
simular_canicas: Calcular la trayectoria y posición final de las canicas.
graficar_histograma: Generar el gráfico de barras con los resultados.
guardar_resultados: Guardar los resultados en un archivo de texto.
