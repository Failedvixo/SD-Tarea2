import matplotlib.pyplot as plt
import numpy as np


# Ruta de los archivos de texto
archivo1 = 'tiempos_kafka-latencia-25.txt' #kafka
archivo2 =  'tiempos_rabbitmq-latencia-25.txt' #rabbitmq
archivo3 = 'tiempos_kafka-latencia-50.txt' #kafka
archivo4 = 'tiempos_rabbitmq-latencia-50.txt' #rabbitmq
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

y3 = []
with open(archivo3, 'r') as f:
    for linea in f:
        y3.append(float(linea))
x3 = np.arange(len(y3))

y4 = []
with open(archivo4, 'r') as f:
    for linea in f:
        y4.append(float(linea))
x4 = np.arange(len(y4))

# Graficar las curvas
plt.plot(x1, y1, label='Kafka 25 mensajes')
plt.plot(x2, y2, label='RabbitMQ 25 mensajes')
plt.plot(x3, y3, label='Kafka 50 mensajes')
plt.plot(x4, y4, label='RabbitMQ 50 mensajes')

# Etiquetas y título del gráfico
plt.xlabel('Nro de mensaje')
plt.ylabel('Delta Tiempo')
plt.title('Grafico con 1000 Producers')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
