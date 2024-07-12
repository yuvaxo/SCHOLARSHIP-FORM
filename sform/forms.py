from django import forms
from .models import Student, Location, College, Bank
import random, os, string
from django.conf import settings
import json


json_path = os.path.join(settings.BASE_DIR, 'sform', 'static', 'plocation.json')
with open(json_path) as file:  # Update the path to your JSON file
    data = json.load(file)

# Ensure data is a dictionary with states as keys and lists of cities as values
STATE_CHOICES = [(state, state) for state in data.keys()]
CITY_CHOICES = {state: [(city, city) for city in cities] for state, cities in data.items()}

class StudentForm(forms.ModelForm):
    community_file = forms.FileField(required=False)
    income_file = forms.FileField(required=False)
    
    
    
    COMMUNITY_CHOICES = [
        ('GEN','General'),
        ('SC','Scheduled Caste'),
        ('ST','Scheduled Tribes'),
        ('OBC','OBC'),
        ('EWS','EWS'),
    ]
    
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    # Update sex field to use ChoiceField with Select widget
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    community = forms.ChoiceField(choices=COMMUNITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Student
        fields = [
            's_name', 'sex', 'dob', 'edu_year',
            'f_m_name', 'community', 'p_income', 'community_file',
            'income_file', 'password'
        ]
        labels = {
            's_name': 'Student Name',
            'dob': 'Date of Birth',
            'edu_year': 'Graduation Year',
            'f_m_name': 'Father/Mother Name',
            'p_income': "Parents' Income",
        }
        widgets = {
            's_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'edu_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'f_m_name': forms.TextInput(attrs={'class': 'form-control'}),
            'community': forms.TextInput(attrs={'class': 'form-control'}),
            'p_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        student = super().save(commit=False)
        edu_year = str(self.cleaned_data['edu_year'])
        random_number = ''.join(random.choices(string.digits, k=6))
        student.s_code = int(edu_year + random_number)

        if commit:
            student.save()
            
        community_file = self.cleaned_data.get('community_file')
        if community_file:
            student.community_attach = community_file.read()
            student.ca_name = community_file.name

        # Handle income file
        income_file = self.cleaned_data.get('income_file')
        if income_file:
            student.income_attach = income_file.read()
            student.ia_name = income_file.name

        return student
    

class LocationForm(forms.ModelForm):
    states = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_states'}))
    
    ruchoice = {
            ('R', 'Rural'),
            ('U','Urban')
    }
    r_u = forms.ChoiceField(choices=ruchoice, widget=forms.Select(attrs={'class': 'form-control'}),label='Rural/Urban')
    
   
   
    class Meta:
        
        model = Location
        fields = '__all__'
        
        
        labels = {
            's_code': 'Student Code',
            'r_u': 'Rural/Urban',
            'addr1': 'Address 1',
            'addr2': 'Address 2',
            'p_name': 'Postal Name',
            'd_name': 'City',
            'states': 'State',
        }
        
        widgets = {
            's_code': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'r_u': forms.TextInput(attrs={'class': 'form-control'}),
            'addr1': forms.TextInput(attrs={'class': 'form-control'}),
            'addr2': forms.TextInput(attrs={'class': 'form-control'}),
            'p_name': forms.TextInput(attrs={'class': 'form-control'}),
            'd_name': forms.TextInput(attrs={'class': 'form-control'}),
            'states': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        def __init__(self, *args, **kwargs):
            super(LocationForm, self).__init__(*args, **kwargs)
            self.fields['d_name'].choices = []


class CollegeForm(forms.ModelForm):
    l_name = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_states'}),label='Location')
    
    class Meta:
        model = College
        fields = '__all__'
        
        widgets = {
            's_code': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'c_code': forms.NumberInput(attrs={'class': 'form-control',}),
            'c_name': forms.TextInput(attrs={'class': 'form-control'}),
            'l_name': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            's_code': 'Student Code',
            'c_code': 'College Code',
            'c_name': 'College Name',
            'l_name': 'Location',
        }


# class BankForm(forms.ModelForm):
#     class Meta:
#         model = Bank
#         fields = '__all__'
#         widgets = {
#             'acc_no': forms.NumberInput(attrs={'class': 'form-control'}),
#             's_code': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
#             'ifsc': forms.TextInput(attrs={'class': 'form-control'}),
#             'b_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'b_loc': forms.TextInput(attrs={'class': 'form-control'}),
#             'b_addr': forms.TextInput(attrs={'class': 'form-control'}),
#         }
        
class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
        
        labels = {
            
            'acc_no': 'Account Number',
            's_code': 'Student Code',
            'ifsc': 'IFSC CODE',
            'b_name': 'Bank Name',
            'b_loc': 'Bank Location',
            'b_addr': 'Bank Address',
        }
        
        widgets = {
            
            'acc_no': forms.NumberInput(attrs={'class': 'form-control'}),
            's_code': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'ifsc': forms.TextInput(attrs={'class': 'form-control', 'id': 'ifsc'}),
            'b_name': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control', 'id': 'b_name'}),
            'b_loc': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control', 'id': 'b_loc'}),
            'b_addr': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control', 'id': 'b_addr'}),
        }


class LoginForm(forms.Form):
    s_code = forms.CharField(label="Student Code")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
