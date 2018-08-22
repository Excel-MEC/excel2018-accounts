from django.core.exceptions import ValidationError
from register.models import userinfo
from django.core.validators import EmailValidator
'''from validate_email import validate_email'''


def redundantmail(value):
    qs_exists = userinfo.objects.filter(email=value).exists()
    if qs_exists:
        raise ValidationError("This mail id is aldready registered.")
    else:
        return value


def redundantmailforpaid(value):
    if value == "":
        return value
    qs_exists = paid_userinfo.objects.filter(email=value).exists()
    if qs_exists:
        raise ValidationError("This mail id is aldready registered.")
    else:
        return value


def validatemail(value):
	is_valid = validate_email(value,verify=True)
	if is_valid:
		return value
	raise ValidationError("Enter a valid email address.")

def number(value):
	try:
		val = int(value)
		return val
	except ValueError:
		raise ValidationError("Enter a valid phone number.")

def redundantnum(value):
    qs_exists = userinfo.objects.filter(phone=value).exists()
    if qs_exists:
        raise ValidationError("This phone number aldready exists.")
    else:
        return value


def redundantnumforpaid(value):
	qs_exists=paid_userinfo.objects.filter(phone=value).exists()
	if qs_exists:
		raise ValidationError("This phone number aldready exists.")
	else:
		return value
