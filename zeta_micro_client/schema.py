from marshmallow import (Schema,
                         fields,
                         validate)


class CreateAccountHolderSchema(Schema):
    first_name = fields.Str(required=True, allow_none=False,
                            validate=validate.Length(min=1))
    middle_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)
    gender = fields.Str(
        required=True, validate=validate.OneOf(["Male", "Female"]))
    kyc_type = fields.Str(required=True, validate=validate.OneOf(
        ["VOTER_ID", "PAN", "PASSPORT", "DRIVING_LICENSE"]))
    kyc_value = fields.Str(required=True, validate=validate.Length(min=5))
    phone_number = fields.Str(
        required=True, validate=validate.Length(equal=10))
    dob = fields.Date(required=True)
    person_id = fields.UUID(required=False, allow_none=True)


class CreateAccountSchema(Schema):
    account_holder_id = fields.Str(required=True)
    accounts = fields.List(fields.Str(
        required=True, validate=validate.Length(min=5)))
    person_id = fields.UUID(required=False, allow_none=True)


class CreateResourceSchema(Schema):
    account_id = fields.Str(required=True, validate=validate.Length(equal=36))
    phone_number = fields.Str(
        required=True, validate=validate.Length(equal=13))
    person_id = fields.UUID(required=False, allow_none=True)


class UpdateResourceStatusSchema(Schema):
    status = fields.Str(required=True, validate=validate.OneOf(
        ["ACTIVE", "INACTIVE", "DELETED"]))
    description = fields.Str()


class DeleteResourceStatusSchema(Schema):
    status = fields.Str(required=True, validate=validate.OneOf(
        ["DELETED"]))


class UpdateFormFactorStatusSchema(Schema):
    status = fields.Str(required=True, validate=validate.OneOf(
        ["ACTIVE", "INACTIVE", "DELETED"]))
    description = fields.Str()


class SuspendAccountSchema(Schema):
    status = fields.Str(required=True)


class AccountDebitSchema(Schema):
    debit_account_id = fields.Str(required=True)
    amount = fields.Integer(required=True)
    remarks = fields.Str(required=True)
    attributes = fields.Dict(keys=fields.String(), values=fields.String())
    txn_id = fields.Str(required=True)


class AccountCreditSchema(Schema):
    credit_account_id = fields.Str(required=True)
    amount = fields.Integer(required=True)
    remarks = fields.Str(required=True)
    attributes = fields.Dict(keys=fields.String(), values=fields.String())
    txn_id = fields.Str(required=True)


class AccountTransferSchema(Schema):
    debit_account_id = fields.Str(required=True)
    credit_account_id = fields.Str(required=True)
    amount = fields.Integer(required=True)
    remarks = fields.Str(required=True)
    attributes = fields.Dict(keys=fields.String(), values=fields.String())
    txn_id = fields.Str(required=True)


class PersonAccountHolderSchema(Schema):

    person_id = fields.UUID(required=True)
    first_name = fields.String(required=True)
    middle_name = fields.String(required=True)
    last_name = fields.String(required=True)
    dob = fields.Date(required=True)
    gender = fields.String(required=True, validate=validate.OneOf(["Male", "Female"]))
    mobile_number = fields.String(required=True, validate=validate.Length(10))
    auth_type = fields.String(required=True, validate=validate.OneOf(["PAN", "DRIVING_LICENSE", "VOTER_ID", "PASSPORT"]))
    auth_data = fields.String(required=True, min=5)


class PersonAccountSchema(Schema):

    person_id = fields.UUID(required=True)
    account_holder_id = fields.String(required=True)
    name = fields.String(required=True)


class PersonBundleSchema(Schema):

    person_id = fields.UUID(required=True)
    account_holder_id = fields.String(required=True)
    name = fields.String(required=True)
    mobile_number = fields.String(required=True)
