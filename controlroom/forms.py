from django import forms
from .models import event,venue
from controlroom.validators import isnumber,vaildusers





class eventform(forms.ModelForm):
        model=event
        class Meta:
                model=event
                fields=['event_id',
                'event_name',
                'venue_id',
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
        venue_id=forms.CharField(max_length=20,required=True,label='Venue ID',widget=forms.TextInput(attrs={
                "placeholder":"Venue ID",
                'readonly':'readonly',
                "class":"form-control ",
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


class venueform(forms.ModelForm):
        model=venue
        class Meta:
                model=venue
                fields=['venue_id',
                'vm_1',
                'vm_2',
                'vm_num_1',
                'vm_num_2',
                'power',
                'power_num',
                'current_event',
                'occupied'
                ]
        TRUE_FALSE_CHOICES = (
                ('',"Occupied or not"),
                (1, "Occupied"),
                (0, "Free"),)
        venue_id=forms.CharField(max_length=20,required=True,label='Venue ID',widget=forms.TextInput(attrs={
                "placeholder":"Venue ID",
                "class":"form-control ",
                "style":"height:50px;margin-bottom:20px;"
                }))
        vm_1=forms.CharField(max_length=100,label='Venue Manager 1',widget=forms.TextInput(attrs={
                "placeholder":"Venue Manager1",
                "class":"form-control",
                "style":"height:50px;margin-bottom:20px;"
                }))
        vm_2=forms.CharField(max_length=100,label='Venue Manager 2',widget=forms.TextInput(attrs={
                "placeholder":"Venue Manager2",
                "class":"form-control",
                "style":"height:50px;margin-bottom:20px;"
                }))
        vm_num_1=forms.CharField(max_length=10,min_length=10,label='Venue Manager Number 1',widget=forms.TextInput(attrs={
                "placeholder":"Phone number1",
                "class":"form-control",
                "style":"height:50px;margin-bottom:20px;"
                }))
        vm_num_2=forms.CharField(max_length=10,label='Venue Manager Number 2',widget=forms.TextInput(attrs={
                "placeholder":"Phone number2",
                "class":"form-control",
                "style":"height:50px;margin-bottom:20px;"
                }))
        power=forms.CharField(max_length=100,label='power team member',widget=forms.TextInput(attrs={
                "placeholder":"Power team",
                "class":"form-control",
                "style":"height:50px;margin-bottom:20px;"
                }))
        power_num=forms.CharField(max_length=10,label='power team number',widget=forms.TextInput(attrs={
                "placeholder":"Power team phone number",
                "class":"form-control",
                "style":"height:50px;margin-bottom:20px;"
                }))
        current_event=forms.CharField(max_length=100,label='current event',widget=forms.TextInput(attrs={
                "placeholder":"Current event",
                "class":"form-control",
                "style":"height:50px;margin-bottom:20px;"
                }))
