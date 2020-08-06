import io
from django import forms
from .models import Book

class DataForm(Book):
    data_file = forms.FileField()