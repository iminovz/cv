from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cv'),
    # path('<about_me>', views.get_info),
]
