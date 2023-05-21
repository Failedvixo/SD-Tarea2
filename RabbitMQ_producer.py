import pika

#docker pull rabbitmq

#Coneccion al sv
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

#Creación cola
channel.queue_declare(queue='messages')

channel.basic_publish(exchange='',
                      routing_key='messages',
                      body='test')
print(" Mensaje enviado ")

connection.close()