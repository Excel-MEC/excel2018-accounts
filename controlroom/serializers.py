from rest_framework.serializers import ModelSerializer
from .models import event
from register.models import userinfo,winners

class api(ModelSerializer):
	class Meta:
		model = userinfo
		fields = [
			'name',
			'phone',
		]

class winnerapi(ModelSerializer):
	class Meta:
		model = winners
		fields = [
		'position',
		'name',
		'college'
		]
