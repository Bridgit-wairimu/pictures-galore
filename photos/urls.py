from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.photos,name = 'photos'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single,name='single')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

