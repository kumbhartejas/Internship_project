from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from app1.models import *
from app1.form import SectionForm, ItemForm

@login_required(login_url='login')
def dashboard(request):
    unseen_bookings = Booking.objects.filter(is_seen=False).order_by('-submitted_at')
    latest_contacts = m_form.objects.filter(is_seen=False).order_by('-submitted_at')

    context = {
        'unseen_bookings': unseen_bookings,
        'latest_contacts': latest_contacts,
    }
    return render(request, 'Dashboard/dashboard.html', context)

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

@login_required(login_url='login')
def sections_list(request):
    sections = Section.objects.all()
    return render(request, 'Dashboard/sections_list.html', {'sections': sections})

@login_required(login_url='login')
def section_items(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    items = item.objects.filter(section=section)
    return render(request, 'Dashboard/section_items.html', {'section': section, 'items': items})

@login_required(login_url='login')
def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Section created successfully.')
            return redirect('sections_list')
    else:
        form = SectionForm()
    return render(request, 'Dashboard/add_section.html', {'form': form})

@login_required(login_url='login')
def edit_section(request, section_id):
    section_instance = get_object_or_404(Section, id=section_id)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Section updated successfully.')
            return redirect('sections_list')
    else:
        form = SectionForm(instance=section_instance)
    return render(request, 'Dashboard/add_section.html', {'form': form, 'edit': True, 'section': section_instance})

@login_required(login_url='login')
def delete_section(request, section_id):
    section_instance = get_object_or_404(Section, id=section_id)
    if request.method == 'POST':
        section_instance.delete()
        messages.success(request, 'Section deleted successfully.')
        return redirect('sections_list')
    return render(request, 'Dashboard/confirm_delete_section.html', {'section': section_instance})

@login_required(login_url='login')
def add_item(request, section_id=None):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item_instance = form.save(commit=False)
            item_instance.slug = slugify(item_instance.name)
            item_instance.save()
            messages.success(request, 'Item created successfully.')
            if section_id:
                return redirect('section_items', section_id=section_id)
            else:
                return redirect('sections_list')
    else:
        if section_id:
            section = get_object_or_404(Section, id=section_id)
            form = ItemForm(initial={'section': section})
        else:
            form = ItemForm()
    return render(request, 'Dashboard/add_item.html', {'form': form})

@login_required(login_url='login')
def edit_item(request, item_id):
    item_instance = get_object_or_404(item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item_instance)
        if form.is_valid():
            item_instance = form.save(commit=False)
            item_instance.slug = slugify(item_instance.name)
            item_instance.save()
            messages.success(request, 'Item updated successfully.')
            return redirect('section_items', section_id=item_instance.section.id)
        else:
            messages.error(request, f"Form errors: {form.errors}")
    else:
        form = ItemForm(instance=item_instance)
    return render(request, 'Dashboard/edit_item.html', {'form': form, 'edit': True, 'item': item_instance})

@login_required(login_url='login')
def delete_item(request, item_id):
    item_instance = get_object_or_404(item, id=item_id)
    section_id = item_instance.section.id
    if request.method == 'POST':
        item_instance.delete()
        messages.success(request, 'Item deleted successfully.')
        return redirect('section_items', section_id=section_id)
    return render(request, 'Dashboard/confirm_delete.html', {'item': item_instance})

@login_required(login_url='login')
def item_detail(request, slug):
    item_instance = get_object_or_404(item, slug=slug)
    return render(request, 'Dashboard/item_detail.html', {'item': item_instance})

@login_required(login_url='login')
def contact(request):
    con = m_form.objects.all()
    contf={'cf':con}
    return render(request,'Dashboard/ContactForm.html',contf)

@login_required(login_url='login')
def booking(request):
    book = Booking.objects.all()
    bookf={'bf':book}
    return render(request,'Dashboard/bookingForm.html',bookf)

@login_required(login_url='login')
def edit_book(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.method == 'POST':
        booking.name = request.POST.get('name')
        booking.email = request.POST.get('email')
        booking.date = request.POST.get('date')
        booking.time = request.POST.get('time')
        booking.guests = request.POST.get('guests')
        booking.message = request.POST.get('message')
        booking.save()
        return redirect('bookingform')  # after save, go back to booking list

    return render(request, 'Dashboard/edit_booking.html', {'booking': booking})

# Delete View
@login_required(login_url='login')
def delete_book(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.delete()
    return redirect('bookingform')  


@login_required(login_url='login')
def edit_contacts(request, id):
    contact = get_object_or_404(m_form, id=id)  # Adjust model name if needed
    if request.method == 'POST':
        contact.name = request.POST.get('name')
        contact.lastname = request.POST.get('lastname')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()
        return redirect('contactform')  # After edit, redirect back to the table
    return render(request, 'Dashboard/edit_contact.html', {'contact': contact})

@login_required(login_url='login')
def delete_contacts(request, id):
    contact = get_object_or_404(m_form, id=id)
    contact.delete()
    return redirect('contactform')  