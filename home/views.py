from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
# task no. 3
def home(request):
    comments=[
        {
            'name':'Ava',
            'age':'21'
        },
        {
            'name':'tanu',
            'age':"20"
        }
    ]
    return JsonResponse({'comments': comments})


