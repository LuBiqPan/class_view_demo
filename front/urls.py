
from django.urls import path
from . import views


app_name = 'front'

urlpatterns = [
    path('add/', views.add_book, name='add_article'),
    path('list/', views.BookListView.as_view(), name='article_list'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', views.login, name='login')
]
