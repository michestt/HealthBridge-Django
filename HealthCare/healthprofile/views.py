from django.shortcuts import render
from .forms import ProfileForm, ContactForm
from healthprofile import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def profile(request):
    user = request.user
    user_profile = models.Profile.objects.get(user=user)
    user_contact = models.Contact.objects.get(user=user)

    return render(request, "profile/profile.html", locals())


@login_required
def update_profile(request):
    user = request.user
    user_profile = models.Profile.objects.get(user=user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Update Success')
        else:
            messages.warning(request, 'To modify the personal information, each field must be filled in')
    else:
        profile_form = ProfileForm(instance=user_profile)
        messages.warning(request, 'Update Failed')

    return render(request, 'profile/update_profile.html', locals())


@login_required
def update_contact(request):
    user = request.user
    user_contact = models.Contact.objects.get(user=user)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST, instance=user_contact)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Update Success')
        else:
            messages.warning(request, 'To modify the personal information, each field must be filled in')
    else:
        contact_form = ContactForm(instance=user_contact)
        messages.warning(request, 'Update Failed')

    return render(request, 'profile/update_contact.html', locals())
