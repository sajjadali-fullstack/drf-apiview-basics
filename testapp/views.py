from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views / business logic here. 👇

class TestAPIView(APIView):  # TestAPIView is a child class of APIView
    def get(self, request, *args, **kwargs):
        coding = ['python', 'java', 'C#', 'javaScript', 'C++']

        # Response class is responsible to convert python dict to json_data
        return Response({'msg':'Happy Coding', 'coding':coding})
