from django.urls import path, include
from . import views

urlpatterns = [
    #include bao gồm tất cả các file của polls
    # path('polls/',include('polls.urls')),
    path('', views.index, name = 'index'),
    # path('introduce/',views.introduce, name='introduce')
    path("createView/", views.create_view, name = 'createView')
]
