from django import forms
from django.contrib.auth.models import User
from workers.models import Departaments
from account.models import Position
from workers.models import Workers,Units,Departament_block
# Create your models here.
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторить пароль',widget=forms.PasswordInput)
    departament = forms.ModelChoiceField(queryset=Departaments.objects.all(),label='Департамент')
    position = forms.ModelChoiceField(queryset=Position.objects.all(),label='Должность')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']

class WorkerEdit(forms.ModelForm):
    class Meta:
        model=Workers
        fields=['room','ip_number','mobile_phone','phone']

class New_worker_edit(forms.ModelForm):
    class Meta:
        model=Workers
        fields=['fullname','deps','deps_block','position','room','ip_number','mobile_phone','phone','status','date_out','date_in']
        widgets = {
            'deps': forms.HiddenInput(),
            'deps_block': forms.HiddenInput(),
            'date_out':forms.SelectDateWidget(),
            'date_in':forms.SelectDateWidget(),

            'room': forms.HiddenInput(),
            'ip_number': forms.HiddenInput(),
            'mobile_phone': forms.HiddenInput(),
            'phone': forms.HiddenInput(),
        }

class Units_form(forms.ModelForm):
    class Meta:
        model=Units
        fields=['name']
class Departament_form(forms.ModelForm):
    class Meta:
        model=Departaments
        fields=['name','units']
        widgets = {'units': forms.HiddenInput()}
class Departament_block_form(forms.ModelForm):
    class Meta:
        model=Departament_block
        fields=['name','deps']
        widgets = {'deps': forms.HiddenInput()}
class Departament_workers_form(forms.ModelForm):
    class Meta:
        model=Workers
        fields=['fullname','deps','position','room','ip_number','city','mobile_phone','phone','status','date_out','date_in']
        widgets={'deps':forms.HiddenInput(),
                 'date_out': forms.HiddenInput(),
                         'date_in': forms.HiddenInput(),
                         'status': forms.HiddenInput(),
                 'room': forms.HiddenInput(),
                 'ip_number': forms.HiddenInput(),
                 'mobile_phone': forms.HiddenInput(),
                 'phone': forms.HiddenInput(),

        }
class WorkerAdd(forms.ModelForm):
    class Meta:
        model=Workers
        fields=['fullname','deps','deps_block','position','city','room','ip_number','mobile_phone','phone','status','date_out','date_in']
        widgets = {
            'deps': forms.HiddenInput(),
            'deps_block': forms.HiddenInput(),
            'date_out': forms.HiddenInput(),
            'date_in': forms.HiddenInput(),

            'status': forms.HiddenInput(),
            'room': forms.HiddenInput(),
            'ip_number': forms.HiddenInput(),
            'mobile_phone': forms.HiddenInput(),
            'phone': forms.HiddenInput(),
        }