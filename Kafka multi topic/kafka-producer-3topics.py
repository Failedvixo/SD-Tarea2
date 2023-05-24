from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging
import sys
import random
import threading
from datetime import datetime
import redis


fake=Faker()


logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

p=Producer({'bootstrap.servers':'localhost:9092'})

#####################

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)
        
#####################
print('Kafka Producer has been initiated...')

def producer(name):
    trago = []
    with open('data.txt','r') as data:
        for linea in data:
            trago.append(linea)
    
    #182
    numero = len(trago)-157
    #numero = 2
    for i in range(numero):
        dt = datetime.now()
        time_p = datetime.timestamp(dt)
        data={
            'name': name,
            'timestamp': time_p,
            'user_id': fake.random_int(min=20000, max=100000),
            'drink_name': trago[i]
        }
        m=json.dumps(data)
        t = random.randint(0,2)
        topic = f"Tragos{t+1}"
        p.poll(1)
        p.produce(topic ,m.encode('utf-8'),callback=receipt)
        p.flush()
        time.sleep(3)

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    threads = list()
    
    number_of_producers = 1000
    
    for index in range(number_of_producers):
        x = threading.Thread(target=producer, args=(index,))
        threads.append(x)
        x.start()
        
    for index, thread in enumerate(threads):
        thread.join()
    
        
if __name__ == '__main__':
    main()
