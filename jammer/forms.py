from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import magic


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


class UploadFileForm(forms.Form):
    background_pic_form = forms.FileField(required=False)
    profile_pic_form = forms.FileField(required=False)

    def clean_file(self, file_):
        valid_img_ext = [
            "jpg",
            "jpeg",
            "png",
            "gif"
        ]

        file_from_mem = self.cleaned_data.get(file_, False)
        filetype = magic.from_buffer(file_from_mem.read())
        for img_types in valid_img_ext:
            if img_types in filetype.lower():
                return file_from_mem

        raise ValidationError("Not a valid image file")