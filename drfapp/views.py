from drfapp.models import Students
from drfapp.serializers import StudentsSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
# Create your views here.

class AboutStudent(ListModelMixin,CreateModelMixin,GenericAPIView  ):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        queryset = Students.objects.all()
        item_name = self.request.query_params.get('first_name')
        if item_name:
            queryset = queryset.filter(name = item_name)


    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)
