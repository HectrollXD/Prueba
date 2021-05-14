from django import forms





class AddNewUserForm( forms.Form ):
    CHOICES = [
        ('A', 'Admin'),
        ('B', 'Employe')
    ]

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
        ),
        max_length = 100,
        min_length = 10,
        required = True
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        ),
        max_length = 32,
        min_length = 8,
        required = True
    )

    admin = forms.ChoiceField(
        choices = CHOICES,
        widget = forms.Select(
            attrs = {
                'class': 'form-control text-center'
            }
        ),
    )





class LoginForm( forms.Form ):
    user = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        ),
        min_length = 3,
        max_length = 50,
        required = True,
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )