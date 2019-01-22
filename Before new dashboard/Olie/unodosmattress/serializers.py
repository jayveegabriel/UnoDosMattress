from rest_framework import serializers

from unodosmattress.models import Temperature, Beds,HeartRate

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Temperature
		fields = ('url', 'idTemperature', 'temperature','date','time')
		extra_kwargs = {
            'url': {
                'view_name': 'unodosmattress:temperature-detail',
           	}
	}
	def create(self, validated_data):
		todo = Temperature(
        	temperature=validated_data.get('temperature', ''),
        	date=validated_data.get('date', ''),
        	time=validated_data.get('time', ''),
			idPatient_id=2,
        	)
		todo.save()
		return todo

class HeartRateSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = HeartRate
		fields = ('url', 'idHeartRate', 'heartRate','date','time')
		extra_kwargs = {
            'url': {
                'view_name': 'unodosmattress:heartRate-detail',
           	}
	}
	def create(self, validated_data):
		hr = HeartRate(
        	heartRate=validated_data.get('heartRate', ''),
        	date=validated_data.get('date', ''),
        	time=validated_data.get('time', ''),
			idPatient_id = 2,
        	)
		hr.save()
		return hr

# class NotificationSerializer(serializers.HyperlinkedModelSerializer):
#
# 	class Meta:
# 		model = Notification
# 		fields = ('url', 'idBeds')
# 		extra_kwargs = {
#             'url': {
#                 'view_name': 'unodosmattress:notification-detail'
#            	}
# 	}
# 	def create(self, validated_data):
# 		n = Notification(
#         	idBeds=validated_data.get('idBeds', ''),
#         	)
# 		n.save()
# 		return n




class BedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Beds
		fields = ('url','bedNumber','bedStatus')
		extra_kwargs = {
			'url':{
				'view_name': 'unodosmattress:bed-detail'
			}
		}

	def create(self, validated_data):
		beds = Beds.objects.all()
		i = 1
		isOkay = False
		bedNumber = 0
		while isOkay == False:
			wew = 0
			for x in range(0, len(beds)):

				if(beds[x].bedNumber == i):
					wew = 1
			if wew == 0:
				bedNumber = i
				isOkay = True
			i = i + 1


		bed = Beds(
        	bedNumber= bedNumber,
        	bedStatus='Pending',
        	)
		bed.save()
		return bed
