from rest_framework.serializers import ModelSerializer
from Remote.models import Show,Customer


class ListSerializersShow(ModelSerializer):
	class Meta:
		model=Show
		fields=[
			'S_id',
			'S_name',
			'Monday',
		]



class ListSerializersUser(ModelSerializer):
	class Meta:
		model=Customer
		fields=[
			'username',
			'password',
			'firstname',
			'lastname',
			'emailid',
			#'mobileno',
			'distributor',
		]
