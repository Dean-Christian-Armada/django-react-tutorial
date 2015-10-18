from rest_framework import serializers
from models import Band

# http://www.django-rest-framework.org/api-guide/serializers/
# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can be easily rendered into JSON, XML or other content types
class BandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Band