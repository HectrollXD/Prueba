from typing_extensions import Required
from django import forms


class AddNewUserForm( forms.Form ):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = { 
                'class': 'form-control',
            }
        ),
        max_length = 50,
        min_length = 3,
        required = True
    )

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = { 
                'class': 'form-control',
            }
        )
    )

    password = forms.PasswordInput(
        Widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )