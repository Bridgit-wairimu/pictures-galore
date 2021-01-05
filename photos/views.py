from django.shortcuts import render
from .models import Image

# Create your views here.
def welcome(request):
    return render( request ,'welcome.html')


def photos(request):
    
    images = Image.objects.all()
    return render(request, 'welcome.html',{'images': images[::-1]})


def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        return render(request, 'search.html',{"message": message})


