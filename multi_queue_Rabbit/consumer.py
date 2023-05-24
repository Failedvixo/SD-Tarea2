import pika, sys, os, redis, time
from datetime import datetime

r = redis.Redis(host='localhost', port=6379)
f = open("tiempos_rabbitmq_improved.txt", "w+")


def main():
    # Coneccion al sv
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()

    # Creación cola, buena practica repetir la creación de la cola
    channel.queue_declare(queue='queue1')
    channel.queue_declare(queue='queue2')
    channel.queue_declare(queue='queue3')
    def callback(ch, method, properties, body):
        data = body.decode('utf-8')
        dt = datetime.now()
        time_p = datetime.timestamp(dt)

        print(" [x] Received %r" % body)
        data = body.decode('utf-8')
        real_data = {
            'name': eval(data)['name'],
            'drink_name': eval(data)['drink_name']
        }
        print("Tiempo Kafka: " + str(r.get(str(real_data))))
        tiempo_final = datetime.fromtimestamp(time_p)
        tiempo_principio = datetime.fromtimestamp(eval(data)['timestamp'])
        tiempo_demora = tiempo_final - tiempo_principio
        print("Tiempo Rabbit: " + str(tiempo_demora.total_seconds()))
        f.write(str(tiempo_demora.total_seconds()) + '\n')

    # llama a callback en caso de recibir mensaje
    channel.basic_consume(queue='queue1',
                          auto_ack=True,
                          on_message_callback=callback)
    channel.basic_consume(queue='queue2',
                          auto_ack=True,
                          on_message_callback=callback)
    channel.basic_consume(queue='queue3',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        f.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)




