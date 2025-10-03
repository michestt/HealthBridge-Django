from django.shortcuts import render
from contact import models
from . import forms
from django.contrib import messages

# Create your views here.

def contact(request):
	message_sub1 = models.message_subject_1.objects.all()
	form_q1 = forms.create_form2()

	if request.method == 'GET':
		form_res_q1 = form_q1(request.GET)

		if form_res_q1.is_valid():
			category = models.message_subject_1.objects.get(title=str(request.GET['category']))
			message_sub2 = models.message_subject_2.objects.filter(category=category)
			form_q2 = forms.create_form(str(request.GET['category']), category)

	if request.method == "POST":
		category = request.session['category_form']
		category2 = models.message_subject_1.objects.get(title=category)
		form_init = forms.create_form(category, category2)
		form_p = form_init(request.POST)
		if form_p.is_valid():
			name = request.POST['name']
			email = request.POST['email']
			message = request.POST['message']
			subject = models.message_subject_2.objects.get(title=request.POST['category2'])
			post = models.Contact.objects.create(user_name=name, message_subject2=subject, user_email=email, user_message=message)
			post.save()
			messages.add_message(request, messages.SUCCESS, 'Thanks For Your Mail')
		else:
			messages.warning(request, "Please Check Your Message Is CORRECT Or Not")

	# if request.method == "POST":
	# 	form = forms.ContactForm(request.POST)
	# 	if form.is_valid():
	# 		messages.success(request, "Thanks For Your Mail")
	# 		form.save()
	# 	else:
	# 		messages.warning(request, "Please Check Your Message Is CORRECT Or Not")
	# else:
	# 	form = forms.ContactForm()
	#
	return render(request, "contact/contact.html", locals())
