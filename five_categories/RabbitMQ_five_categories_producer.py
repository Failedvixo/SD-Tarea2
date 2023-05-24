import pika, datetime, random, json, time, threading, logging
from datetime import datetime

# docker pull rabbitmq

def publish_message(channel, message, queue_random):
    channel.basic_publish(exchange='', routing_key=queue_random, body=message)


def producer(name):
    # Coneccion al sv
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    # Creación cola
    queues = []
    queues.append(connection.channel())
    queues[0].queue_declare(queue='queue1')

    queues.append(connection.channel())
    queues[1].queue_declare(queue='queue2')

    queues.append(connection.channel())
    queues[2].queue_declare(queue='queue3')

    queues.append(connection.channel())
    queues[3].queue_declare(queue='queue4')

    queues.append(connection.channel())
    queues[4].queue_declare(queue='queue5')

    trago = []
    with open('../data.txt', 'r') as data:
        for linea in data:
            trago.append(linea)

    # 182
    numero = len(trago) - 157
    queue_number = random.randint(0, 4)
    queue_random = f"queue{queue_number + 1}"
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
        publish_message(channel, message, queue_random)
        print(message)
        print(f"Dispositivo de categoría: {queue_number+1}")
        time.sleep(3)

    connection.close()


def threads():
    threads = list()
    number_of_producers = 1000

    for index in range(number_of_producers):
        x = threading.Thread(target=producer, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()


threads()

