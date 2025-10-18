import json
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from api.models import Product


def parse_body(request):
    
    try:
        return json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return request.POST


@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
    
    def get(self, request):
        products = list(Product.objects.values())
        return JsonResponse(products, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Details(View):
    
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        return JsonResponse(model_to_dict(product), status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Add(View):
    
    def post(self, request):
        data = parse_body(request)
        name = data.get("name")
        price = data.get("price")
        description = data.get("description")
        vatRate = data.get("vatRate")
        barcode = data.get("barcode")

        if not name or not price or not barcode:
            return JsonResponse({"error": "Name, barcode and price are required."}, status=400)

        product = Product.objects.create(
            name=name,
            price=price,
            description=description,
            barcode=barcode,
            vatRate=vatRate
        )
        return JsonResponse(model_to_dict(product), status=201)


@method_decorator(csrf_exempt, name='dispatch')
class Update(View):
   
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        data = parse_body(request)

        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.description = data.get("description", product.description)
        product.vatRate = data.get("vatRate", product.vatRate)
        product.barcode = data.get("barcode", product.barcode)
        product.save()

        return JsonResponse(model_to_dict(product), status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Delete(View):
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return JsonResponse({"message": "Product deleted successfully."}, status=200)