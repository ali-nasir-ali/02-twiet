from django.contrib import admin
from django.urls import path

from tweets.views import (
    home_view , 
    tweet_detail_view, 
    tweet_list_view,
    tweet_create_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('create-tweet', tweet_create_view),
    path('tweets', tweet_list_view),
    path('tweets/<int:tweet_id>', home_view),

]  # at 1 hour mark
#     <a class="nav-item nav-link" href="{% url '' %}">To do list</a>
#     <a class="nav-item nav-link" href="{% url '' %}">About</a>
#     <a class="nav-item nav-link" href="{% url '' %}">Pricing</a>
#     <a class="nav-item nav-link" href="{% url '' %}">Contact</a>     
