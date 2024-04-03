from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DataBase
from django.core.serializers import serialize


# Create your views here.
def index(request):
    data_base = DataBase.objects.all()
    field_names = [field.name for field in DataBase._meta.fields]
    data = [{field_name: getattr(obj, field_name) for field_name in field_names} for obj in data_base]
    return JsonResponse(data, safe=False)


def about(request):
    return HttpResponse("Page About Us!!!!")
