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

TESTS = ( 
	('Breathalyzer','breathalyzer'),
	('Balance and coordination tests','balance and coordination tests'),
	('Eye movement test (pen test)','eye movement test (pen test)'),
	('Blood test','blood test'),
	('Other','Other'),
	)

REASONS = (
	('Speeding'),('Swerving'), ('Illegal maneuver'),
	('Reckless driving'), ('Equipment violation (missing headlight, excessive window tinting, etc.)'),
	('DUI checkpoint'), ('Other'),
	)

SITUATION = (
	('I was questioned'),
	('I was detained'),
	('I was arrested'),
	('I was formally charged with a crime')
	)

CHOICES1 = (('1', 'Yes',), ('2', 'No',),('3','Not Sure',))
CHOICES2 = (('1', 'Male',), ('2', 'Female',))
CHOICES3 = (('1', 'Yes',), ('2', 'No',))
CHOICES4 = (('1','Morning'),('2','Afternoon'),('3','Evening'),('4','Late Night'))
CHOICES5 = (('1','No'),('2','Yes, I do'),('3','Yes, my partner does'),('4','Yes, we both do'),('5','I\'m not sure'))
CHOICES6 = (('1','Buying a business'),('2','Selling a business'),('3','Merging with another company'))
CHOICES7 = (('1','Buying an estate'),('2','Selling an estate'))
CHOICES8 = (('1','Condominium'),('2','Single family home'),('3','Multi-family complex'),
	('4','Office building'),('5','Shopping center'),('6','Land'),('7','Industrial'),('8','Other'))


class divorceForm(forms.Form):
	spouse = forms.CharField(label='What is your Spouse\'s name?', max_length = 25)
	date_of_marriage = forms.DateField(initial=datetime.date.today,label = 'What was your Date of Marriage?')
	gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES2, label = 'Gender of your spouse?')
	mutual = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES1, label = 'Was a pre-nuptial agreement in place at the time of marriage?')
	assets = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=ASSETS, label = 'What Assets did spouse have before marriage? (Select All that Apply)')
	assets_before = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=ASSETS, label = 'What Assets did spouse acquire after marriage? (Select All that Apply)')
	children = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES3, label = 'Do you have children?')
	custody = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES1, label = 'Will either spouse be asking for child support?')
	budget = forms.CharField(label='What is your estimated budget?')
	details = forms.CharField(label='Further Details')

class duiForm(forms.Form):
 	date_of_citation = forms.DateField(initial = datetime.date.today , label = 'When did you receive the DUI citation?');
 	tests = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices = TESTS,
 		label =  'What sobriety tests did the officer perform to measure your intoxication level? (Select all that apply)')
 	bac = forms.DecimalField(label = 'If applicable, What was your Blood Alcohol Content (BAC)?',decimal_places=2, null = True)
 	time_of_day = forms.ChoiceField(widget = forms.RadioSelect, label = 'What time of day were you pulled over?', choices = CHOICES4)
 	reason = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = REASONS, label = 'Why were you pulled Over? (Select all that apply)')
 	past = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES3, label = 'Have you had a DUI in the past?')
 	next_date = forms.DateField(initial = datetime.date.today + timedelta(days = 7), label = 'When is your next court date?')
 	budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2, null=True)
 	details = forms.CharField(label = 'Further Details')

class criminalForm(forms.Form):
 	offense = forms.CharField(label = 'What is the name of the offense?')
 	offense_date = forms.DateField(initial = datetime.date.today, label = 'What date did the incident occur?')
 	situation = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = SITUATION, 
 		label= 'Which of the following best describe your situation?')
	agency = forms.CharField(label = 'What was the law enforcement agency involved?')
 	court_past = forms.ChoiceField(widget = forms.RadioSelect, label = 'Have you already been to court for this matter?', choices = CHOICES3)
 	next_date = forms.DateField(initial = datetime.date.today + timedelta(days = 7), label = 'When is your next court date?')
 	worked = forms.ChoiceField(widget = forms.RadioSelect ,label = 'Have you previously worked with a lawyer on this matter?', choices = CHOICES3)
 	budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2, null=True)
 	details = forms.CharField(label = 'Further Details')

class prenupForm(forms.Form):
 	partner = forms.CharField(label = 'What is your partner\'s name?', max_length = 25)
 	assets = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = ASSETS, 
 		label = 'Which assests do you own that will be part of the pre-nuptial agreement? (Select all that apply)')
 	debt = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES5, label = 'Do you or your partner have any debt?')
 	debt_details = forms.CharField(label = 'If yes, please explain the type of the debt and approximate amount')
	assets_exclude = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES1, 
 		label = 'Are there any assets that you or your partner would like to exclude from the pre-nuptial agreement?')
 	exclude_details = forms.CharField(label = 'If yes, Please explain')
 	budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2, null=True)

class mergerForm(forms.Form):
 	types = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES6, label = 'Which of the following do you need help?')
 	names = forms.CharField(label  = 'What are the names of all the parties involved in the transaction?')
 	circumstances = forms.CharField(label = 'Describe the circumstances of the sale or merger in as much details as possible:')
 	need = forms.CharField(label = 'What do you need a lawyer to help with?')
 	budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2, null=True)

class estateForm(forms.Form):
	types  = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES7, label = 'What do you want to do?')
	property_type = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES8, label = 'What type of property is involved?')
	details = forms.CharField(label= 'Describe your legal issues in as much details as possible:', widget=forms.Textarea)
	need = forms.CharField(label = 'What do you need a lawyer to help with?', widget=forms.Textarea)
	budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2)