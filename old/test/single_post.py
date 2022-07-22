# import json
import pika
import random
from old.tool.random_message import randomMessage
from old.tool.random_item import randomItem
from old.tool.random_tool import RandomSelf


# 远程rabbitmq服务的配置信息
username = 'labai'
pwd = 'labai'
ip_addr = '139.217.234.156'
port_num = 5672

# 消息队列服务的连接和队列的创建
credentials = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(ip_addr, port_num, '/', credentials))
channel = connection.channel()
# 创建一个名为balance的队列，对queue进行durable持久化设为True(持久化第一步)
channel.queue_declare(queue='AIRequest', durable=True)


OrderId = '162942399722805'
CommandIdentifier = 'NW'
PatientId = '248842'
BirthDate = '19580601'
Gender = 'F'

items = ['ALP', 'BUN', 'AST']
# result
items2 = ['ALP', 'BUN', 'AST']

time1 = RandomSelf.random_secondtime()
# 第二个时间在第一个时间后1-5小时
time2 = str(random.randint(1, 5)*10000 + int(time1))

Message = randomMessage.randomMassage(OrderId, CommandIdentifier, PatientId, BirthDate, items, time1, Gender)

Items = randomItem.randomItem(OrderId, PatientId, BirthDate, items, time2, Gender)

# with open('json/listoinstrument/massage_sample.json', 'r', encoding='utf8')as ms:
#     massage = str(json.load(ms))
# print(massage)

# item = ''
# with open('json/instrumenttolis/item_sample.json', 'r', encoding='utf8')as it:
#     item = str(json.load(it))
# print(item)

# LisToInstrumentDto 发送申请
# channel.basic_publish(
#         exchange='',
#         routing_key='AIRequest',
#         body=Message,  # 要发送的消息
#         # type LisToInstrumentDto massage
#         properties=pika.BasicProperties(type='Services.ServiceModel.Messages.LisToInstrumentDto, Services', correlation_id='xxxxxx1', delivery_mode=2)  # 设置消息持久化(持久化第二步)，将要发送的消息的属性标记为2，表示该消息要持久化
#     )  # 向消息队列发送一条消息

# InstrumentToLisDto 回传检验结果
channel.basic_publish(
        exchange='',
        routing_key='AIRequest',
        body=Items,  # 要发送的消息
        # type InstrumentToLisDto items
        properties=pika.BasicProperties(type='Services.ServiceModel.Messages.InstrumentToLisDto, Services', correlation_id='xxxxxx1', delivery_mode=2)  # 设置消息持久化(持久化第二步)，将要发送的消息的属性标记为2，表示该消息要持久化
    )  # 向消息队列发送一条消息

print("Success")
connection.close()
