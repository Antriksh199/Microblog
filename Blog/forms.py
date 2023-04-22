from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from User.models import *


def validateContent(value):
	if len(value.strip()) == 0:
		print('Empty Content')
		raise forms.ValidationError('Please add content to your blog')
	return value

def validateCategory(value):
	if value.strip() == 'Choose Blog Category':
		raise forms.ValidationError('Please select Blog Category.')
	return value


class BlogForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea(attrs={'id':'form_content','class':'form-control'}),max_length=250,help_text='Tell us what you are thinking in maximum 250 words.',validators=[validateContent])
	category = forms.ChoiceField(widget=forms.Select(attrs={'id':'form_category','class':'form-select'}),validators=[validateCategory])
	title = forms.CharField(widget=forms.TextInput(attrs={'id':'form_title','class':'form-control'}),max_length=20,help_text='Give your blog a title in 20 characters',error_messages={'required':'Title is required.'})

	def __init__(self,user,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.user = user
		interest = UserProfile.objects.filter(user=user).values('interests')
		self.fields['category'].choices=[('Choose Blog Category','Choose Blog Category')]
		self.fields['category'].choices.extend([(i.strip(),i.strip()) for i in interest[0]['interests'].split(';')])

	

class EditBlogForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea(attrs={'id':'edit_form_content','class':'form-control'}),max_length=250,help_text='Tell us what you are thinking in maximum 250 words.',validators=[validateContent])
	category = forms.ChoiceField(widget=forms.Select(attrs={'id':'edit_form_category','class':'form-select'}),validators=[validateCategory])
	title = forms.CharField(widget=forms.TextInput(attrs={'id':'edit_form_title','class':'form-control'}),max_length=20,help_text='Give your blog a title in 20 characters',error_messages={'required':'Title is required.'})

	def __init__(self,user,*args,**kwargs):
		super().__init__(*args,**kwargs)
		#blog = kwargs.pop('blog',None)
		self.user = user
		interest = UserProfile.objects.filter(user=user).values('interests').first()
		print(interest)
		self.fields['category'].choices=[('Choose Blog Category','Choose Blog Category')]
		self.fields['category'].choices.extend([(i.strip(),i.strip()) for i in interest['interests'].split(';')])
		
		
			
		




