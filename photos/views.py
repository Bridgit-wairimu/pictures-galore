from django.shortcuts import render,redirect
from .models import Image,Category,Location
from django.http  import HttpResponse, Http404

# Create your views here.
def welcome(request):
    return render( request ,'welcome.html')


def photos(request):
    
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'welcome.html',{'images': images[::-1], 'locations':locations})


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
                
        message = 'No searches yet'
        return render(request, 'search.html',{"message": message})


def single(request,category_name,image_id):
    title = 'Image'
    locations = Location.objects.all()
    image_category = Image.objects.filter(image_category_name = category_name)
    try:
        image = Image.objects.get(id= image_id)
    except DoesNotExist:
        raise Http404()
    
    return render(request,"single.html",{'title':title,"image":image, "locations":locations, "image_category":image_category})
    