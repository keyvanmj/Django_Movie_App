from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Main.urls',namespace='Main')),
    path('accounts/',include('accounts.urls',namespace='Accounts')),
    path('movies/', include('Movie_app.urls', namespace='Movies')),
    path('', include('Person_app.urls', namespace='Person')),
    path('vote/', include('Vote_app.urls', namespace='Vote')),
    path('search/', include('Search.urls', namespace='Search')),
    path('category/',include('Movie_Category.urls',namespace='Category')),
    path('series/',include('Series_app.urls',namespace='Series')),
    path('favourite/',include('Favourite_App.urls',namespace='Favourite')),
    path('comments/',include('Comment_app.urls',namespace='Comments')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

