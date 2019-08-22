import json

from kafka import KafkaProducer
from kafka.client import log
from kafka.errors import KafkaError


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)


def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception


def send_msg(topic, key, value):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    # Asynchronous by default
    bytes_key = json.dumps(key).encode('utf-8')
    bytes_value = json.dumps(value).encode('utf-8')
    future = producer.send(topic=topic, key=bytes_key, value=bytes_value)

    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        log.exception()
        pass

    # Successful result returns assigned partition and offset
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)
