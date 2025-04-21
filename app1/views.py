

from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import LoginForm,SearchForm
from django.db.models import Q  
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.



def home(request):
    sections = Section.objects.filter(name="Foodies Special").prefetch_related('item').all
    img = scroll.objects.all() 
    sec={'sections': sections
         ,'img':img,}
    return render(request, 'index.html', sec)

def detail(request,slug):
    details=get_object_or_404(item,slug=slug)
    source = request.GET.get('from', '')
    if source == 'home':
        back_url = reverse('home')
    elif source == 'explore':
        back_url = reverse('explore')
    else:
        back_url = reverse('home') 

    data={'dish':details,'back_url': back_url
}
    return render (request,"details.html",data)



def explore(request):
    sections=Section.objects.prefetch_related('item').all()
    categ={'cat':sections}
    return render(request, 'Explore.html', categ)

def form(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('lastname')
        c = request.POST.get('email')
        d = request.POST.get('subject')
        e = request.POST.get('message')

        form1 = m_form(name = a,lastname = b,email = c,subject = d,message=e)
        form1.save()
        messages.success(request,'Submmited successfully')
        return redirect('contact') 
    
    data=(m_form.objects.all())
    forms={'form_data':data}
    return render(request,'contact.html',forms)


@login_required(login_url='login')
def login_page(request):
    if request.method == "POST":
        a = request.POST['username']
        b = request.POST['password']
        
        user = authenticate(request, username = a, password = b)

        if user is not None:
         
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')

        else:
           
            messages.error(request, 'In-correct username or password!..')    
        
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('login')




def search_results(request):
    query = request.GET.get('query', '')
    results = []

    if query:
        results = item.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(section__name__icontains=query)|
            Q(price__icontains=query)
        ).select_related('section')

    context = {'query': query, 'results': results}
    return render(request, 'search.html', context)

@login_required(login_url='login')
def dashboard(request):
    return render(request,'Dashboard/dashboard.html')


def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

