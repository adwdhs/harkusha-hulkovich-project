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

        if not name or not price:
            return JsonResponse({"error": "Name and price are required."}, status=400)

        product = Product.objects.create(
            name=name,
            price=price,
            description=description
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
        product.save()

        return JsonResponse(model_to_dict(product), status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Delete(View):
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return JsonResponse({"message": "Product deleted successfully."}, status=200)