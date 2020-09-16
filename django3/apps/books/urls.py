
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'books'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',views.list,name='list'),
    path('del_book/<int:id>',views.del_book,name='del1'),
    path('del_book2/<int:id>',views.del_book2,name='del2'),
    path('create/', views.create_book, name='create'),
    path('lists/', views.BookView.as_view(), name='lists'),
]
