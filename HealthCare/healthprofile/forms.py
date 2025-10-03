from django import forms
from . import models

class ContactForm(forms.ModelForm):
	class Meta:
		model = models.Contact
		fields = ['phone_number', 'email', 'website']

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['phone_number'].label = 'Contact Number'
		self.fields['email'].label = 'Email'
		self.fields['website'].label = 'Your Personal Website'


class ProfileForm(forms.ModelForm):

	class Meta:
		model = models.Profile
		fields = ['profile_picture', 'country', 'gender', 'BOD', 'self_introduction', 'expertise']

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['profile_picture'].label = 'Profile Picture'
		self.fields['country'].label = 'Country'
		self.fields['gender'].label = 'Male'
		self.fields['BOD'].label = 'BOD'
		self.fields['self_introduction'].label = 'Self Introduction'
		self.fields['expertise'].label = 'Expertise'
