from django.shortcuts import render
from .models import Category, Sub_Category


def home(request):

    category = Category.objects.all()
    sub = Sub_Category.objects.all()

    context = {
        'categories': category,
        'sub': sub,
    }
    return render(request, 'index.html', context)
