from django import forms
from .models import Bug, Project


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'project', 'status', 'assignee']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assignee'].required = False


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
