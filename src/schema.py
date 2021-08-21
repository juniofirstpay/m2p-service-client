from marshmallow import (Schema, 
                        fields, 
                        validate)


def CreateAccountHolderSchema(Schema):
    first_name=fields.Str(required=True, allow_none=False, validate=validate.Length(min=1))
    middle_name=fields.Str(required=True, allow_none=False)
    last_name=fields.Str(required=True, allow_none=False)
    gender=fields.Str(required=True, validate=validate.OneOf(["Male", "Female"]))
    kyc_type=fields.Str(required=True, validate=validate.OneOf(["VOTER_ID", "PAN", "PASSPORT", "DRIVING_LICENCE"]))
    kyc_value=fields.Str(required=True, validate=validate.Length(min='5'))
    mobile_number=fields.Str(required=True, validate=validate.Length(equal='10'))
    birth_date=fields.Date("YYYY-MM-DD")


def CreateAccountSchema(Schema): 
    account_holder_id=fields.Str(required=True)
    account_name=fields.Str(required=True, validate=validate.Length(min=36))


def CreateResourceSchema(Schema): 
    account_holder_id=fields.Str(required=True)
    account_id=fields.Str(required=True, validate=validate.Length(equal=36))
    mobile_number=fields.Str(required=True, validate=validate.Length(equal=10))


def UpdateResourceStatusSchema(Schema):
    status = fields.Str(required=True, validate=validate.OneOf["ACTIVE","INACTIVE", "DELETED"])
    description = fields.Str()

def UpdateFormFactorStatusSchema(Schema):
    status = fields.Str(required=True, validate=validate.OneOf["ACTIVE","INACTIVE", "DELETED"])
    description = fields.Str()