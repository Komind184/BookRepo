from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Category, Writer, Book, Review, Slider
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import RegistrationForm, ReviewForm , BookForm
from django.http import HttpResponse
from django.views.generic import CreateView,ListView



def signin(request):
    if request.user.is_authenticated:
        return redirect('store:index')
    else:
        if request.method == 'POST': #if someone fills out form , Post it 
            username = request.POST['user']
            password = request.POST['pass']
            checkuser = request.POST['check']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:# if user exist
                if checkuser == 'SELLER':
                    login(request, user)
                    messages.success(request,('Youre logged in'))
                    return redirect('store:sellerdashboard') #routes to 'home' on successful login   
                else:
                    login(request, user)
                    messages.success(request,('Youre logged in'))
                    return redirect('store:index')           
            else:
                messages.success(request,('Error logging in'))
                return redirect('store:signin') #re routes to login page upon unsucessful login
        else:
            return render(request, 'store/login.html', {})	


def signout(request):
    logout(request)
    return redirect('store:signin')	

def registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('store:signin')
    return render(request,'store/signup.html', {"form": form})


def payment(request):
    return render(request, 'store/payment.html')



def get_books(request):
    books_ = Book.objects.all().order_by('-created')
    paginator = Paginator(books_, 10)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, "store/category.html", {"book":books})

def get_book_category(request, id):
    book_ = Book.objects.filter(category_id=id)
    paginator = Paginator(book_, 10)
    page = request.GET.get('page')
    book = paginator.get_page(page)
    return render(request, "store/category.html", {"book":book})

def get_writer(request, id): 
    context = {
        "wrt": wrt,
        "book": book
    }
    return render(request, "store/writer.html", context)

def aboutus(request):
    return render(request,'store/about.html')

def sellerdashboard(request):
    return render(request,'store/sellerdashboard.html')


class AddBook(CreateView):
    form_class = BookForm
    model = Book
    success_url ="/getallbooks"
    template_name = 'store/addbookwithform.html'


def getAllbooks(request):
    allbook = Book.objects.all().values()
    return render(request,'store/allbooks.html',{'allbooks':allbook})

class getBookaddbyuser(ListView):
    model = User

    def get(self,request, *args, **kwargs):
        user = request.user
        bookadd = Book.objects.filter(user=request.user).values()

        return render(request,'store/getbookaddbyuser.html',{'bookadds':bookadd})
   
def deleteBook(request,id):
    
    bk = Book.objects.get(id=id)
    bk.delete()
    return redirect('store:bookaddbyuser')
        
    
def updateBook(request,id):
    bk = Book.objects.get(id=id)
    form = BookForm(request.POST or None,instance=bk)
    if form.is_valid():
        bk.save()
        return redirect('store:bookaddbyuser')
    
    return render(request,'store/updatebook.html',{'form':form})