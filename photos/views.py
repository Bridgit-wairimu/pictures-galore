from django.shortcuts import render
from .models import Image,Category,Location

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



# def location_filter(request, image_location):
#     location = Location.get_location_id(image_location)
#     images = Image.filter_by_location(image_location)
#     title = f'{location} Photos'
#     return render(request, 'location.html', {'title':title,'images':images,'location':location})


def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'pictures/location.html', {'location_images': images})


