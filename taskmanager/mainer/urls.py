from django.urls import path
from . import views

urlpatterns = [
    path('', views.kazakh, name='project'),
    path('kazakh1/',views.kazakh1, name='action'),
    path('kazakh2/',views.kazakh2, name='animation'),
    path('kazakh3/',views.kazakh3, name='comedy'),
    path('kazakh4/',views.kazakh4, name='horror'),
    path('kazakh7/', views.kazakh5, name='ch'),
    path('kazakh10/', views.kazakh6, name='kz'),
    path('kazakh12/', views.kazakh7, name='ru'),
    path('kazakh13/', views.kazakh8, name='us'),
    path('send/', views.send_message),
    # path('info/', views.info, name='info'),
    # path('insert/', views.insert, name='insert'),
    path('registration/', views.registration, name='registration'),
    # path('info/<int:pk>', views.NewsDetailView.as_view(), name='info-detail'),
    # path('info/<int:pk>/update', views.NewsUpdateView.as_view(), name='info-update'),
    # path('info/<int:pk>/delete', views.NewsDeleteView.as_view(), name='info-delete'),
    ]