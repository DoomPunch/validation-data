import time
import random
import csv
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
Rb.create_connection()

services = {
    'LisToInstrument': 'Services.ServiceModel.Messages.LisToInstrumentDto, Services',
    'InstrumentToLis': 'Services.ServiceModel.Messages.InstrumentToLisDto, Services'
    }

'''
创建: NW
撤销: CA
更改: XO
'''
CommandIdentifier = ['NW', 'CA', 'XO']

# 创建csv文件，并生成csv表头
f = open('测试数据.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["id", "listoins", "instolis"])

for i in range(50):
    OrderId = RandomSelf.random_id()

    time1 = RandomSelf.random_secondtime()
    # 第二个时间在第一个时间后1-5小时
    time2 = str(random.randint(1, 5)*10000 + int(time1))

    PatientId = int(OrderId) % 100000000
    # PatientId = 9876543210
    BirthDay = RandomSelf.random_birthday()
    # BirthDay = '19990808'
    Gender = RandomSelf.random_gender()
    # Gender = 'UNKNOWN'

    OrderId2 = RandomSelf.random_id()
    PatientId2 = int(OrderId2) % 100000000
    BirthDay2 = RandomSelf.random_birthday()
    Gender2 = RandomSelf.random_gender()
    # Gender = 'U'

    # order lis
    # items = ['CRP', 'AFU', 'HBDH', 'GGT', 'LDH', 'LAP', 'PA', 'CO2', 'CHOL', 'TBA', 'TBIL', 'ADA', 'ALB', 'ALBD',
    #          'ALP', 'ALT', 'APO_A', 'APO_B', 'ASLO', 'AST', 'CA', 'CH50', 'CK', 'CKMB', 'CL', 'CREA', 'CYSC', 'DBIL',
    #          'EFT', 'FRUC', 'GA', 'GAD', 'GLU', 'HDL_C', 'Hemoliti', 'HP', 'HSCRP', 'Icteric', 'K', 'LDL_C', 'Lipaemic',
    #          'LPA', 'MG', 'NA', 'PHOS', 'RF', 'SAA', 'sdLDL-C', 'TG', 'TP', 'UA', 'UREA', 'HCY']
    # items = ['ALB', 'GA']
    items = {
        # 'ABC': '1.0',

        # 'TG': '0.80',
        # 'GLU': '3.3',
        # 'TP': '67',
        # 'UA': '772',
        # 'APO_A': '1.5',
        # 'APO_B': '1.02',
        # 'CREA': '266',
        # 'DBIL': '4',
        # 'ADA': '14',
        # 'sdLDL-C': '120',
        # 'HDL_C': '1.16',  # > 1.15
        # 'ALB': '45',
        # 'ALP': '88',
        # 'ALT': '40',
        # 'AST': '20',
        # 'HBDH': '73',
        # 'GGT': '40',
        # 'LDH': '130',
        # 'LAP': '30',
        # 'PA': '350',
        # 'CO2': '19.5',
        # 'CHOL': '3.39',  # 3.38-5.2
        # 'TBA': '5.5',
        # 'TBIL': '5',
        'CK': '1',
        'CKMB': '20',
        'UREA': '42.2',

        # 'EFT': '200',
        # 'FRUC': '250',
        # 'GA': '13',
        # 'GAD': '200',
        # 'HCY': '14',
        # 'CRP': '4',
        # 'AFU': '35',
        # 'CA': '2.5',
        # 'CH50': '24',
        # 'ASLO': '100',
        # 'RF': '13',
        # 'NA': '140',
        # 'LPA': '200',
        # 'Lipaemic': '7',
        # 'LDL_C': '1.8',  # < 3.37
        # 'Icteric': '4',
        # 'HSCRP': '3',
        # 'Hemoliti': '8',
        # 'CYSC': '1.1',
        # 'ALBD': '300',
        # 'HP': '14',
        # 'K': '5',
        # 'MG': '0.77',
        # 'PHOS': '1.2',
        # 'SAA': '8',
        # 'CL': '100',
    }
    # items = ['TG']
    # mid
    # result middle
    # items2 = []
    # items2 = ['BUN']
    Message = message(OrderId, CommandIdentifier[0], PatientId, BirthDay, items, time1, Gender)
    # Message2 = message(OrderId2, CommandIdentifier[0], PatientId2, BirthDay2, items3, time1, Gender)
    Result = result(OrderId, PatientId, BirthDay, items, time2, Gender)
    # Result2 = result(OrderId2, PatientId2, BirthDay2, items3, time2, Gender2)

    # xo_item = ['ABC']
    # xo_message = message(OrderId, CommandIdentifier[2], PatientId, BirthDay, xo_item, time1, Gender)
    # xo_result = result(OrderId, PatientId, BirthDay, xo_item, time2, Gender)

    # ca_item = []
    # ca_message = message(OrderId, CommandIdentifier[1], PatientId, BirthDay, ca_item, time1, Gender)

    # 在csv插入数据
    csv_writer.writerow([OrderId,  Message, Result])

    for j in range(1):
        # LisToInstrumentDto 申请
        # print("第一次message")
        Rb.send_message(Message, services['LisToInstrument'])
        print(str(i) + ' : ' +str(OrderId))
        # print(PatientId + ' - ' + BirthDay + ' - ' + Gender)

        # time.sleep(5)
        # print("第二次message")
        # Rb.send_message(Message2, services['LisToInstrument'])
        # print(OrderId2)
        time.sleep(0.01)

        # InstrumentToLisDto 回传检验结果
        # print("第一次result")
        Rb.send_message(Result, services['InstrumentToLis'])
        # time.sleep(10)
        # print("第二次result")
        # Rb.send_message(Result2, services['InstrumentToLis'])

        # 是否XO
        if False:
            print('XO')
            Rb.send_message(xo_message, services['LisToInstrument'])
            time.sleep(10)
            Rb.send_message(xo_result, services['InstrumentToLis'])
            csv_writer.writerow([OrderId,  xo_message, xo_result])

    # 是否CA
    # time.sleep(5)
    if False:
        print('CA')
        Rb.send_message(ca_message, services['LisToInstrument'])
    time.sleep(0.01)

Rb.connection_close()
f.close()
