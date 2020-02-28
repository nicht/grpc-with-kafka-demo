import json

from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


search_term = {"search_term": "Rodolfo"}

p.produce('category', json.dumps(search_term), callback=delivery_report)
p.produce('department', json.dumps(search_term), callback=delivery_report)
p.produce('user', json.dumps(search_term), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()
