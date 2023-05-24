import pika, datetime, random, json, time, threading, logging
from datetime import datetime
#docker pull rabbitmq



def publish_message(channel, message):
    channel.basic_publish(exchange='', routing_key='messages', body=message)


def producer(name):
    # Coneccion al sv
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    # Creación cola
    channel.queue_declare(queue='messages')

    trago = []
    with open('data.txt','r') as data:
        for linea in data:
            trago.append(linea)
    
    #182
    numero = len(trago)-157

    for i in range(numero):
        dt = datetime.now()
        time_p = datetime.timestamp(dt)
        data = {
            'name': name,
            'timestamp': time_p,
            'user_id': random.randint(20000, 100000),
            'drink_name': trago[i]
        }

        message = json.dumps(data)
        publish_message(channel,message)
        print(message)
        time.sleep(3)

    connection.close()

def threads():

    threads = list()
    number_of_producers = 1

    for index in range(number_of_producers):
        x = threading.Thread(target=producer, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()


threads()

