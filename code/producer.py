from kafka import KafkaProducer
from kafka.errors import KafkaError
from time import sleep
from json import dumps
import os
import csv


topic_serializer = lambda x: dumps(x).encode('utf-8')

def write_in_topic(topic_name: str, filename: str) -> None:
    counter = 0
    future = None
    kafka_broker = 'localhost:9092'
    filepath = os.getcwd() + '/inputs/' + filename

    producer = KafkaProducer(bootstrap_servers=[kafka_broker], value_serializer=topic_serializer)

    with open(filepath, encoding = "ISO-8859-1") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                for row in reader:
                    counter += 1
                    print(row)
                    future = producer.send(topic_name, row)

    print(f'Nombre dinsertions dans: {counter}')

    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        print('Error writimg in Topic')
        pass

    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)


    write_in_topic(topic_name='toursTopic', filename='tours.csv')
    write_in_topic(topic_name='societeTopic', filename='societe.csv')
