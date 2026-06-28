from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer
from rest_framework.viewsets import ViewSet

# Create your views / business logic here. 👇

class TestAPIView(APIView):  # TestAPIView is a child class of APIView
    # GET
    def get(self, request, *args, **kwargs):
        coding = ['python', 'java', 'C#', 'javaScript', 'C++']

        # Response class is responsible to convert python dict to json_data
        return Response({'msg':'Happy Coding', 'coding':coding})

    # POST
    def post(self, request, *args, **kwargs):
        serializer =  NameSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = f'Hey {name}, Hapy ending of DRF classes'
            return Response({'msg':msg})
        else:
            return Response(serializer.errors, status=400)

    # PUT'
    def put(self, request, *args, **kwargs):
        return Response({'msg':'This response is from PUT method APIView'})
    
    # PATCH
    def patch(self, request, *args, **kwargs):
        return Response({'msg':'This response is from PATCH method APIView'})
    
    # DELETE
    def delete(self, request, *args, **kwargs):
        return Response({'msg':'This response is from DELETE method APIView'})
    


class TestViewSet(ViewSet):
    def list(self, request):
        colours = ['red', 'green', 'blue']
        return Response({'msg':'Learning DRF', 'colours':colours})


    def retrive(self, request, pk=None):
        return Response({'msg':'This is from RETRIVE method'})

    def partial_update(self, request, pk=None):
        return Response({'msg':'This is from PARTIAL UPDATE method'})
        

    def destroy(self, request, pk=None):
        return Response({'msg':'This is from DESTROY method'})
        