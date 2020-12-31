from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        """
            Creating a user login form by inheriting (AuthenticationForm) django authentication form.
            Adding bootstrap class 'form-control' to all visible fields for styling.
            The username field to be set auto focused.
        """

        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == "username":
                visible.field.widget.attrs['autofocus'] = True
                visible.field.widget.attrs['placeholder'] = "Username"
                visible.field.widget.attrs['placeholder'] = "Username"

            if visible.name == "password":
                visible.field.widget.attrs['placeholder'] = 'Password'

            visible.field.widget.attrs['class'] = 'input100'


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'username', 'first_name',  'last_name']

    def __init__(self, *args, **kwargs):
        """
            Creating a user registration form by inheriting (UserCreationForm) django authentication form.
            Adding bootstrap class 'form-control' to all visible fields for styling.
            The email field to be set auto focused.
        """
        super(UserCreate, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['autocomplete'] = 'off'
            visible.field.help_text = ' '

        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['password1'].widget.attrs['placeholder'] = "Password"
        self.fields['password2'].widget.attrs['placeholder'] = "Confirm Password"
        self.fields['first_name'].widget.attrs['placeholder'] = "First Name"
        self.fields['first_name'].widget.attrs['autofocus'] = True
        self.fields['last_name'].widget.attrs['placeholder'] = "Last Name"
        self.fields['username'].widget.attrs['placeholder'] = "username"

        self.fields['username'].widget.attrs['required'] = True
        self.fields['email'].widget.attrs['required'] = True
        self.fields['password1'].widget.attrs['required'] = True
        self.fields['password2'].widget.attrs['required'] = True
        self.fields['first_name'].widget.attrs['required'] = True
        self.fields['last_name'].widget.attrs['required'] = True

