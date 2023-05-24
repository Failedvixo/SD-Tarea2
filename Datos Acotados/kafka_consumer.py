from confluent_kafka import Consumer
import redis
import time
from datetime import datetime
################
r = redis.Redis(host='localhost', port=6379)

c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})

print('Available topics to consume: ', c.list_topics().topics)

c.subscribe(['Tragos'])

################

def main():
    f = open("tiempos_kafka.txt","w+")
    while True:
        msg=c.poll(1.0) #timeout
        dt = datetime.now()
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        time_p = datetime.timestamp(dt)
        data=msg.value().decode('utf-8')
        print(data)
        tiempo_final = datetime.fromtimestamp(time_p)
        tiempo_principio = datetime.fromtimestamp(eval(data)['timestamp'])
        tiempo_demora = tiempo_final-tiempo_principio
        print(tiempo_demora)
        r.set(data,tiempo_demora.total_seconds())
        f.write(str(tiempo_demora.total_seconds()) + '\n')
    c.close()
    f.close()
        
if __name__ == '__main__':
    main()