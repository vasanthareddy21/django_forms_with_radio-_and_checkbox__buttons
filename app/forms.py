from django import forms

g=[('female','FEMALE'),('male','MALE')]
c=[('python','python'),('django','django'),('api','api'),('selenium','selenium')]
class RegistrationForm(forms.Form):
    
    Name=forms.CharField()
    age=forms.IntegerField()
    password=forms.CharField(max_length=10,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #courses=forms.MultipleChoiceField(choices=c)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)