from django import forms
from . import models
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
	captcha = CaptchaField()

	class Meta:
		model = models.Contact
		fields = ['user_name', 'message_subject2', 'user_email', 'user_message']

	def __int__(self, *args, **kwargs):
		super(ContactForm, self).__int__(*args, **kwargs)
		self.fields['user_name'].label = "Your name"
		self.fields['message_subject2'].label = "Message subject 2"
		self.fields['user_email'].label = "Email"
		self.fields['user_message'].label = "Message"
		self.fields['captcha'].label = "Verification"


def create_form(catg1=None, catg2=None):

	class ContactForm1(forms.Form):
		choices = []
		if catg1 is None:
			message_sub1 = models.message_subject_1.objects.all()
			for m in message_sub1:
				choices.append([str(m), str(m)])
		else:
			message_sub1 = models.message_subject_1.objects.get(title=catg1)
			m = message_sub1
			choices.append([str(m), str(m)])

		category = forms.ChoiceField(label='Message Subject', choices=choices, required=True)

	form = ContactForm1

	if catg2 is not None:
		class ContactForm2(ContactForm1):
			message_sub2 = models.message_subject_2.objects.filter(category=catg2)
			choices = []
			for m in message_sub2:
				choices.append([str(m), str(m)])
			category2 = forms.ChoiceField(label='Message Subject 2', choices=choices, required=True)

		class ContactForm3(ContactForm2):
			name = forms.CharField(label='Your name', max_length=50)
			email = forms.EmailField(label="Email")
			message = forms.CharField(label='Message', widget=forms.Textarea)
			captcha = CaptchaField()

		form = ContactForm3

	return form


def create_form2():
	class ContactMsmSub1Form(forms.Form):
		message_sub1 = models.message_subject_1.objects.all()
		choices = []
		for m in message_sub1:
			choices.append([str(m), str(m)])
		category = forms.ChoiceField(label='Message Subject', choices=choices, required=True, )

	return ContactMsmSub1Form
