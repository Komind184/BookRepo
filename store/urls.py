from django.urls import path
from . import views
from .views import *

app_name = 'store'

urlpatterns = [
	path('index/', views.index, name = "index"),
	path('', views.signin, name="signin"),
	path('logout', views.signout, name="signout"),
	path('registration', views.registration, name="registration"),
	path('book/<int:id>', views.get_book, name="book"),
	path('books', views.get_books, name="books"),
	path('category/<int:id>', views.get_book_category, name="category"),
	path('writer/<int:id>', views.get_writer, name = "writer"),
    path('aboutus', views.aboutus, name="about"),
    path('sellerdashboard',views.sellerdashboard,name='sellerdashboard'),
    #path('addbook',views.addbookwithform,name='addbook'),
    path('addbook',AddBook.as_view(),name='addbook'),
    path('getallbooks',views.getAllbooks,name='getallbooks'),
    path('getbookaddbyuser',getBookaddbyuser.as_view(),name='bookaddbyuser'),
    path('deletebook/<int:id>',views.deleteBook,name='deletebook'),
    path('updatebook/<int:id>',views.updateBook,name='updatebook'),
]
