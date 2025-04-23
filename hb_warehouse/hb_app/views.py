from django.shortcuts import render
from .models import brand
# Create your views here.
def index(request):
    brands = brand.objects.all()
    context = {'brands': brands}
    return render(request, 'warehouse/index.html', context)