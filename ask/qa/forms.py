from django import forms
from qa.models import Question, Answer

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
