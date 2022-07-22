import pika
from configparser import ConfigParser


class RabbitMQ():
    def __init__(self, path):
        self.parse = ConfigParser()
        self.parse.read(path, encoding='utf8')
        self.username = self.parse.get('mq', 'username')
        self.pwd = self.parse.get('mq', 'pwd')
        self.ip = self.parse.get('mq', 'ip')
        self.port = self.parse.get('mq', 'port')
        self.connection = ''
        self.channel = ''

    # 消息队列服务的连接和队列的创建
    def create_connetion(self):
        self.credentials = pika.PlainCredentials(self.username, self.pwd)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.ip, self.port, '/', self.credentials))
        self.channel = self.connection.channel()
        # 创建一个名为balance的队列，对queue进行durable持久化设为True(持久化第一步)
        self.channel.queue_declare(queue='AIRequest', durable=True)

    def send_message(self, message, service):
        self.channel.basic_publish(
            exchange='',
            routing_key='AIRequest',
            body=message,  # 要发送的消息
            properties=pika.BasicProperties(type=service)  # 设置消息持久化(持久化第二步)，将要发送的消息的属性标记为2，表示该消息要持久化
        )

    def connection_close(self):
        self.connection.close()
