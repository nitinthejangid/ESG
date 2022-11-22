from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import os

def getAnalyzedData(request):
    # Folder Path
    path = r"D:\WORK\test_json.json"
    with open(path, 'r') as f:
        data = json.load(f)

    return JsonResponse(data, safe=False)
