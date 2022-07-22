import random
import json


def result(orderid, patient_id, birthday, itemss, t, gender):

    TestItemResults = []
    for item, test_result in itemss.items():
        stritem = {
            "ResultValue": test_result,
            "ResultDescription": "",
            "Unit": "",
            "ReferenceRangeMin": "",
            "ReferenceRangeMax": "",
            "RackNo": "",
            "PositionNo": "",
            "InstrumentNo": "",
            "Module": "",
            "Comments": [],
            "ItemCode": item,
            "ItemName": "",
            "ReferenceRange": ""
        }
        TestItemResults.append(stritem)

    # 自动审核结果  -1：不支持 0:不通过 1:通过
    Mvr = ['0', '1']
    # random.shuffle(Mvr)
    MiddlewareValidationResult = Mvr[1]
    ItemMessage = {
        "RawData": "",
        "InstrumentToLis": {
            "OrderId": orderid,
            "ResultCreateTime": t,
            "EncounterType": "",
            "Department": "",
            "DepartmentCode": "",
            "Diagnosis": "",
            "DiagnosisIcd": "",
            "MiddlewareValidationResult": MiddlewareValidationResult,
            "PatientProfile": {
                "PatientId": patient_id,
                "BirthDate": birthday,
                "Gender": gender
            },
            "TestItemResults": TestItemResults,
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
    with open('result.json', 'w') as file:
        file.write(json.dumps(ItemMessage))
    return str(json.dumps(ItemMessage))
