import matplotlib.pyplot as plt
import numpy as np


# Ruta de los archivos de texto
archivo1 = 'tiempos_kafka-latencia-50.txt' #kafka
archivo2 = 'tiempos_rabbitmq_five_categories.txt' #rabbitmq

# Leer los datos del archivo 1
y1 = []
with open(archivo1, 'r') as f:
    for linea in f:
        y1.append(float(linea))
x1 = np.arange(len(y1))

# Leer los datos del archivo 2
y2 = []
with open(archivo2, 'r') as f:
    for linea in f:
        y2.append(float(linea))
x2 = np.arange(len(y2))

# Graficar las curvas
plt.plot(x1, y1, label='Kafka')
plt.plot(x2, y2, label='RabbitMQ')

# Etiquetas y título del gráfico
plt.xlabel('Nro de mensaje')
plt.ylabel('Delta Tiempo')
plt.title('Grafico con 1000 Producers')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
