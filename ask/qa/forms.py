from django import forms
from django.contrib.auth.forms import UserCreationForm
from qa.models import Question, Answer, User

class AskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=150)
    text = forms.CharField(label="Text of the Question", widget=forms.Textarea)
    def clean(self):
        return self.cleaned_data
    def save(self):
        self.cleaned_data['author'] = self._user
        q = Question(**self.cleaned_data)
        q.save()
        return q

class AnswerForm(forms.Form):
    text = forms.CharField(label="Answer", widget=forms.Textarea)
    question = forms.IntegerField(label="", widget=forms.HiddenInput)
    def clean(self):
        return self.cleaned_data
    def save(self):
        q_id = self.cleaned_data['question']
        q = Question.objects.get(id=q_id)
        self.cleaned_data['question']=q
        self.cleaned_data['author'] = self._user
        a = Answer(**self.cleaned_data)
        a.save()
        return a

class SignupForm(forms.Form):
    username = forms.CharField(label="Username:")
    email = forms.EmailField(label="Email:")
    password = forms.CharField(label="Password:", widget=forms.PasswordInput)
    def clean(self):
        return self.cleaned_data
    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
        return user
