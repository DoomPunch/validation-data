import random
import sys

from message.message import message
from message.result import result
from tool.random_tool import RandomSelf
from tool.rabbitmq import RabbitMQ


a = sys.path[0].split('\\')
a = a[:len(a)-1]
a.append('config.ini')

path = '/'.join(a)

# 消息队列服务的连接和队列的创建
Rb = RabbitMQ(path)
Rb.create_connetion()


Services = {
    'LisToInstrument': 'Services.ServiceModel.Messages.LisToInstrumentDto, Services',
    'InstrumentToLis': 'Services.ServiceModel.Messages.InstrumentToLisDto, Services'
    }

# NW=创建 CA=撤销 XO=更改
CommandIdentifier = 'XO'

OrderId = '163106813665210'
PatientId = '13665210'
BirthDay = '19330813'
Gender = 'M'

time1 = RandomSelf.random_secondtime()
# 第二个时间在第一个时间后1-5小时
time2 = str(random.randint(1, 5)*10000 + int(time1))

# order
items = ['ABC']

# result
items2 = ['ABC']

Message = message(OrderId, CommandIdentifier, PatientId, BirthDay, items, time1, Gender)
Result = result(OrderId, PatientId, BirthDay, items2, time2, Gender)

# LisToInstrumentDto 申请
Rb.send_message(Message, Services['LisToInstrument'])
print(OrderId)

# InstrumentToLisDto 回传检验结果
Rb.send_message(Result, Services['InstrumentToLis'])

Rb.connection_close()
