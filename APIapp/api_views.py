from django.shortcuts import render
from classes.models import Classroom, Student
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import UpdateClassroomSerializer, ClassroomSerializer, ClassroomDetailsSerializer,CreateSerializer

# class UserLoginAPIView(APIView):
# 	serializer_class = UserLoginSerializer
#
# 	def post(self, request):
# 		my_data = request.data
# 		serializer = UserLoginSerializer(data=my_data)
# 		if serializer.is_valid(raise_exception=True):
# 			valid_data = serializer.data
# 			return Response(valid_data, status=HTTP_200_OK)
# 		return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class APIListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer

class DetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class CreateView(CreateAPIView):
	serializer_class = CreateSerializer
	def perform_create(self, serializer):
		# classroom_id = self.kwargs.get("classroom_id")
		# classroom_obj = Flight.objects.get(id=classroom_id)
		serializer.save(teacher = self.request.user)


class UpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateClassroomSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class DeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
