from django.urls import path
import fitforum.views as fitforum


urlpatterns = [
    path('',fitforum.index,name='fitforum'),
    path('fitness/',fitforum.fitness,name='fitness'),
    path('<int:tvno>/',fitforum.fitness,name='tv-url'),
    path('<int:tvno>/',fitforum.fitness,name='tvno-url'),
    path('yoga/',fitforum.yoga,name='yoga'),
    path('yoga/<int:tvno>/',fitforum.yoga,name='yoga-url'),
]
