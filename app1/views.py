

from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import LoginForm,SearchForm
from django.db.models import Q  
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
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
    list(messages.get_messages(request))

    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('lastname')
        c = request.POST.get('email')
        d = request.POST.get('subject')
        e = request.POST.get('message')
        f= request.POST.get('submitted_at')

        form1 = m_form(name = a,lastname = b,email = c,subject = d,message=e,submitted_at=f)
        form1.save()
        messages.success(request,'Submmited successfully')
        return redirect('contact') 
    
    data=(m_form.objects.all())
    forms={'form_data':data}
    return render(request,'contact.html',forms)


def login_page(request):
    list(messages.get_messages(request))

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

    storage = messages.get_messages(request) # to clear old message after logout 
    for _ in storage:
        pass
    storage.used = True

    messages.success(request, "You have been logged out!")
    return redirect('login')




def search_results(request):
    list(messages.get_messages(request))

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



def about(request):
    return render(request,'about.html')

def booking(request):
    list(messages.get_messages(request))

    if request.method == 'POST':
        # Getting the data from the form manually
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create a new booking entry and save it
        if name and email and date and time and guests and phone and message:
            booking = Booking(
                name=name,
                email=email,
                date=date,
                time=time,
                guests=guests,
                phone=phone,
                message=message,
                submitted_at=timezone.now()
            )
            booking.save()

         
            messages.success(request, "Booking submitted successfully!")
            return redirect('booking')
        else:
            messages.error(request, "All fields are required!")
    
    return render(request, 'booking.html')




