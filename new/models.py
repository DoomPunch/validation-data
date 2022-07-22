import json

__all__ = ['ItemResult', 'Item', 'Patient', 'OrderMessage', 'MiddlewareMessage']


class Item:
    def __init__(self, item_code: str):
        self.item_code = item_code
        self.item = {}

    def to_dict(self):
        self.item = {
            "ItemCode": self.item_code,
            "ItemName": "",
            "ReferenceRange": ""
        }


class ItemResult:
    def __init__(self, result: str, item_code: str):
        self.result = result
        self.item_code = item_code
        self.item = {}

    def to_dict(self):
        self.item = {
            "ResultValue": self.result,
            "ResultDescription": "",
            "Unit": "",
            "ReferenceRangeMin": "",
            "ReferenceRangeMax": "",
            "RackNo": "",
            "PositionNo": "",
            "InstrumentNo": "",
            "Module": "",
            "Comments": [],
            "ItemCode": self.item_code,
            "ItemName": "",
            "ReferenceRange": ""
        }

        return self.item


class Patient:
    def __init__(self, patient_id, birthdate, sex):
        self.patient_id = patient_id
        self.birthdate = birthdate
        self.sex = sex

    def to_dict(self):
        return {
            "PatientId": self.patient_id,
            "BirthDate": self.birthdate,
            "Gender": self.sex
        }


class OrderMessage:
    def __init__(self, order_id, time, command_identifier, patient: Patient, items, origin, department, diagnosis):
        self.order_id = order_id
        self.time = time
        self.command_identifier = command_identifier
        self.patient = patient
        self.items = items
        self.origin = origin
        self.department = department
        self.diagnosis = diagnosis
        self.order_message = {}

    def get_order_message(self):
        self.order_message = {
            "RawData": "",
            "LisToInstrument": {
                "OrderId": self.order_id,
                "SerialNumber": "",
                "CommandIdentifier": self.command_identifier,
                "OrderCreateTime": self.time,
                "EncounterType": self.origin,
                "Department": "",
                "DepartmentCode": self.department,
                "Diagnosis": self.diagnosis,
                "DiagnosisIcd": "",
                "PatientProfile": self.patient,
                "TestItems": self.items,
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


class MiddlewareMessage:
    def __init__(self, order_id, time, middleware, patient: Patient, items_result, origin, department, diagnosis):
        self.order_id = order_id
        self.time = time
        self.middleware = middleware
        self.patient = patient
        self.items_result = items_result
        self.origin = origin
        self.department = department
        self.diagnosis = diagnosis
        self.middleware_message = {}

    def get_middleware_message(self):
        self.middleware_message = {
            "RawData": "",
            "InstrumentToLis": {
                "OrderId": self.order_id,
                "ResultCreateTime": self.time,
                "EncounterType": "",
                "Department": "",
                "DepartmentCode": "",
                "Diagnosis": "",
                "DiagnosisIcd": "",
                "MiddlewareValidationResult": self.middleware,
                "PatientProfile": self.patient,
                "TestItemResults": self.items_result,
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

