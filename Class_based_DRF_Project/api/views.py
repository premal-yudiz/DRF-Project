from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from django.core import serializers

@csrf_exempt

def student_api(request):
    if request.method == "GET":
        print("gtfghg")
        json_data = request.body
        print("json data...", json_data)
        stream = io.BytesIO(json_data)
        # try:
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        print("id", id)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializers(stu)
            # json_data = JSONRenderer().render(serializer.data)
            # return  HttpResponse(json_data,content_type = 'application/json')
            return JsonResponse(serializer.data,safe=False)
        # except Exception as e:
        #     return HttpResponse(e)

        else:
            stu = Student.objects.all()
            serializer = StudentSerializers(stu, many=True)
            return JsonResponse(serializer.data,safe=False)
        
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        print("++++++++++++++++",stream)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializers(data=json_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            return JsonResponse(res,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)
        
    if request.method == "PUT":
        json_data = request.body
        print("json_data........",json_data)
        stream = io.BytesIO(json_data)
        print("stream.....",stream)
        pythondata = JSONParser().parse(stream)
        print("python data is...",pythondata)
        id = pythondata.get('id')
        print("id id ",id)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu,data=pythondata,partial=True)
        print("serializer....",serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated'}
            return JsonResponse(res,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)
        



    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id  = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg': 'deleted...'}
        return JsonResponse(res,safe=False)
    else:
        return JsonResponse(serializer.errors,safe=False)



        
    
            




