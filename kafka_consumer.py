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
    i = 0
    
    while True:
        msg=c.poll(1.0) #timeout
        dt = datetime.now()
        time_p = datetime.timestamp(dt)
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        print(data)
        r.set(i,data)
        i+=1
        print("tiempo mensaje: ",time_p);
    c.close()
        
if __name__ == '__main__':
    main()