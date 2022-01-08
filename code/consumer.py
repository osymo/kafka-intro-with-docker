from kafka import KafkaConsumer


def read_from_topic(topic_name: str) -> None:
    counter = 0
    kafka_broker = 'localhost:9092'
    consumer = KafkaConsumer(topic_name, 
                            bootstrap_servers=[kafka_broker], 
                            auto_offset_reset='earliest', 
                            enable_auto_commit=False,
                            consumer_timeout_ms=1000)
    for msg in consumer:
        counter+=1
        print(msg)

    print(f'Nombre de lignes lues: {counter}')


read_from_topic('toursTopic')
read_from_topic('societeTopic')

        