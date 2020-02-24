from rest_framework import serializers
from django.contrib.auth.models import User
from classes.models import Classroom, Student

#
# class UserLoginSerializer(serializers.Serializer):
#     ...
#
#     def validate(self, data):
#         my_username = data.get('username')
#         my_password = data.get('password')
#
#         try:
#             user_obj = User.objects.get(username=my_username)
#         except:
#             raise serializers.ValidationError("This username does not exist")
#
#         if not user_obj.check_password(my_password):
#             raise serializers.ValidationError("Incorrect username/password combination! Noob..")
#         return data

class ClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'name', 'year', 'teacher', 'id']


class ClassroomDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'subject', 'year', 'teacher', 'id']



class UpdateClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'name', 'year']


class CreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'name', 'year', 'teacher']
