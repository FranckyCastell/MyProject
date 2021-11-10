from django.shortcuts import render
from Shop.models import Category

# Create your views here.


def home(request):

    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'MyProjectApp/home.html', context)


def handler404(request, exception):  # HANDLER 404
    return render(request, 'MyProjectApp/404.html')


def handler500(request, *args, **argv):  # HANDLER 500
    return render(request, 'MyProjectApp/500.html', status=500)
