from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    """

    Create a model form. This will generate and map
    the fields from the registration html page to the
    database fields.

    """

    # Overloading the password field, you can overload any
    # field that's declared in the user model.

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password'
                  ]
