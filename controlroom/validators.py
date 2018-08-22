from django.core.exceptions import ValidationError
from register.models import userinfo, paid_userinfo


def isnumber(value):
    list = value.split(',')
    numstring = ""
    for num in list:
        numstring += num
    try:
        val = int(numstring)
        if len(numstring) % 10 == 0:
            return value
        else:
            raise ValidationError("Enter valid phone numbers.")
    except ValueError:
        raise ValidationError("Enter valid phone numbers.")


def vaildusers(value):
    if value == "nil" or value == "":
        return value
    else:
        list = value.split(',')
        for user in list:
            if not userinfo.objects.filter(excelid=user).exists() and not paid_userinfo.objects.filter(excelid=user).exists():
                raise ValidationError("Wrong excelid : %s" % user)
    return value
