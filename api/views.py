from django.shortcuts import render, redirect
from django.views import View
from .models import Product


class Index(View): 
    def get(self, request): 
        products = Product.objects.all()
        context = {
            "products": products
        }

        return render(request, "index.html", context)

class Update(View):
    def get(self, request, pk): 
        product = Product.objects.get(id=pk)
        context = {
            "product_id": product.id,
            "product_name": product.name,
            "product_price": product.price,
            "product_description": product.description,
            "product_barcode": product.barcode,
            "product_vatRate": product.vatRate,
        }

        return render(request, "update.html", context)
    
    def post(self, request, pk): 
        product = Product.objects.get(id=pk)

        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        barcode = request.POST.get("barcode")
        vatRate = request.POST.get("vatRate")

        product.name = name
        product.price = price
        product.description = description
        product.vatRate = vatRate
        product.barcode = barcode
        product.save()

        return redirect('details', pk=pk)
    

class Add(View):
    def get(self, request): 
       

        return render(request, "add.html")
    
    def post(self, request): 
        
        if request.method == "POST":
            name = request.POST.get("name")
            price = request.POST.get("price")
            description = request.POST.get("description")
            barcode = request.POST.get("barcode")
            vatRate = request.POST.get("vatRate")
            product = Product.objects.create(name=name, price=price, description=description, barcode=barcode, vatRate=vatRate)
            id = product.id
            return redirect('details', pk=id)
        return render(request, "add.html")    
    


class Details(View):
    def get(self, request, pk): 
        product = Product.objects.get(id=pk)
        context = {
            "product_id": product.id,
            "product_name": product.name,
            "product_price": product.price,
            "product_description": product.description,
            "product_barcode": product.barcode,
            "product_vatRate": product.vatRate,
        }

        return render(request, "details.html", context)
    
class Delete(View):
    def get(self, request, pk): 
        product = Product.objects.get(id=pk)
        product.delete()

        return redirect('home')
    



      
      
