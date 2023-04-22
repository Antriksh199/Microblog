from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field
from crispy_forms.bootstrap import PrependedText
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

def validateContact(value):
    if (len(value)!=10) or (not value.isdigit()) :
        raise forms.ValidationError('Incorrect Contact Number')
    return value

def validateCountry(value):
    if value == 'NA':
        raise forms.ValidationError('Country is missing')
    return value

def validateState(value):
    if value == 'NA':
        raise forms.ValidationError('State is missing')
    return value

def validateCity(value):
    if value == 'NA':
        raise forms.ValidationError('City is missing')
    return value

def get_country():
    countries = [('0','Select Country')]
    for x in Country.objects.all():
        countries.append((x.pk,x.name))
    return countries

Interests = (('NA','Select Interests'),
('Scinece & Technology','Scinece & Technology'),
('Banking & Finance','Banking & Finance'),
('History & Culture','History & Culture'),
('Arts','Arts'),
('Politics & Debate','Politics & Debate')
)


education = (
    ('NA','Select Education'),
('High School','High School'),
('Intermediate','Intermediate'),
('Undergraduate','Undergraduate'),
('Graduate','Graduate'),
('Masters','Masters'),
('6','Doctorate')
)

gender=[('NA','Select Gender'),
            ('Male','Male'),
            ('Female','Female'),
            ('Others','Others')]

def validateState(state):
    if state == 'NA' or state is None:
        raise forms.ValidationError("State is required.")
    return state

def validateCity(city):
    if city == 'NA' or city is None:
        raise forms.ValidationError("City is required.")
    return city

def validateGender(value):
    if value == 'NA' or value is None:
        raise forms.ValidationError("Gender is required")
    return value

def validateEducation(value):
    if value == 'NA' or value is None:
        raise forms.ValidationError("Education is required")
    return value


class SignUpForm(forms.Form,UserCreationForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'email','class':'form-control'}) ,max_length=30,label="Email",help_text='Enter Email',error_messages={'required':'Email is required.'})
    fname = forms.CharField(widget=forms.TextInput(attrs={'id':'fname','class':'form-control'}),max_length=30,label='First Name',help_text="Enter First Name",error_messages={'required':'First Name is required.'})
    lname = forms.CharField(widget=forms.TextInput(attrs={'id':'lname','class':'form-control'}),max_length=30, label='Last Name',help_text='Enter Last Name',error_messages={'required':'Last Name is required.'})
    country = forms.ChoiceField(choices=get_country(),widget=forms.Select(attrs={'id':'country','class':'form-select'}),label="Country",error_messages={'required':'Country is required.'},validators=[validateCountry],help_text='Select your Country.')
    contact = forms.CharField(widget=forms.TextInput(attrs={'id':'contact','class':'form-control'}),label="Contact",help_text="Enter Contact Number without Country Code.",error_messages={'required':'Contact is required.'},validators=[validateContact])
    #code = forms.CharField(widget=forms.TextInput(attrs={'id':'code','name':'code','class':'form-control'}))
    state = forms.CharField(validators=[validateState])
    city = forms.CharField(validators=[validateCity])
    dob = forms.CharField(widget=forms.TextInput(attrs={'type':'date','id':'dob','class':'form-control'}),label='Date of Birth',help_text='Date is mm/dd/yyyy format.',error_messages={'required':'Date of Birth is required.'})
    interest = forms.MultipleChoiceField(choices=Interests,widget=forms.CheckboxSelectMultiple(attrs={'id':'interest','class':'form-control'}),error_messages={'required':'You need to select atleast one Interest.'})
    gender = forms.ChoiceField(choices=gender,widget=forms.Select(attrs={'id':'gender','class':'form-select'}),error_messages={'required':'Gender is required.'},validators=[validateGender])
    education = forms.ChoiceField(choices=education,widget=forms.Select(attrs={'id':'education','class':'form-select'}),error_messages={'required':'Education is required.'},validators=[validateEducation])
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


class EditUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'uname','class':'form-control','readonly':'true','required':'false'}),label='Username',required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'email','class':'form-control'}) ,max_length=30,label="Email",help_text='Enter Email',error_messages={'required':'Email is required.'})
    fname = forms.CharField(widget=forms.TextInput(attrs={'id':'fname','class':'form-control'}),max_length=30,label='First Name',help_text="Enter First Name",error_messages={'required':'First Name is required.'})
    lname = forms.CharField(widget=forms.TextInput(attrs={'id':'lname','class':'form-control'}),max_length=30, label='Last Name',help_text='Enter Last Name',error_messages={'required':'Last Name is required.'})
    country = forms.ChoiceField(choices=get_country(),widget=forms.Select(attrs={'id':'country','class':'form-select'}),label="Country",error_messages={'required':'Country is required.'},validators=[validateCountry],help_text='Select your Country.')
    contact = forms.CharField(widget=forms.TextInput(attrs={'id':'contact','class':'form-control'}),label="Contact",help_text="Enter Contact Number without Country Code.",error_messages={'required':'Contact is required.'},validators=[validateContact])
    #code = forms.CharField(widget=forms.TextInput(attrs={'id':'code','name':'code','class':'form-control'}))
    state = forms.CharField(validators=[validateState],help_text='Select Country to change State.')
    city = forms.CharField(validators=[validateCity],help_text='Select State to change City.')
    dob = forms.CharField(widget=forms.TextInput(attrs={'type':'date','id':'dob','class':'form-control'}),label='Date of Birth',help_text='Date is mm/dd/yyyy format.',error_messages={'required':'Date of Birth is required.'})
    interest = forms.MultipleChoiceField(choices=Interests,widget=forms.CheckboxSelectMultiple(attrs={'id':'interest','class':'form-control'}),error_messages={'required':'You need to select atleast one Interest.'})
    gender = forms.ChoiceField(choices=gender,widget=forms.Select(attrs={'id':'gender','class':'form-select'}),error_messages={'required':'Gender is required.'},validators=[validateGender])
    education = forms.ChoiceField(choices=education,widget=forms.Select(attrs={'id':'education','class':'form-select'}),error_messages={'required':'Education is required.'},validators=[validateEducation])
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


