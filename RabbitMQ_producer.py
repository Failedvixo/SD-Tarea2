import pika, datetime, random, json, time
from datetime import datetime
#docker pull rabbitmq

def producer(name):
    trago = []
    with open('data.txt', 'r') as data:
        for linea in data:
            trago.append(linea)

    numero = 3

    for i in range(numero):
        numero_aleatorio = random.randint(0,len(trago)-1)
        dt = datetime.now()
        time_p = datetime.timestamp(dt)
        data={
            'name': name,
            'timestamp': time_p,
            'user_id': random.randint(20000, 100000),
            'drink_name': trago[numero_aleatorio]
        }

        message = json.dumps(data)
        channel.basic_publish(exchange='', routing_key='messages', body=message)
        time.sleep(3)


#Coneccion al sv
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

#Creación cola
channel.queue_declare(queue='messages')

producer("sex")
connection.close()