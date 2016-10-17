from django import forms
from django.contrib.auth.models import User
import datetime
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')
		
		def clean_password2(self):
			cd = self.cleaned_data
			if cd['password'] != cd['password2']:
				raise forms.ValidationError('Passwords don\'t match.')
			return cd['password2']

class SearchForm(forms.Form):
	query = forms.CharField()

ASSETS = (
    ('residential_property', 'Residential Property'),
    ('investment_property', 'Investmant Property'),
    ('investment_account', ' Investment Account(s) (stocks, bonds, mutual funds, etc.) '),
    ('bank_account','Bank Account(s)'),
    ('pension', 'pension, or other retirement plan'),
    ('business','Business interest(s)'),
    ('personal_property','Personal property (jewelry, cars, furniture, appliances, etc.) '),
    ('others','Others'),
    
)
class divorceForm(forms.Form):
	spouse = forms.CharField(label='What is your Spouse\'s name?', max_length = 25)
	date_of_marriage = forms.DateField(initial=datetime.date.today,label = 'What was your Date of Marriage?')
	CHOICES1 = (('1', 'Yes',), ('2', 'No',),('3','Not Sure',))
	CHOICES2 = (('1', 'Male',), ('2', 'Female',))
	CHOICES3 = (('1', 'Yes',), ('2', 'No',))
	gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES2, label = 'Gender of your spouse?')
	mutual = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES1, label = 'Was a pre-nuptial agreement in place at the time of marriage?')
	assets = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=ASSETS, label = 'What Assets did spouse have before marriage? (Select All that Apply)')
	assets_before = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=ASSETS, label = 'What Assets did spouse acquire after marriage? (Select All that Apply)')
	children = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES3, label = 'Do you have children?')
	custody = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES1, label = 'Will either spouse be asking for child support?')
	budget = forms.CharField(label='What is your estimated budget?')
	details = forms.CharField(label='Further Details')