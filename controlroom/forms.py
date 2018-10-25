from django import forms
from .models import event
from controlroom.validators import isnumber, vaildusers

class eventform(forms.ModelForm):
		model=event
		class Meta:
				model=event
				fields=['event_id',
				'event_name',
				'winner1',
				'winner2',
				'winner3',
				'short_list',
				'participants']


		event_id=forms.CharField(max_length=6,required=True,label='Event Id',widget=forms.TextInput(attrs={
				"placeholder":"Event ID",
				'readonly':'readonly',
				"class":"form-control ",
				"style":"height:50px;margin-bottom:20px;"
				}))
		event_name=forms.CharField(max_length=100,label='Event Name',widget=forms.TextInput(attrs={
				"placeholder":"Event Name",
				'readonly':'readonly',
				"class":"form-control",
				"style":"height:50px;margin-bottom:20px;"
				}))
		participants=forms.CharField(max_length=10000,validators=[vaildusers],label='participants',required=False,widget=forms.TextInput(attrs={

				"placeholder":"participants",
				"class":"form-control",
				"style":"height:50px;margin-bottom:20px;"
				}))

		short_list=forms.CharField(max_length=200,label='ShortListed',validators=[vaildusers],required=False,widget=forms.TextInput(attrs={
				"placeholder":"Shortlisted participants",
				"class":"form-control",
				"style":"height:50px;margin-bottom:30px;"
				}))

		winner1=forms.CharField(max_length=60,label='Winner1',validators=[vaildusers],required=False,widget=forms.TextInput(attrs={
				"placeholder":"Winner1",
				"class":"form-control",
				"style":"height:50px;margin-bottom:30px;"
				}))
		winner2=forms.CharField(max_length=60,label='Winner2',validators=[vaildusers],required=False,widget=forms.TextInput(attrs={
				"placeholder":"Winner2",
				"class":"form-control",
				"style":"height:50px;margin-bottom:30px;"
				}))
		winner3=forms.CharField(max_length=60,label='Winner3',validators=[vaildusers],required=False,widget=forms.TextInput(attrs={
				"placeholder":"winner3",
				"class":"form-control",
				"style":"height:50px;margin-bottom:20px;"
				}))

		'''def clean(self):
				cleaned_data=super(eventform,self).clean()
				print(cleaned_data)'''
