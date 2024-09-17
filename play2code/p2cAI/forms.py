# qna/forms.py
from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(
        label="Ask a question:", widget=forms.Textarea(attrs={"rows": 4})
    )
