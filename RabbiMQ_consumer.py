import pika, sys, os

def main():
    #Coneccion al sv
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()

    #Creación cola, buena practica repetir la creación de la cola
    channel.queue_declare(queue='messages')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    #llama a callback en caso de recibir mensaje
    channel.basic_consume(queue='messages',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)