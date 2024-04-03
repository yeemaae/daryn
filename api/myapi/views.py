from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DataBase
from django.core.serializers import serialize

data_base = DataBase.objects.all()


# Create your views here.
def index(request):
    field_names = [field.name for field in DataBase._meta.fields]
    data = [{field_name: getattr(obj, field_name) for field_name in field_names} for obj in data_base]
    return JsonResponse(data, safe=False)


def teacher(request):
    try:
        # Fetch all field names for the model
        field_names = [field.name for field in DataBase._meta.fields]

        # Fetch data from the database and construct dictionaries for each row
        data = [{field_name: getattr(obj, field_name) for field_name in field_names} for obj in DataBase.objects.all()]

        # Filter data based on the value of 'send_to_nobd' field
        filtered_data = [row for row in data if row.get('send_to_nobd') == 2]

        # Return the filtered data as JSON response
        return JsonResponse(filtered_data, safe=False)
    except Exception as e:
        # Print or log the exception for debugging
        print("An error occurred:", str(e))
        # Return an error response
        return JsonResponse({'error': 'An error occurred'}, status=500)


def student(request):
    try:
        # Fetch all field names for the model
        field_names = [field.name for field in DataBase._meta.fields]

        # Fetch data from the database and construct dictionaries for each row
        data = [{field_name: getattr(obj, field_name) for field_name in field_names} for obj in DataBase.objects.all()]

        # Filter data based on the value of 'send_to_nobd' field
        filtered_data = [row for row in data if row.get('send_to_nobd') == 1]

        # Return the filtered data as JSON response
        return JsonResponse(filtered_data, safe=False)
    except Exception as e:
        # Print or log the exception for debugging
        print("An error occurred:", str(e))
        # Return an error response
        return JsonResponse({'error': 'An error occurred'}, status=500)
