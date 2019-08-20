import kafka


def pub_msg_login(value):
    producer = kafka.KafkaProducer(bootstrap_servers=['localhost:9092'])
    value_bytes = bytes(value, encoding='utf-8')
    message = producer.send(topic='login', value=value_bytes)
    print(producer.config)
    print(message)


def publish_message(topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        connect_kafka_producer().send(topic_name, key=key_bytes, value=value_bytes)
        connect_kafka_producer().flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = kafka.KafkaProducer(bootstrap_servers=['localhost:9092'])
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer
