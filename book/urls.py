from django.urls import path
from . import views

# from .views import BookListView

urlpatterns = [
    path('home/', views.home, name='shop-home'),
    path('', views.all_books, name='shop-books'),
    # path('', BookListView.as_view(), name='shop-books'),
]
