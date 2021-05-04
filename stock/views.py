from django.shortcuts import render
import requests
import json

response = requests.get("http://api.coincap.io/v2/assets")
currencies = json.loads(response.text)


def stock(request):
    return render(request, "stock/stock.html")
