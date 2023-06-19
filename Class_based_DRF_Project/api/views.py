from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


from django.utils.decorators import method_decorator
from django.views import View
@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args, **kwargs):
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
            return JsonResponse(serializer.data,safe=False)
        # except Exception as e:
        #     return HttpResponse(e)

        else:
            stu = Student.objects.all()
            serializer = StudentSerializers(stu, many=True)
            return JsonResponse(serializer.data,safe=False)
        
    def post(self,request,*args, **kwargs):
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
    
    def put(self,request,*args, **kwargs):
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
        
    def delete(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id  = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg': 'deleted...'}
        return JsonResponse(res,safe=False)
        

        



