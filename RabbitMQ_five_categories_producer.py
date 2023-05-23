import pika, datetime, random, json, time, threading, logging
from datetime import datetime

def producer_five_categories(name, category):

    trago = []
    with open('data.txt', 'r') as data:
        for linea in data:
            trago.append(linea)
    numero_aleatorio = random.randint(0, len(trago) - 1)
    dt = datetime.now()
    time_p = datetime.timestamp(dt)
    data = {
        'name': name,
        'timestamp': time_p,
        'user_id': random.randint(20000, 100000),
        'drink_name': trago[numero_aleatorio]
    }
    print(f"Enviando a la cola: {category}")
    message = json.dumps(data)
    queue_name = f"queue{category}"
    queues[int(category) - 1].basic_publish(exchange='', routing_key=queue_name, body=message)

    print(message)
    time.sleep(0.3)

def threads_five_categories(cantidad):
    threads = list()

    for index in range(cantidad):
        categoria = random.randint(1,5)
        x = threading.Thread(target=producer_five_categories(index,categoria), args=(),)
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()


connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
# Establecemos 5 canales de coneccion diferentes
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

threads_five_categories(100)
# Close the connection
connection.close()