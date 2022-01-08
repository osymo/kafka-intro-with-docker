docker network create lightinvestNetwork --driver bridge

docker run -d --name zookeeper-server --network lightinvestNetwork -e ALLOW_ANONYMOUS_LOGIN=yes  bitnami/zookeeper:latest

docker run -d --name kafka-server --network lightinvestNetwork -e ALLOW_PLAINTEXT_LISTENER=yes -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest

docker run -d --name kafka-client --network lightinvestNetwork -e ALLOW_PLAINTEXT_LISTENER=yes -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest




docker exec -it kafka-client bash
kafka-topics.sh --list --bootstrap-server localhost:9092
kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic societeTopic --bootstrap-server localhost:9092
kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic toursTopic --bootstrap-server localhost:9092

kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic playground --bootstrap-server localhost:9092
kafka-console-producer.sh --topic playground --bootstrap-server localhost:9092
kafka-console-consumer.sh --topic playground --from-beginning --bootstrap-server localhost:9092


docker exec -it kafka-node-1 /bin/kafka-topics --list --bootstrap-server localhost:9092

docker exec -it kafka-node-1 /bin/kafka-topics --create --partitions 1 --replication-factor 1 --topic toursTopic --bootstrap-server localhost:9092
docker exec -it kafka-node-1 /bin/kafka-topics --create --partitions 1 --replication-factor 1 --topic societeTopic --bootstrap-server localhost:9092

docker run --tty --network veilletechnologique_default  confluentinc/cp-kafkacat kafkacat -b kafka-node-1:29092  -L