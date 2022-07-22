# import random
import json


def message(OrderId, CommandIdentifier, PatientId, BirthDate, items, t, Gender):
    # 0015cdbf-833c-4a5f-9ce1-9c73dc263afe
    # OrderId = str(int(time.time()*1000))
    # NW=创建 CA=撤销 XO=更改
    # CommandIdentifiers = ['NW', 'CA', 'XO']
    # random.shuffle(CommandIdentifiers)
    # CommandIdentifier = CommandIdentifiers[0]
    # 20210725024957
    # OrderCreateTime = str(int(time.time()))
    # 就诊类型 住院 = RI 住院免疫 = II 住院生化 = IC 体检 = C 体检免疫 = TM 体检生化 = TC 急诊 = RS 急诊 = S 普通 = R 未知 = U 门诊 = RO 门诊免疫 = OI 门诊生化 = OC
    # 'RI', 'II', 'IC', 'C', 'TM', 'TC', 'RS', 'S', 'R', 'U', 'RO', 'OI', 'OC'
    # EncounterTypes = []
    # random.shuffle(EncounterTypes)
    # EncounterType = EncounterTypes[0]
    # 血液内科住院7
    # Department = '血液内科住院' + str(random.randint(1, 10))
    # 外周T细胞淋巴瘤9
    # Diagnosis = '外周T细胞淋巴瘤' + str(random.randint(1, 10))
    # b0cce118-d22e-44f9-9751-c52b2960219c
    # PatientId = str(int(time.time()*1000))
    # F=女性；M=男性；U=未知
    # 19530123
    # BirthDate = str(random.randint(1930, 2021))+str(random.randint(1, 12))+str(random.randint(1, 28))

    TestItems = []

    for item in items:
        stritem = {
            "ItemCode": item,
            "ItemName": "",
            "ReferenceRange": ""
        }
        TestItems.append(stritem)

    # 消息 先发送消息 再发送item item可以一个item消息中多个item 或者多个item消息 只要保证itemcode与message中的item一致

    message = {
        "RawData": "",
        "LisToInstrument": {
            "OrderId": OrderId,
            "SerialNumber": "",
            "CommandIdentifier": CommandIdentifier,
            "OrderCreateTime": t,
            "EncounterType": "R",
            "Department": "",
            "DepartmentCode": "wa",
            "Diagnosis": "测试120",
            "DiagnosisIcd": "",
            "PatientProfile": {
                "PatientId": PatientId,
                "BirthDate": BirthDate,
                "Gender": Gender
            },
            "TestItems": TestItems,
            "SendingApplication": "FAC1",
            "SendingFacility": "",
            "ReceivingApplication": "",
            "ReceivingFacility": "",
            "DateTimeOfMessage": "",
            "Security": "",
            "MessageType": "",
            "MessageControlId": "",
            "ProcessingId": "",
            "VersionId": "",
            "SequenceNumber": "",
            "ContinuationPointer": "",
            "AcceptAcknowledgementType": "",
            "ApplicationAcknowledgementType": "",
            "CountryCode": "",
            "CharacterSet": "",
            "PrincipalLanguageOfMessage": ""
        }
    }
    with open('middleware.json', 'w') as file:
        file.write(json.dumps(message))
    return str(json.dumps(message))
