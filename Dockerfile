FROM confluentinc/cp-kafka-connect
ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"
RUN confluent-hub install --no-prompt jcustenborder/kafka-connect-spooldir:latest