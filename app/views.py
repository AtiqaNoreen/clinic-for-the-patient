from django.shortcuts import render
from .models import Doctor, Appointment
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Case, When, Value, IntegerField
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


def home(request):
    doctors = Doctor.objects.all()
    return render(request, "index.html", {"doctors": doctors})

def search_doctors(request):

    doctor_name = request.GET.get("doctor_name", "").strip()
    specialty = request.GET.get("specialty", "").strip()

    doctors = Doctor.objects.all()

    if doctor_name:
        doctors = doctors.annotate(
            priority=Case(
                When(name__icontains=doctor_name, then=Value(0)),
                default=Value(1),
                output_field=IntegerField(),
            )
        ).order_by("priority", "name")

    if specialty:
        doctors = doctors.annotate(
            sp_priority=Case(
                When(specialty__icontains=specialty, then=Value(0)),
                default=Value(1),
                output_field=IntegerField(),
            )
        ).order_by("sp_priority", "priority", "name")

    html = render_to_string(
        "docter_card.html",
        {"doctors": doctors},
        request=request
    )

    return JsonResponse({
        "html": html
    })


def appointment(request):
    if request.method == "POST":

        Appointment.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            department=request.POST.get("department"),
            doctor=request.POST.get("doctor"),
            date=request.POST.get("date"),
            message=request.POST.get("message"),
        )

        messages.success(request, "Your appointment has been booked successfully!")
        return redirect(reverse("appointment") + "#appointment")

    return render(request, "Appointment.html")

def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, 'services.html')
def doctors(request):
    return render(request, 'doctors.html')

def gallery(request):
    return render(request, 'gallery.html')
def departments(request):
    return render(request, 'departments.html')

def contact(request):
    return render(request, 'contact.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')
def department_details(request):
    return render(request, "department-details.html")


def service_details(request):
    return render(request, 'service-details.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def faq(request):
    return render(request, 'faq.html')



def page404(request):
    return render(request, '404.html')