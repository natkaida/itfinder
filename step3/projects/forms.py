from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'image', 'tags', 'description', 'demo_link', 'source_link']
        labels = {
            'title': 'Название проекта',
            'slug': 'Слаг',
            'image':'Скриншот проекта',
            'tags':'Теги', 
            'description':'Описание проекта',
            'demo_link':'Демо-версия',
            'source_link':'Исходный код на GitHub'
        }

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})    