import threading
import queue
from producer import PwdProducer
from consumer import PasswordConsumer

queue = queue.Queue(maxsize=10)
condition = threading.Condition()

producer = PwdProducer(queue, condition)

consumer = PasswordConsumer(queue, condition)

producer.start()
consumer.start()

producer.join()
consumer.join()