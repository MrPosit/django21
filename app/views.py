from django.shortcuts import render
from .models import Product, Review
from django.contrib.contenttypes.models import ContentType

def index(request):
    all_products = Product.objects.all()
    if request.method == 'POST':
        text = request.POST.get('text', None)
        product_id = request.POST.get('product', None)
        product = Product.objects.get(id=product_id)
        Review.objects.create(text=text, 
                              content_type=ContentType.objects.get_for_model(Product),
                              object_id=product.id)
        return render(request, 'index.html', {'products': all_products})    
    return render(request, 'index.html', {'products': all_products})
