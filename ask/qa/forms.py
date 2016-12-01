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

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
