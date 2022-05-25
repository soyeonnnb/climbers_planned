from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "이메일"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is Wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User Does Not Exist."))


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs = {
            "class": "form-control",
            "id": "numberInput",
            "type": "text",
            "placeholder": "이메일",
            "name": "userID",
            "maxlength": "20",
        }
        self.fields["password"].widget.attrs = {
            "class": "form-control",
            "id": "numberInput",
            "type": "password",
            "placeholder": "비밀번호",
            "name": "userPassword",
            "maxlength": "20",
        }
    
    


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("name", "nickname", "email")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "이름"}),
            "nickname": forms.TextInput(attrs={"placeholder": "닉네임"}),
            "email": forms.EmailInput(attrs={"placeholder": "이메일"}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호 확인"})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("이미 존재하는 이메일입니다.", code="existing_user")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        # commit=False -> 생성은 하되 db에는 올리지 말라는 뜻
        user.username = email
        user.set_password(password)
        user.save()

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs = {
            "class": "form-control",
            "id": "numberInput",
            "type": "text",
            "placeholder": "이메일",
            "name": "userID",
            "maxlength": "20",
        }
        self.fields["password"].widget.attrs = {
            "class": "form-control",
            "id": "numberInput",
            "type": "password",
            "placeholder": "비밀번호",
            "name": "userPassword",
            "maxlength": "20",
        }
        self.fields["name"].widget.attrs = {
            "class": "form-control",
            "id": "numberInput",
            "type": "text",
            "placeholder": "이름",
            "name": "userName",
            "maxlength": "20",
        }
        self.fields["nickname"].widget.attrs = {
            "class": "form-control",
            "id": "numberInput",
            "type": "text",
            "placeholder": "닉네임",
            "name": "userNickname",
            "maxlength": "20",
        }
