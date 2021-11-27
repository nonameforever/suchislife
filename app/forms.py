"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import fields
from django.utils.translation import ugettext_lazy as _

from .models import Comment

class BootstrapAuthenticationForm(AuthenticationForm):
  """Authentication form which uses boostrap CSS."""
  username = forms.CharField(max_length=254,
  widget=forms.TextInput({
    'class': 'form-control login-input',
    'placeholder': 'Имя пользователя'}))
  password = forms.CharField(label=_("Password"),
    widget=forms.PasswordInput({
      'class': 'form-control login-input',
      'placeholder':'Пароль'}))

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('text',)