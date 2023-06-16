from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
def student_api(request):
    if request.method == "GET":
        print("gtfghg")
        json_data = request.body
        print("json data...", json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        print("id", id)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializers(stu)
            # json_data = JSONRenderer().render(serializer.data)
            # return  HttpResponse(json_data,content_type = 'application/json')
            return JsonResponse(serializer.data,safe=False)

        else:
            stu = Student.objects.all()
            serializer = StudentSerializers(stu, many=True)
            return JsonResponse(serializer.data,safe=False)
        
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()



