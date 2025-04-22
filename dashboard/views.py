from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth
from django.db.models import Count
from app1.models import Booking, m_form

@login_required(login_url='login')
def dashboard(request):
    unseen_bookings = Booking.objects.filter(is_seen=False).order_by('-submitted_at')
    latest_contacts = m_form.objects.filter(is_seen=False).order_by('-submitted_at')

    bookings_by_month_qs = Booking.objects.annotate(month=TruncMonth('submitted_at')).values('month').annotate(count=Count('id')).order_by('month')
    bookings_by_month = {entry['month'].strftime('%b %Y'): entry['count'] for entry in bookings_by_month_qs}

    context = {
        'unseen_bookings': unseen_bookings,
        'latest_contacts': latest_contacts,
        'bookings_by_month': bookings_by_month,
    }
    return render(request,'Dashboard/dashboard.html', context)

@login_required(login_url='login')
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.is_seen = True
    booking.save()
    return redirect('dashboard')

@login_required(login_url='login')
def delete_contact(request, contact_id):
    contact = get_object_or_404(m_form, id=contact_id)
    contact.is_seen = True
    contact.save()
    return redirect('dashboard')

# Create your views here.
