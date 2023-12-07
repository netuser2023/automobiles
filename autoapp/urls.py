from django.urls import path
from . import views

urlpatterns = [
    path('automobiles/', views.automobiles, name='posts'),
    path('auto/<str:pk>', views.auto, name="post"),
    path('postdelete/<str:pk>', views.postdelete, name='postdelete'),
]